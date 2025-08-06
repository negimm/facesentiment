import os
import argparse
from camera import capture_face_image
from agent import create_emotion_agent, get_content_suggestions

def run_application(image_path_arg: str | None):
    """
    Main function to run the face sentiment agent.
    1. Gets an image path (either from webcam or command line argument).
    2. Gets content suggestions based on the analyzed emotion from the image.
    3. Cleans up temporary files.
    """
    image_path = image_path_arg
    is_temp_file = False

    try:
        # Step 1: Get an image path. If none is provided, use the webcam.
        if not image_path:
            print("No image path provided via arguments, starting webcam...")
            image_path = capture_face_image()
            if image_path:
                is_temp_file = True  # Mark that this is a temporary file

        if not image_path:
            print("No image was captured. Exiting.")
            return

        # Verify that the final image path exists before proceeding.
        if not os.path.exists(image_path):
            print(f"Error: The image file was not found at the specified path: {image_path}")
            return

        # Step 2: Check for API keys
        if not os.getenv("GOOGLE_API_KEY") or not os.getenv("TAVILY_API_KEY"):
            print("Error: Required API key (GOOGLE_API_KEY or TAVILY_API_KEY) is not set.")
            print("Please create a .env file and add your API keys.")
            return

        # Step 3: Create agent and get content suggestions
        agent_executor = create_emotion_agent()
        get_content_suggestions(image_path, agent_executor)

    finally:
        # Step 4: Clean up the temporary file if one was created
        if is_temp_file and image_path and os.path.exists(image_path):
            print(f"Cleaning up temporary file: {image_path}")
            os.remove(image_path)

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