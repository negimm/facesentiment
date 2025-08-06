import cv2
import os
import tempfile

def capture_face_image() -> str | None:
    """
    Opens a webcam feed. When the user presses 'c', it captures the frame
    and saves it as a temporary JPG file.

    Returns:
        The path to the saved temporary image file, or None if the user quits.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return None

    saved_filepath = None
    try:
        print("\n--- Webcam Active ---")
        print("Position your face and press 'c' to capture.")
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
                # Create a temporary file to save the image
                with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmpfile:
                    saved_filepath = tmpfile.name
                    print(f"\nCapturing image and saving to {saved_filepath}...")
                    cv2.imwrite(saved_filepath, frame)
                    print("Image saved.")
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return saved_filepath