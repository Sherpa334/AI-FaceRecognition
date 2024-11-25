import face_recognition
import os
import numpy as np
from pathlib import Path

# Directory containing images of known faces
ROOT_DIR = Path(__file__).parent.parent
KNOWN_FACES_DIR = os.path.join(ROOT_DIR, "known_faces", "training_data")
TOLERANCE = 0.6  # Match tolerance

class FaceRecognition:
    def __init__(self):
        self.known_faces = []
        self.known_names = []
        self.load_known_faces()

    def load_known_faces(self):
        for person_name in os.listdir(KNOWN_FACES_DIR):
            person_folder = os.path.join(KNOWN_FACES_DIR, person_name)
            if os.path.isdir(person_folder):
                # Loop through each image file in the person's folder
                for filename in os.listdir(person_folder):
                    image_path = os.path.join(person_folder, filename)
                    image = face_recognition.load_image_file(image_path)
                    
                    # Generate face encodings for the image
                    encodings = face_recognition.face_encodings(image)
                    if encodings:  # Proceed if an encoding is found
                        self.known_faces.append(encodings[0])  # Append the encoding
                        self.known_names.append(person_name)   # Associate with person's name

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