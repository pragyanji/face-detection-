import cv2  # Import the OpenCV library
import pyaudio
import wave


class Personal_Assistance:
    def face_detection(self):
        # Initialize the video capture object, which captures video from the webcam (index 0)
        cap = cv2.VideoCapture(0)

        while True:  # Start an infinite loop
            ret, frame = cap.read()  # Capture a frame from the webcam

            # Display the frame in a window named 'Detecting Face'
            cv2.imshow('Detecting Face', frame)

            # If 'q' is pressed, break the loop
            if cv2.waitKey(1) == ord('q'):
                break
            
        # Release the video capture object and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()
    
obj1 = Personal_Assistance()

obj1.face_detection()