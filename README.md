# php-to-pyhton
PHP to python project for OreFox


Carry out environmental testing and installation of necessary components---4/19/2021


Complete the server and client on the python side---4/22/2021

test on load---
Requirements
For Database management system 
Python ==3.8
$ pip install Django 
$ pip install pymysql 

For Prediction model (YOLOv5)
$ pip install -r requirements.txt


Tutorials
The entire database management system is implemented through the background management of the Django framework:

$ cd SQLmange
$ python manage.py runserver

Run the server, add /admin after the domain name
Username : zoe
Password: 123456
1.	Can add, delete, modify and check existing databases
2.	You can manage user rights in the background. Increase access rights
 
You can also associate the new database and table in DBope through Django.model
For details, please see:
https://docs.djangoproject.com/en/3.2/topics/db/models/
