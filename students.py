
#We implement a few functions of students module
#First we import connection and query from queries module
from school.queries.connection import *
from school.queries.query import *
import mysql.connector

class Student:
    def __init__(self, *args):
        #conxDB: instance of connection to the database
        self.username=args[0]
        self.pwd=args[1]
        self.conxDB=self.getConnection(self.username, self.pwd)
        
    def getConnection(self, username,passwd):
        return connectServer("127.0.0.1", username, passwd, 10)


    #Create a function to add items to table student
    def addStudent(self, attributes, values):
        #attributes: list of attributes name of student table
        #values: list of tuples (value1, value2,..., valueN)
        #        each value is an information about the student profile
        
        cursor=self.conxDB.cursor()
        tb_query=inserttoTable("student", attributes, values)

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
    def selectStudent(self, requestedAttr, condition):
        #requestedAttr: list of attributes (string data type)
        #condition: condition on which rows of tables are selected
        #           attribute= or > value        
        
        cursor=self.conxDB.cursor()
        tb_query=select("student", requestedAttr, condition)
        
        try:
            cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Something is wrong => ", Er)
        else:
            result=cursor.fetchall()
        return result
    #this function help to update any attibute in the student table 
    def edit_value(self,attribute, value, condition):
        
        cursor = self.conxDB.cursor()
        atr_value =" "+attribute+"="+values
        tb_query = editparam(student, atr_value, condition)
        try:
            cursor.execute(tb_query)
        except mysql.connector.Error as Er:
            print("Something is wrong => ", Er)
        else:
            result=cursor.fetchall()
        return result