import cv2
from collections import deque

# Set the desired resolution
width, height = 1920, 1080

# Open the default webcam with the desired resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

# Set the number of frames to save
num_frames = 30

# Create a circular buffer to store frames
buffer_size = num_frames + 1
buffer = deque(maxlen=buffer_size)

# Loop to continuously save frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Add the frame to the buffer
    buffer.append(frame)

    # Display the current frame
    #cv2.imshow('Frame', frame)

    # Check if enough frames are saved
    if len(buffer) == buffer_size:
        # Save the frames from the buffer
        for i, saved_frame in enumerate(buffer):
            file_name = f"frame{i+1}.jpg"
            cv2.imwrite(file_name, saved_frame)
        # Clear the buffer
        buffer.clear()
    # Break the loop if 'q' is pressed
#    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
