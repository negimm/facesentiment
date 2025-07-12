# Face Sentiment Analysis Agent

This project is an AI-driven agent that analyzes a person's facial expression from an image to determine their emotion. Based on the detected emotion, it then searches the web to suggest relevant and uplifting content, such as articles, videos, or activities.

## Features

-   **Webcam Capture**: Easily capture an image of your face using your webcam.
-   **File-Based Analysis**: Provide a path to an existing image file for analysis via a command-line interface.
-   **Advanced Emotion Detection**: Utilizes Google's Gemini 1.5 Pro vision model for accurate and nuanced facial expression analysis.
-   **Intelligent Content Suggestions**: Employs a LangChain agent with Tavily Search to find personalized content based on your mood.
-   **Modern Python Tooling**: Built with Poetry for robust dependency management.

## Prerequisites

-   Python (version 3.9 to 3.12)
-   [Poetry](https://python-poetry.org/docs/#installation) for dependency management.
-   A **Google Gemini API Key**. You can get one from [Google AI Studio](https://aistudio.google.com/app/apikey).
-   A **Tavily API Key**. You can sign up for one on the [Tavily website](https://tavily.com/).

## Installation

Follow these steps to set up the project on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd facesentiment
    ```

2.  **Install dependencies using Poetry:**
    This command will create a virtual environment and install all the necessary packages listed in `pyproject.toml`.
    ```bash
    poetry install
    ```

3.  **Set up environment variables:**
    Create a file named `.env` in the root of the project directory (`c:\AI\facesentiment\.env`) and add your API keys:
    ```
    GOOGLE_API_KEY="your_google_gemini_api_key_here"
    TAVILY_API_KEY="your_tavily_api_key_here"
    ```

## How to Run the Program

You can run the application in two ways. Make sure you are in the project's root directory.

### 1. Using the Webcam
To launch the application and use your webcam to capture an image:
```bash
poetry run python src/main.py
```
A window will open showing your webcam feed. Position your face and press the **'c'** key to capture the image and start the analysis.

### 2. Using an Existing Image File
To analyze an image you already have on your computer, use the `--image` (or `-i`) command-line argument:
```bash
poetry run python src/main.py --image "C:\path\to\your\image.jpg"
```
The agent will then analyze the provided image and print its content suggestions to the console.
