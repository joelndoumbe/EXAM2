#We implement a few functions of courses module
#First we import connection and query from queries module
from school.queries.connection import *
from school.queries.query import *
import mysql.connector

class Course:
    def __init__(self, *args):
        #conxDB: instance of connection to the database
        self.username=args[0]
        self.pwd=args[1]
        self.conxDB=self.getConnection(self.username, self.pwd)
        
    def getConnection(self, username,passwd):
        return connectServer("127.0.0.1", username, passwd, 10)


    #Create a function to add items to table student
    def addCourse(self, attributes, values):
        #attributes: list of attributes name of student table
        #values: list of tuples (value1, value2,..., valueN)
        #        each value is an information about the student profile
        
        cursor=self.conxDB.cursor()
        tb_query=inserttoTable("course", attributes, values)

        try:
            cursor.execute("USE school")
        except mysql.connector.Error as Er:
            print("Something is wrong with this data! Please check=> ", Er)
            exit(1)
        
        try:
            cursor.executemany(tb_query, values)
        except mysql.connector.Error as Er:
            print("Can't insert element into table! Please check what's wrong=> ", Er)
        else:
            self.conxDB.commit()
        cursor.close()
    
    #Create a function selectStudent to search and find student within a MySQL table
    def selectCourse(self, requestedAttr, condition):
        #requestedAttr: list of attributes (string data type)
        #condition: condition on which rows of tables are selected
        #           attribute= or > value        
        
        cursor=self.conxDB.cursor()
        tb_query=select("course", requestedAttr, condition)
        
        try:
            cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Something is wrong => ", Er)
        else:
            result=cursor.fetchall()
        return result

    #Create a function whoEnroll to count and display students who enrolled in a course
    def whoEnroll(self,courseId):
        #CourseId: Id of the course
        cursor=self.conxDB.cursor()
        
        s_query="SELECT student.name, course.name, registration.lecturehall FROM student "
        l_query="LEFT JOIN (course, registration) ON (course.level=student.class AND registration.studentId=student.Id) "
        w_query="WHERE course.Id=courseId"
        tb_query=s_query+l_query+w_query
        
        try:
            cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("An error occured! Please check what's wrong=> ",Er)
        else:
            result=cursor.fetchall()
            return result