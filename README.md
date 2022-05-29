
![image](https://connectedremag.com/wp-content/uploads/2019/10/facial-recognition-connected-real-estate-768x687.png)
# Project-OCULUS
### `THEME : FACE RECOGNITION`

`Project-Oculus` Project Oculus is an Attendance tracking application to take individual as well as group attendance for any organization. Along with that it also provides emotion recognition from facial features as well as hand gesture recognition to create interactive surveys.

Contents
========

 * [Installation](#installation)
 * [Tech-Stacks Used](#Tech-Stacks-Used)
 * [Features Added](#Features-Added)
 * [Snapshots](#Snapshots)
 * [Demo](#Demo)
 


### Installation
---
1. Clone the repository
2. Open the Project Path where manage.py is present in python console. (ex-  C:\Users\jenaa\djangoproject\Project-Oculus)
3. Run `pip install -r requirements.txt`
4. Run `python manage.py makemigrations` then `python manage.py migrate`.
5. In python console type, `python manage.py runserver`
6. The website link should be displayed on the side. Copy it and paste in the web browser.

`.env file datas hasn't been pushed`
<br/>


### Tech-Stacks Used
---
<ol>
<li> Django Templating language
<li>Django Rest Framework 
<br/>
<li>SQLite3
<br/>
<li>Jinja2
<br/>
<li>tensorflow
<br/>
<li>OpenCV
<br/>
<li>Bootstrap CSS
<br/>
</ol>

### Features Added
---
<ol>
    
<li>Create Profile: User has to create a profile by adding a picture of his/her face.
</li></br>
<li>Take individual attendance: User can login and give attendance by verifying his face . Spoof or fake photos are identified by livliness detection and hence not accepted only faces of real human are verified.</li></br>
<li>Group attendance : By uploading a picture of a group , the model recognises all people present in the photo and provides a downloadable excel sheet.
</li></br>
<li>Gesture identification : Gesture identification predicts number of extended fingers by taking hand image as input hence can predict any numeral shown via gesture.</li></br>
<li>Facial emotion recognition : 7 class of emotions are recognized along with their confidence scores by the model as -
 angry,disgust,fear,happy,neutral,sad,surprise
</li></br>
<li>Downloadable : All the attendance taken can be downloaded on basis of date as an excel sheet
</li></br>

</ol>

### Snapshots
---
Some of the snapshots of website.
</br>
![Screenshot (321)](https://user-images.githubusercontent.com/79363736/154756737-5dd6ab6e-48ad-4813-a2d3-5098633a9e81.png)<br/> - Landing Page

![Screenshot (327)](https://user-images.githubusercontent.com/79363736/154758030-8814c915-dd88-4594-9d85-17fe82bf457c.png) <br/> - DashBoard with POEM Score and weather dependency

![Screenshot (328)](https://user-images.githubusercontent.com/79363736/154758229-6f1695f4-2bf6-4633-b2e3-0fb60b02cae7.png) <br/> - POEM questionnaire

![Screenshot (330)](https://user-images.githubusercontent.com/79363736/154758868-cc821375-191f-4aaf-a890-ff99e316d877.png) <br/> - Triggers List

![Screenshot (331)](https://user-images.githubusercontent.com/79363736/154758790-24ffca0a-b5b2-4a54-8843-ea3a64e6a2a4.png) <br/> - Insights

![Screenshot (332)](https://user-images.githubusercontent.com/79363736/154758683-d57a0185-1486-4ba1-bc0e-b046abc9cc35.png) <br/> - EczeImage Analysis

![Screenshot (334)](https://user-images.githubusercontent.com/79363736/154759244-744f93ba-e19b-4afa-8fd9-7cb07c7d2502.png) <br/> - Doctor's portal 

![Screenshot (335)](https://user-images.githubusercontent.com/79363736/154759379-69d3eece-74e2-4f5c-8968-a685fc37acf7.png) <br/> - Appointment confirmation

