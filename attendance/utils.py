import face_recognition
from PIL import Image
import base64
from django.core.files.base import ContentFile
import uuid
import imghdr
import io

def compare_two_face(existing_file, received_file):
    existing_img = face_recognition.load_image_file(existing_file)
    img_received = face_recognition.load_image_file(received_file)
    print(face_recognition.face_encodings(img_received))
    img_received_facial = face_recognition.face_encodings(img_received)[0]
    existing_img_facial = face_recognition.face_encodings(existing_img)[0]
    results = face_recognition.compare_faces([img_received_facial],existing_img_facial)
    if(results[0]):
        return 1
    else:
        return 0

def get_file_extension(file_name,decoded_file):
    extension = imghdr.what(file_name,decoded_file)
    extension = "jpg" if extension=="jpeg" else extension
    return extension 

def decodeDesignImage(data):
    try:
        data = base64.b64decode(data)
        buf = io.BytesIO(data)
        img = Image.open(buf)
        img.save('image.png', 'PNG')
    except:
        print("INVALID")
    file_name = str(uuid.uuid4())[:12]
    file_extension = get_file_extension(file_name,data)
    complete_file_name = "%s.%s" % (file_name,file_extension,)
    return ContentFile(data,name=complete_file_name)
    