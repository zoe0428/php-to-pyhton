# php-to-pyhton
PHP to python project for OreFo
Development Process
Carry out environmental testing and installation of necessary components---4/19/2021 

Complete the server and client on the python side---4/22/2021 

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


1. You need to fill in the permissions of the database you need to modify in setting.py in SQLmange.
2. Then generate the corresponding Class in the model
3. Register the classes in the database in DBope's admin.py!
![9c29229ce5c65c0c972028f2b70dd43](https://user-images.githubusercontent.com/64721544/120452928-2adc8200-c3c5-11eb-85cd-c0c96fdefab8.png)




$ cd SQLmange
$ python manage.py runserver


Run the server, add /admin after the domain name
Username : zoe
Password: 123456
1.	Can add, delete, modify and check existing databases
2.	You can manage user rights in the background. Increase access rights
![image](https://user-images.githubusercontent.com/64721544/120441963-b64f1680-c3b7-11eb-8118-8f13e18da9e0.png)
 
You can also associate the new database and table in DBope through Django.model
For details, please see:
https://docs.djangoproject.com/en/3.2/topics/db/models/


For show the results of the Prediction model:
Under root
$ test.py --data data/mineral.yaml --weights best.pt
