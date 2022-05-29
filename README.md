
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




