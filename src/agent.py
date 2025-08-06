import os
import base64
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from PIL import Image
from langchain_community.tools.tavily_search import TavilySearchResults

# Load environment variables from a .env file
load_dotenv()

# Initialize the Tavily search tool once to be reused.
tavily_tool = TavilySearchResults()

@tool
def search_web_content(query: str) -> str:
    """
    Searches the web for relevant content based on a given query using Tavily.
    Note: Ensure TAVILY_API_KEY is set in your .env file for this to work.
    """
    results = tavily_tool.invoke({"query": query})
    return results

@tool
def analyze_facial_expression(image_path: str) -> str:
    """
    Analyzes an image of a person's face and returns a description of their
    facial expression and perceived emotion. Use this tool to understand how
    a user is feeling based on a picture of them.
    The input to this tool MUST be a valid file path to an image.
    """
    try:
        if not os.path.exists(image_path):
            return f"Error: Image file not found at {image_path}"

        # Verify it's an image
        Image.open(image_path).verify()

        print(f"Analyzing facial expression from image: {image_path}")

        # Initialize the vision model
        llm_vision = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.2)

        # Encode the image to base64
        with open(image_path, "rb") as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode('utf-8')

        # Prepare the message for the vision model
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": "Analyze this image of a person's face. Describe their primary emotion in a single word (e.g., happy, sad, angry, surprised, neutral). If no face is clear, say 'unknown'. Only return the single word for the emotion.",
                },
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"}},
            ]
        )

        # Invoke the model and get the response
        response = llm_vision.invoke([message])
        emotion = response.content.strip().lower()
        print(f"Vision model detected emotion: {emotion}")
        return f"The user's emotion has been analyzed as: {emotion}"

    except Exception as e:
        return f"An error occurred during image analysis: {e}"

def create_emotion_agent() -> AgentExecutor:
    """
    Creates and returns a LangChain agent configured with Google Gemini.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
    tools = [search_web_content, analyze_facial_expression]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

def get_content_suggestions(image_path: str, agent_executor: AgentExecutor):
    """
    Invokes the agent to get content suggestions for a given emotion.
    """
    if not image_path:
        print("No image path provided. Cannot get suggestions.")
        return

    # The agent is now smart enough to know which tool to use based on the input.
    # We provide the image_path directly in the input dictionary.
    prompt_text = "A user has provided an image of their face. First, analyze their emotion from the image. Then, find uplifting content (articles, videos, activities) based on that emotion. Finally, present the suggestions to the user with a concise summary and a link."
    print("\nAsking agent for content suggestions...")
    response = agent_executor.invoke({
        "input": prompt_text,
        "image_path": image_path
    })
    print("\n--- Suggested Content ---")
    print(response["output"])