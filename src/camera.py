import cv2
import os

def capture_face_image(filename: str = "captured_face.jpg") -> str | None:
    """
    Opens a webcam feed. When the user presses 'c', it captures the frame,
    and saves it as a JPG file in the current working directory.

    Args:
        filename: The name of the file to save the image as.

    Returns:
        The absolute path to the saved image, or None if the user quits.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    saved_filename = None
    try:
        print("\n--- Webcam Active ---")
        print(f"Position your face and press 'c' to capture. Image will be saved as {filename}")
        print("Press 'q' to quit.")

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame from webcam.")
                break

            cv2.imshow('Webcam - Press "c" to capture, "q" to quit', frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                print("Exiting webcam.")
                break
            elif key == ord('c'):
                print(f"\nCapturing image and saving to {filename}...")
                cv2.imwrite(filename, frame)
                print("Image saved.")
                saved_filename = os.path.abspath(filename)
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return saved_filename