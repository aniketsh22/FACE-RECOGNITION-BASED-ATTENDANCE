# FACE-RECOGNITION-BASED-ATTENDANCE
![Logo](https://user-images.githubusercontent.com/89505839/170663229-51279416-3a26-4387-94e1-a87e6386582e.png)

TRACKO A browser based face recognition attendance system. Made this project for the Microsoft engage '22.

- Detect's face accurately within a second.

- User friendly and easily accessible.

- Easy for the user to understand the whole sytem.

- A system made for detecting human face and particularly for attendance.

# Microsoft ENGAGE 2022

Problem statement: 

Develop a browser-based application or a native mobile application to demonstrate application of Face Recognition technology.
You could choose to demonstrate application of Face Recognition in any area of application of your choice.

## VIDEO :

https://user-images.githubusercontent.com/89505839/170777929-5af0d5fd-6de5-4377-bcc4-1000bf9606f9.mp4


## Tech Stack

**FRONTEND:** 

• HTML

• CSS

• BOOTSTRAP


**BACKEND:** 

• DJANGO ( web development framework )

• PYTHON ( backend programming language )

• OpenCV ( Computer Vision Library )


## INSTALLATION

Required packages and libraries

The Code is written in Python. If you don't have Python installed you can find it [HERE](https://www.python.org/downloads/)

Before installing required packages and libraries make sure you have installed visual studio code community version. After that make sure you select Desktop development with C++ and install it. --> [For dlib library you must first download c++ visual studio version, then only dlib get's installed properly]
<img width="960" alt="vscodess" src="https://user-images.githubusercontent.com/89505839/170658528-ee5aa11a-5494-4bdc-b86c-88a672d5aba9.png">


```bash
  pip install cmake
  pip install dlib
  pip install face-recognition
  pip install numpy
  pip install opencv-python
  pip install Pillow
```

## TO CLONE THE PROJECT

```bash
  git clone https://github.com/aniketsh22/FACE-RECOGNITION-BASED-ATTENDANCE.git
```

## TO RUN LOCALLY

After cloning make sure that all the libraries are installed properly and correctly. For running the cloned project go to the project folder where the manage.py file is located and then run the following commands into the command prompt:

**First making migrations:** 
```bash
  python manage.py makemigrations
  python manage.py migrate
```

**Creating superuser for accessing the database:** 

After running the following command, create one superuser by adding username, password
```bash
  python manage.py createsuperuser
```

**Running the project on the local host:** 
```bash
  python manage.py runserver
```

## FOR ACCESSING ADMIN PANEL
```bash
  http://127.0.0.1:8000/admin
```
<img width="602" alt="adminss" src="https://user-images.githubusercontent.com/89505839/170661481-e2f526b2-fc85-405f-b39d-7f894d2d609e.png">

Enter username and paswword, which you have made while creating superuser. To get access to the database.

<img width="813" alt="adminss2" src="https://user-images.githubusercontent.com/89505839/170661830-5d4d1b00-7427-4e33-8ac9-62ffc7e46e5e.png">

## NOTE:

If css is giving error even if properly linked (Go to chrome > settings > clear cache)

<img width="959" alt="cleardatass" src="https://user-images.githubusercontent.com/89505839/170664313-81deb74f-0ff2-4e48-883c-b18e1babfafe.png">



# SCREENSHOTS OF THE APPLICATION

Index page:
<img width="960" alt="indexpagess" src="https://user-images.githubusercontent.com/89505839/170774148-29e51bde-3add-4a9b-ba74-54bc24962cd1.png">

About Page:
<img width="960" alt="aboutss" src="https://user-images.githubusercontent.com/89505839/170774200-e0ea77ee-1041-4bf1-897a-4caef5f648a2.png">

After Loggedin:
<img width="960" alt="afterloginss" src="https://user-images.githubusercontent.com/89505839/170774289-b927070f-9ce1-4622-8fb9-b55f39d9dcba.png">

Dashboard:
<img width="960" alt="dashboardss" src="https://user-images.githubusercontent.com/89505839/170774330-32e5efff-3e5a-4a88-8170-abebc4262809.png">

Training dataset:
<img width="960" alt="trainss" src="https://user-images.githubusercontent.com/89505839/170774395-0e3b0476-dc4b-475e-ac4f-2008d2887c33.png">

Take attendance:
<img width="960" alt="attendancess" src="https://user-images.githubusercontent.com/89505839/170774562-a588a832-e640-45cc-9842-67256071a87f.png">

After face detected:
<img width="959" alt="markedss" src="https://user-images.githubusercontent.com/89505839/170774486-917f8c75-8bb6-4c56-bb5d-98d51cc3fe9f.png">

## Feedback

If you have any feedback, please reach out to us at shrungareaniket05@gmail.com


## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aniket-shrungare-834a39237/)
