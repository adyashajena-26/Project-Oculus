import os
import face_recognition
def compare_two_face(existing_file, received_file):
    existing_img = face_recognition.load_image_file(existing_file)
    img_received = face_recognition.load_image_file(received_file)
    
    img_received_facial = face_recognition.face_encodings(img_received)[0]
    existing_img_facial = face_recognition.face_encodings(existing_img)[0]
    results = face_recognition.compare_faces([img_received_facial],existing_img_facial)
    if(results[0]):
        return 1
    else:
        return 0
dict = {}
for filename in os.listdir("known_faces/"):
        dict[filename]=0
for file in os.listdir("found_faces/"):
    got_im_path = os.path.join("found_faces/",file)
    for filename in os.listdir("known_faces/"):
        
        exist_image =  os.path.join("known_faces/",filename)
        if(compare_two_face(exist_image,got_im_path)==1):
            dict[filename]=1
            break
    

print (dict)
