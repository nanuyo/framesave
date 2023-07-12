import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Set the number of frames to save
num_frames = 30
frame_count = 0

# Loop until the required number of frames are saved
while frame_count < num_frames:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Save the frame as an image
    file_name = f"frame{frame_count}.jpg"
    cv2.imwrite(file_name, frame)

    frame_count += 1

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()