# CSE-368-Project

**Motivation/Introduction**

In the interest of public safety and the limitations in human monitoring capabilities, the integration of artificial intelligence in facial recognition technology could allow for the automatic detection of unfamiliar faces in real-time, thereby enhancing situational awareness and security of particularly vulnerable areas such as hospitals, nursing homes, schools, etc.

AI can visualize data at a speed that humans are not capable of, enabling timely alerts to authorities when unfamiliar or potentially dangerous individuals are detected. This project aims to develop facial recognition software that identifies unfamiliar faces in designated areas, and if so, then notifies the appropriate authorities, thus fostering a safer environment.

**MacOS Installation instruction**
```console
brew install cmake
pip install dlib
pip install -r requirements.txt
```
The steps afterward will follow the same format as other operating systems. 

**Use/Installation**
After downloading folder to computer you can navigate to it in the terminal, prompt of your choice. If Python is installed on your system enter:
```console
foo@bar:~$ pip install -r requirements.txt
foo
```
If you get an error when intalling dlib, then you can download the pre compiled binary from here: [https://github.com/z-mahmud22/Dlib_Windows_Python3.x] Simply follow the instructions on the page for your python version.

To run the program after installing the requirements navigate to the src folder and run:
```console
foo@bar:~$ python main.py
foo
```
If any errors about not finding the training data pops up then open the file facedetect.py and change the KNOWN_FACES_DIR location to point at the 'AI-FaceRecognition-dev\known_faces\training_data' folder. You may need to rewrite as '../known_faces/training_data' depending on your operating system or how your choosing to run the program.
