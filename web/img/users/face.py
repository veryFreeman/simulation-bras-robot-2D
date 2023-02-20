import face_recognition

# Load the two images
img1 = face_recognition.load_image_file("img1.jpg")
img2 = face_recognition.load_image_file("img2.jpg")

# Get the face encodings of the two images
encoding1 = face_recognition.face_encodings(img1)[0]
encoding2 = face_recognition.face_encodings(img2)[0]

# Compare the two face encodings
result = face_recognition.compare_faces([encoding1], encoding2)

# Print the result
if result[0]:
    print("The two faces match.")
else:
    print("The two faces do not match.")
