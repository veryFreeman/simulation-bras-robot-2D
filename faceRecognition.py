import face_recognition
import numpy as np
import cv2
import os


def recognition():
    cam = cv2.VideoCapture(0)
    # cam.set(5,1)
    known_face_encodings = []
    known_faces_filenames = []

    for (dirpath, dirnames, filenames) in os.walk('web/asset/img/users/'):
        known_faces_filenames.extend(filenames)
        break
    for filename in known_faces_filenames:
        face = face_recognition.load_image_file('web/asset/img/users/' + filename)
        known_face_encodings.append(face_recognition.face_encodings(face)[0])
    face_locations = []
    face_encodings = []

    while True:
        _ , frame = cam.read()
        if _ :  
            face_locations = face_recognition.face_locations(frame)
            face_encodings = face_recognition.face_encodings(frame, face_locations)
            for face_encoding in face_encodings: 
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    cam.release()
                    del(cam)
                    return 1

            # cv2.imshow('Video', frame)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #  break


cv2.destroyAllWindows()