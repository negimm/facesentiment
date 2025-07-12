import os
import argparse
from camera import capture_face_image
from agent import create_emotion_agent, get_content_suggestions

def run_application(image_path: str | None):
    """
    Main function to run the face sentiment agent.
    1. Gets an image path (either from webcam or command line).
    2. Gets content suggestions based on the analyzed emotion from the image.
    """
    # Step 1: Get an image path. If none is provided via arguments, use the webcam.
    if not image_path:
        print("No image path provided via arguments, starting webcam...")
        image_path = capture_face_image("captured_face.jpg")

    if not image_path:
        print("No image was captured. Exiting.")
        return

    # Verify that the final image path exists before proceeding.
    if not os.path.exists(image_path):
        print(f"Error: The image file was not found at the specified path: {image_path}")
        return

    # Step 2: Check for API key
    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.")
        print("Please create a .env file and add your Gemini API key.")
        return

    # Step 3: Create agent and get content suggestions
    agent_executor = create_emotion_agent(google_api_key)
    get_content_suggestions(image_path, agent_executor)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Face Sentiment Analysis Agent. Analyzes an image of a face and suggests content."
    )
    parser.add_argument(
        "-i", "--image",
        type=str,
        help="Path to an image file to analyze. If not provided, the webcam will be used."
    )
    args = parser.parse_args()
    run_application(args.image)