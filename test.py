import cv2

# Load the pre-trained model for facial detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Create a video capture object
cap = cv2.VideoCapture(0)

# Loop through video frames
while True:
    # Read a frame from the video capture object
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Face Detection", frame)

    # Exit the loop if the 'q
 