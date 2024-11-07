import face_recognition
import os
import numpy as np

# Directory containing images of known faces
KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6  # Match tolerance

class FaceRecognition:
    def __init__(self):
        self.known_faces = []
        self.known_names = []
        self.load_known_faces()

    def load_known_faces(self):
        for name in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir(f"{KNOWN_FACES_DIR}/{name}"):
                image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{name}/{filename}")
                encoding = face_recognition.face_encodings(image)[0]
                self.known_faces.append(encoding)
                self.known_names.append(name)

    def recognize_face(self, frame):
        locations = face_recognition.face_locations(frame)
        encodings = face_recognition.face_encodings(frame, locations)

        matches = []
        for face_encoding, face_location in zip(encodings, locations):
            results = face_recognition.compare_faces(self.known_faces, face_encoding, TOLERANCE)
            name = "Unfamiliar"
            if True in results:
                name = self.known_names[results.index(True)]
            matches.append((name, face_location))

        return matches