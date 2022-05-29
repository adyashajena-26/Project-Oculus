import imghdr
from django.core.files.base import ContentFile
import base64
from PIL import Image
import io, uuid
import mediapipe as mp
import cv2, math, os
from datetime import datetime
from attendance.utils import compare_two_face
import xlsxwriter
 


def getFacesFromGroup(image_path,user_name):
    
    mp_face_detection = mp.solutions.face_detection
    
    IMAGE_FILES = [image_path]
    with mp_face_detection.FaceDetection(

        model_selection=1, min_detection_confidence=0.5) as face_detection:
        for idx, file in enumerate(IMAGE_FILES):

    
            image = cv2.imread(file)
            # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
            results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

            # Draw face detections of each face.
            if not results.detections:

                continue
            annotated_image = image.copy()
            i=0
            
                
            for detection in results.detections:
               
                x = detection.location_data.relative_bounding_box.xmin
                y = detection.location_data.relative_bounding_box.ymin
                w = detection.location_data.relative_bounding_box.width
                h = detection.location_data.relative_bounding_box.height
                x_p = min(math.floor(x * annotated_image.shape[1]), annotated_image.shape[1] -1)
                y_p = min(math.floor(y * annotated_image.shape[0]), annotated_image.shape[1] -1)
                w_p = min(math.floor(w * annotated_image.shape[1]), annotated_image.shape[1] -1)
                h_p = min(math.floor(h * annotated_image.shape[0]), annotated_image.shape[1] -1)
                path_file =os.path.join("found_faces",str(user_name)+str(datetime.now().timestamp())+str(i)+".jpg") 
                i+=1
                
                cropped_image = annotated_image[y_p:y_p+h_p,x_p:x_p+w_p]
                cv2.imwrite(path_file,cropped_image)
                cv2.waitKey(1)
    

        return 0


def IdentifyFromGroup(found_faces_path , user):

    attendance_dict = {}
    present = []
    absent = []
    for emp in user:
        #key = list(emp.empprofile_set.all())[0].user
        key =  emp.username
        attendance_dict[key] = 0
          
    for filename in os.listdir("found_faces/"):
        got_img_path = os.path.join("found_faces/",filename)
        for emp in user:
            emp_profile = list(emp.empprofile_set.all())
            if len(emp_profile)>0:
                existing_image = emp_profile[0].profile_image.url[1:]
                print("path",existing_image)
        
            
            
                if(compare_two_face(existing_image,got_img_path)==1):
                    attendance_dict[emp.username]=1
                    break
    return attendance_dict

def produce_excel(present,absent):
    
    # Workbook() takes one, non-optional, argument
    # which is the filename that we want to create.
    workbook = xlsxwriter.Workbook('attendance.xlsx')
    
    # The workbook object is then used to add new
    # worksheet via the add_worksheet() method.
    worksheet = workbook.add_worksheet()
    
    
    # Use the worksheet object to write
    # data via the write() method.
    print(len(present))
    for i in range(1,len(present)+1):
        print("hi")
        cell1 = 'A'+str(i)
        cell2 = 'B'+str(i)
        print(cell1,cell2)
        worksheet.write(cell1, present[i-1].username)
        worksheet.write(cell2, 'PRESENT')
    for i in range(1,len(absent)+1):
        cell1 = 'A'+str(i+len(present))
        cell2 = 'B'+str(i+len(present))
        worksheet.write(cell1, absent[i-1].username)
        worksheet.write(cell2, 'ABSENT')
   
    
    # Finally, close the Excel file
    # via the close() method.
    workbook.close()

