import face_recognition
from PIL import Image
import base64
from django.core.files.base import ContentFile
import uuid
import imghdr
import io,os
from datetime import datetime
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
import os
import numpy as np
from tensorflow.keras.models import model_from_json
import xlsxwriter
from django.contrib.auth.models import User
def compare_two_face(existing_file, received_file):

    existing_img = face_recognition.load_image_file(existing_file)
    img_received = face_recognition.load_image_file(received_file)
    img_received_facial = face_recognition.face_encodings(img_received)[0]
    existing_img_facial = face_recognition.face_encodings(existing_img)[0]
    results = face_recognition.compare_faces([img_received_facial],existing_img_facial)
    if(results[0]):
        print(results[0])
        return 1
    else:
        return 0

def get_file_extension(file_name,decoded_file):
    extension = imghdr.what(file_name,decoded_file)
    extension = "jpg" if extension=="jpeg" else extension
    return extension 

def decodeDesignImage(image_data, folder, user_name):
    
    current_time = datetime.now().timestamp()
    new_im_path = os.path.join(folder,str(user_name)+str(current_time)+'.png')
    
    if 'data:' in image_data and ';base64,' in image_data:
                _,data = image_data.split(';base64,')
    try:
        data = base64.b64decode(data)
        buf = io.BytesIO(data)
        img = Image.open(buf)
        img.save(new_im_path, 'PNG')
    except:
        print("INVALID")
    file_name = str(uuid.uuid4())[:12]
    file_extension = get_file_extension(file_name,data)
    complete_file_name = "%s.%s" % (file_name,file_extension,)
    return ContentFile(data,name=complete_file_name), new_im_path
    

def check_spoof(file_path):
    root_dir = os.getcwd()
    # Load Face Detection Model
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # Load Anti-Spoofing Model graph
    json_file = open('antispoofing_models\\antispoofing_model.json','r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load antispoofing model weights 
    model.load_weights('antispoofing_models/antispoofing_model.h5')
    print("Model loaded from disk")
    frame = cv2.imread(file_path)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:  
        face = frame[y-5:y+h+5,x-5:x+w+5]
        resized_face = cv2.resize(face,(160,160))
        resized_face = resized_face.astype("float") / 255.0
        # resized_face = img_to_array(resized_face)
        resized_face = np.expand_dims(resized_face, axis=0)
        # pass the face ROI through the trained liveness detector
        # model to determine if the face is "real" or "fake"
        preds = model.predict(resized_face)[0]
        print(preds)
        if preds> 0.5:
            label = False
            
        else:
            label = True
    return label   
def give_excel(day,month,attendance):
    j=0
    set_item=set()
    print(j)
    workbook = xlsxwriter.Workbook('attendance_all.xlsx')
    
            # The workbook object is then used to add new
            # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    
    print(len(attendance))
    for i in range(0,len(attendance)):
        
        day_t = str(attendance[0][1].date())[8:]
        month_t = str(attendance[0][1].date())[5:-3]
        
      
        if day==day_t and month==month_t:
            print("entered")
            
            elem=User.objects.get(id=attendance[i][3]).username
            print(set_item)
            if elem in set_item:
                print("cont")
                continue
            else:
                cell1 = 'A'+str(j+1)
                j+=1
                worksheet.write(cell1, User.objects.get(id=attendance[i][3]).username)
                set_item.add(elem)
            
    workbook.close()