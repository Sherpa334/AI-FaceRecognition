import cv2
from facedetect import FaceRecognition
from alert_system import AlertSystem

def main():
    face_recognizer = FaceRecognition()
    alert_system = AlertSystem()
    
    video = cv2.VideoCapture(0)
    print("Starting video stream... Press 'q' to exit.")

    while True:
        ret, frame = video.read()
        if not ret:
            break
        matches = face_recognizer.recognize_face(frame)
        for name, (top, right, bottom, left) in matches:
            alert_system.send_alert(name)
            color = (0, 0, 255) if name == "Unfamiliar" else (0, 255, 0)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()