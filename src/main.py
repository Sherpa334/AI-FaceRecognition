import cv2
from facedetect import FaceRecognition
from alert_system import AlertSystem
import sys
import os
from pathlib import Path

def main():
    face_recognizer = FaceRecognition()
    alert_system = AlertSystem()
    
    video = cv2.VideoCapture(0)
    print("Starting video stream... Press 'q' to exit.")

    # get path to training data from root folder
    root_dir = Path(__file__).parent.parent
    path_to_training_data_from_root = os.path.join(root_dir, "known_faces", "training_data")

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
        
        # image count for a folder. Used to name new files.
        img_count = 0
        
        # get key input
        key = cv2.waitKey(0)%256
        if key == ord('q'):
            break

        # take screenshot by pressing the 's' key
        elif key == ord('s'):

            # Get user name (just checks for 2 strings)
            name = input("Enter your name ['first last']:").split(' ')
            while len(name) != 2:
                name = input("Try again, format as ['first last']:").split(' ')
                
            first = name[0].title()
            last = name[1].title()
            dir = os.listdir(path_to_training_data_from_root)

            # This will hold the directory location and folder to add screenshot to
            new_dir = path_to_training_data_from_root

            # get folder to insert pictures
            new_folder_name = ''
            for folder in dir:
                # if folder exists use it
                if (folder == first + '_' + last): 
                    new_folder_name = folder

                    # add the folder to the file path
                    new_dir = os.path.join(new_dir, new_folder_name)

                    # count the number of files in the current directory if one exists
                    img_count = sum(len(files) for _, _, files in os.walk(new_dir))
                    break
             
            # if no folder was found make a new one
            if new_folder_name == '':
                new_folder_name = first + '_' + last

                # add new folder to the file path
                new_dir = os.path.join(path_to_training_data_from_root, new_folder_name)
                os.makedirs(new_dir)
                print("Folder created for new user.")

            # change to the proper directory and add new screenshot to it
            print(new_dir)
            os.chdir(new_dir)
            img_name = "frame{}.png".format(img_count)
            cv2.imwrite(img_name, frame)

            # set the directory back to the starting directory
            os.chdir(os.getcwd())
            print("Screenshot Taken")
            img_count += 1

        # restart the program so the new images are used.
        elif key == ord('r'): 
            print("Restarting...")
            video.release()
            cv2.destroyAllWindows()
            os.execl(sys.executable, sys.executable, *sys.argv)
            
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
