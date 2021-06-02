# php-to-pyhton
PHP to python project for OreFox
Development Process
Carry out environmental testing and installation of necessary components---4/19/2021 \n
Complete the server and client on the python side---4/22/2021 \n
test on load---
Complete the sDatabase management on the python side---5/22/2021
Complete the Predction model build up ---5/22/2021
Complete the test of predction model using mineral image ---1/6/2021
Complete the Database management visualization ---1/6/2021



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
![image](https://user-images.githubusercontent.com/64721544/120441963-b64f1680-c3b7-11eb-8118-8f13e18da9e0.png)

Run the server, add /admin after the domain name
Username : zoe
Password: 123456
1.	Can add, delete, modify and check existing databases
2.	You can manage user rights in the background. Increase access rights
 
You can also associate the new database and table in DBope through Django.model
For details, please see:
https://docs.djangoproject.com/en/3.2/topics/db/models/


For show the results of the Prediction model:
Under root
$ test.py --data data/mineral.yaml --weights best.pt
