import mysql.connector as conn
import csv

# Connect to mysql-server
mydb = conn.connect(
    host="localhost",
    user="root",
    password= "",
    database="Academics"
)
print("Hi")

# Create cursor object
mycursor = mydb.cursor()

# Create DATABASE
mycursor.execute("CREATE DATABASE IF NOT EXISTS Academics")
print("Database created")

# Create college table
mycursor.execute('''CREATE TABLE IF NOT EXISTS college (
College_id INT PRIMARY KEY NOT NULL UNIQUE,
College_Name VARCHAR(100) NOT NULL,
College_Address VARCHAR(100) NOT NULL,
College_city VARCHAR(100) NOT NULL,
College_country VARCHAR(100) NOT NULL)''')
print("College table created")

# Create professor table
# mycursor.execute("DROP TABLE proffessor")
mycursor.execute('''CREATE TABLE IF NOT EXISTS proffessor (
teacher_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
Teacher_Name VARCHAR(100) NOT NULL,
teacher_Email VARCHAR(255) NOT NULL UNIQUE,
College_id INT NOT NULL, Date_joined DATE NOT NULL, Speciality VARCHAR(100), Salary REAL, Experience INT(5),
  CONSTRAINT FK_proffeso_college
  FOREIGN KEY (College_id)
        REFERENCES college(College_id)  )''')
print("Professor table created")

# Create student table
mycursor.execute('''CREATE TABLE IF NOT EXISTS student (
Student_id INT(10) AUTO_INCREMENT PRIMARY KEY NOT NULL UNIQUE,
Student_Name VARCHAR(100) NOT NULL,
Student_Email VARCHAR(255) NOT NULL UNIQUE,
College_id INT NOT NULL, Date_joined DATE NOT NULL, Major_taken VARCHAR(100) NOT NULL, College_Level VARCHAR(100) NOT NULL,
  CONSTRAINT FK_student_college
  FOREIGN KEY (College_id)
        REFERENCES college(College_id)  )''')
print("Student table created")


#  Insert college records from csv file
with open('D:\SchoolDatabase\colleges.csv', 'r') as collegerec:
    c_reader = csv.reader(collegerec)

    next(c_reader)  # dkip first ecord
    for rec in c_reader:
        mycursor.execute(
            "INSERT IGNORE INTO college(College_id, College_Name, College_Address, College_city, College_country) VALUES(%s, %s, %s, %s, %s)", rec)
        mydb.commit()
print("College records added")

#  Insert teacheer records from csv file
with open('D:\SchoolDatabase\proffesors.csv', 'r') as profrec:
    p_reader = csv.reader(profrec)

    next(p_reader)  # dkip first ecord
    for rec in p_reader:
        mycursor.execute(
            "INSERT IGNORE INTO proffessor(teacher_id, Teacher_Name, teacher_Email, College_id, Date_joined, Speciality, Salary, Experience) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", rec)
        mydb.commit()
print("Professor records added")

#  Insert stuent records from csv file
with open('D:\SchoolDatabase\students.csv', 'r') as srec:
    s_reader = csv.reader(srec)

    next(s_reader)  # dkip first ecord
    for rec in s_reader:
        mycursor.execute(
            "INSERT IGNORE INTO student(Student_id, Student_Name, Student_Email, College_id, Date_joined, Major_taken, College_Level) VALUES (%s, %s, %s, %s, %s, %s, %s)", rec)
        mydb.commit()
print("Student records added")

# Function to join the three tables


def acadenia():
    mycursor.execute(
        "SELECT * FROM student INNER JOIN college \
         ON college.College_id = student.College_id\
         INNER JOIN proffessor ON college.College_id = proffessor.College_id ")

    print(" \n\t\t\t\t School Records ")
    print("______________________________________________________________________________\n")
    for j in mycursor.fetchall():
        print(j)


acadenia()

mycursor.close()
print('\n Bye')
