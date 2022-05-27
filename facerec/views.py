import csv
import os
from unicodedata import name
from urllib import request
import cv2
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import PasswordChangeForm
from PIL import Image 
import numpy as np
from datetime import datetime


def index(request):
    return render(request,"index.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['pass1']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')


def register(request):

    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'username already exists! Try with another username')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.success(request,'Email already exists! Try with another email')
                return redirect('register')
            else:
                myuser = User.objects.create_user(username=username, password=pass1, email=email)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                messages.success(request, "Your account has been registered successfully! Please login to continue.")
                return redirect('login')

        else:
             messages.success(request,'Password not matching :(')
        return redirect('register')
    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def dashboard(request):
    return render(request,"dashboard.html")

def about(request):
    return render(request,"about.html")

def createdata(request):
    return render(request,"createdata.html")

def train(request):
    return render(request,"train.html")

def takeattendance(request):
    return render(request,"takeattendance.html")

def authenticateuser(request):
    return render(request,"authenticateuser.html")



#generating dataset of user by taking his information and a set of images for the training purpose
def generate_dataset(request):

    if request.method == "POST":
        face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    def face_cropped(img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        # scaling factor = 1.3
        # minimum neighbor = 5
        
        if faces is ():
            return None
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h,x:x+w]
        return cropped_face
    
    cap = cv2.VideoCapture(0)

    name = request.POST['name']
    id = request.POST['uniqueid']
    branch = request.POST['branch']
    emailidstudent = request.POST['emailidstudent']
    contact = request.POST['contact']
    address = request.POST['address']


    #facedata = User.objects.create_user(name=name, id=id, branch=branch, emailidstudent=emailidstudent, contact=contact, address=address)
    #facedata.save()


    img_id=0
    while True:
        ret, frame = cap.read()
        if face_cropped(frame) is not None:
            img_id+=1
            face = cv2.resize(face_cropped(frame), (200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
            cv2.imwrite(file_name_path, face)
            cv2.putText(face, str(img_id), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            
            cv2.imshow("Cropped face", face)
            
        if cv2.waitKey(1)==13 or int(img_id)==100: #here 13 is, ASCII character for Enter.
            break
            
    cap.release()
    cv2.destroyAllWindows()

    #saving the user data to excel sheet.
    row = [id, name, branch, emailidstudent, contact, address]
    with open('StudentDetails/StudentDetails.csv','a+') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(row)
    csvFile.close()
    messages.success(request, "Data collected successfully !!.")
    return redirect('dashboard')
    


def train_classifier(request):
    #change the data_dir path according to your data folder path !!
    data_dir = r"C:/Users/91816/Desktop/project/microsoftproj/face/data"   #including the path where the face datas are saved
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    
    faces = []
    ids = []
    
    for image in path:
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split(".")[1])
        
        faces.append(imageNp)
        ids.append(id)
        
    ids = np.array(ids)
    
    # Train and save classifier
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    messages.success(request, "Data trained successfully !!.")
    return redirect('dashboard')


def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors,text)
    
    for (x,y,w,h) in features:
        cv2.rectangle(img, (x,y), (x+w,y+h), color, 2 )
        
        id, pred = clf.predict(gray_img[y:y+h,x:x+w])
        confidence = int(100*(1-pred/300))
        
        if confidence>70:
            if id==1:
                cv2.putText(img, "ANIKET", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                
            elif id==2:
                cv2.putText(img, "BILLGATES", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
            
            elif id==3:
                cv2.putText(img, "SHLOK", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)

           #add uder data here [give id(same id provided while creating data) and name] 
           # elif id==2:
                #cv2.putText(img, "BILLGATES", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)

        else:
            cv2.putText(img, "UNKNOWN", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
    
        return img

    # loading classifier
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, img = video_capture.read()
        img = draw_boundary(img, faceCascade, 1.3, 6, (255,255,255), "face", clf)
        cv2.imshow("face Detection", img)
        if cv2.waitKey(1)==13:
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return render(request,'markattendance.html') 



def detect_face(request):
    def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
        
        for (x,y,w,h) in features:
            cv2.rectangle(img, (x,y), (x+w,y+h), color, 2 )
            
            id, pred = clf.predict(gray_img[y:y+h,x:x+w])
            confidence = int(100*(1-pred/300))
            
            if confidence>70:
                if id==1:
                    cv2.putText(img, "ANIKET", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                    
                elif id==2:
                    cv2.putText(img, "BILLGATES", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
                
            else:
                cv2.putText(img, "UNKNOWN", (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 1, cv2.LINE_AA)
        
            return img

    # loading classifier
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("classifier.xml")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, img = video_capture.read()
        img = draw_boundary(img, faceCascade, 1.3, 6, (255,255,255), "face", clf)
        cv2.imshow("face Detection", img)
        if cv2.waitKey(1)==13:
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return render(request,'markattendance.html')



#attendance marked
def markattendance(request):
    if request.method == "POST":
        studentname = request.POST['studentname']

        time_now = datetime.now()
        tStr = time_now.strftime('%H:%M:%S')
        dStr = time_now.strftime('%d/%m/%Y')
        
        row = [studentname, tStr, dStr]
        with open('Markattendance/attendance.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        messages.success(request, "authenticated successfully.")
        return redirect('takeattendance')







#password reset for user
def changepass(request):
    fm = PasswordChangeForm(user=request.user)
    return render(request,"changepass.html", {'form':fm})

