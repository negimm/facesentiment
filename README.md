# Face Sentiment Agent

This project is an AI-driven agent that analyzes the sentiment of a person's face from an image and suggests relevant online content (articles, videos, activities, etc.) based on their detected emotion.

## How it Works

The application uses a combination of computer vision and large language models (LLMs) to deliver a personalized content recommendation experience:

1.  **Image Input**: You can either provide a path to an image file or let the application capture a photo of your face using your webcam.
2.  **Facial Analysis**: A powerful vision-capable LLM (Google's Gemini 1.5 Pro) analyzes the image to detect the primary emotion on the user's face (e.g., happy, sad, surprised).
3.  **Intelligent Search**: An autonomous LangChain agent, powered by the Gemini 1.5 Flash model, takes the detected emotion as input.
4.  **Content Recommendation**: The agent uses a search tool (Tavily) to find engaging and relevant web content that matches the user's current mood.
5.  **Output**: The application presents a list of suggested content, complete with summaries and links.

## Features

-   **Webcam Integration**: Capture a photo directly from your webcam.
-   **Local Image Analysis**: Analyze an existing image file.
-   **Emotion-Based Recommendations**: Get content suggestions tailored to your mood.
-   **Powered by Gemini**: Utilizes Google's state-of-the-art multimodal and instruction-following models.
-   **Autonomous Agent**: Employs a LangChain ReAct agent for intelligent decision-making and tool use.

## Tech Stack

-   **Backend**: Python
-   **Dependency Management**: Poetry
-   **AI/LLM Framework**: LangChain
-   **LLM Provider**: Google Gemini
-   **Web Search**: Tavily API
-   **Computer Vision**: OpenCV

## Setup and Installation

### 1. Prerequisites

-   Python 3.9 or higher
-   Poetry installed (`pip install poetry`)
-   Access to a webcam (for webcam capture feature)

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/face-sentiment-agent.git
cd face-sentiment-agent
```

### 3. API Keys

This project requires API keys from two services:

-   **Google AI**: For access to the Gemini models.
    -   Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
-   **Tavily**: For the web search functionality.
    -   Get your key from the [Tavily website](https://tavily.com/).

Create a `.env` file in the root of the project directory and add your keys:

```
GOOGLE_API_KEY="YOUR_GOOGLE_API_KEY"
TAVILY_API_KEY="YOUR_TAVILY_API_KEY"
```

### 4. Install Dependencies

Install the required Python packages using Poetry:

```bash
poetry install
```

## Usage

You can run the application in two ways:

### 1. Analyze an Image from a File

Use the `-i` or `--image` flag to provide the path to an image file.

```bash
poetry run python src/main.py --image /path/to/your/image.jpg
```

### 2. Capture an Image from the Webcam

Run the script without any arguments to activate the webcam.

```bash
poetry run python src/main.py
```

-   A window will open showing your webcam feed.
-   Position your face and press the **'c'** key to capture.
-   Press the **'q'** key to quit without capturing.

The agent will then analyze the image and print the content suggestions to the console.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.
