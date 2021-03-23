# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 11:22:57 2021

@author: jojo
"""

import school.courses.courses as courses
from school.queries.connection import *

#Parameters of connection
hostname="127.0.0.1"
dbname="school"
username="root"
pwd="user"

course = courses.Course(username, pwd)

course_attr=["Id", "teacherid", "title", "phone", "credit", "duration", "class", "year", "description"]
course_list=[('C107', "T200", "Machine learning", "237699663300", "15", "30", "Master1", "2021","donner la capcité au machine d'apprendre"),
              ('C108', "T220", "Reinforcement learning", "237688442200", "4", "20", "Master1", "2021","interagir avec un environement dans le but de maximiser la recompenses")]


courses.addCourse(course_attr, course_list)
#%%

from school.queries.connection import *
import school.students.students as students

#Parameters of connection
hostname="127.0.0.1"
dbname="school"
username="root"
pwd="user"

#Create an instance of Student class
student= students.Student(username,pwd)

#Create variables to store list of studentsto insert to the database
#
student_attr=["Id", "name", "email", "phone", "address", "uname", "pwd", "level", "grade"]
student_list=[('2A07', "Ali Moussa", "ali.moussa@xyz.com", "237699663300", "Soa, Yaoundé", "moussa", "Moussa2021", "Master",0.0),
              ('2A08', "Abakar", "abakar@xyz.com", "237688442200", "Bini, Ngaoundéré", "abakar", "Abakar2021", "Master",0.0)
              ('2A09', "mako", "mako@xyz.com", "237688842200", "ange raphael, Douala", "mako", "mako2021", "Master",0.0)
              ('2A10', "jodi", "jodi@xyz.com", "237688442400", "Bini, Ngaoundéré", "jodi", "jodi2021", "Master",0.0)
              ('2A11', "hamed", "hamed@xyz.com", "237698442200", "ange raphael, Douala", "hamed", "hamed2021", "Master",0.0)
              ('2A12', "mariaba", "mariaba@xyz.com", "237658442200", "ange raphael, Douala", "mariaba", "mariaba2021", "Master",0.0)
              ('2A13', "locko", "locko@xyz.com", "237688441200", "Bini, Ngaoundéré", "locko", "locko2021", "Master",0.0)
              ('2A14', "lottin", "lottin2@xyz.com", "237682442200", "Bini, Ngaoundéré", "lottin", "lottin2021", "Master",0.0)
              ('2A15', "feuzeu", "feuz@xyz.com", "237688440200", "Soa, Yaoundé", "feuzeu", "feuzeu2021", "Master",0.0)
              ('2A16', "ndoumbe", "joel@xyz.com", "237688442209", "Soa, Yaoundé", "ndoumbe", "ndoumbe2021", "Master",0.0)]

#Call the method addStudent
student.addStudent(student_attr, student_list)
#%%

import school.teachers.teachers as teachers
from school.queries.connection import *

#Parameters of connection
hostname="127.0.0.1"
dbname="school"
username="root"
pwd="user"

teacher = teachers.Teacher(username, pwd)

teacher_attr=["Id", "name", "email", "phone", "adress", "uname", "pwd"]
teacher_list=[('T007', "jean noumbe", "jean@xyz.com", "237699663300", "jean", "1230"),
              ('T008', "carlos konlack", "carl@xyz.com", "237688442200", "carlos", "15869")]


teachers.addTeachers(teacher_attr, teacher_list)
#%%
student_attr=["name", "address"]
student_cond="level='Master'"

#Call the method selectStudent
result=student.selectStudent(student_attr, student_cond)

#Customize the output
for item in result:
    print("The student ", item[0], "lives at ", item[1])
    
#%%

cnxServer.close()
#cnxDB.close()
