import mysql.connector as conn

# Connect to mysql-server
mydb = conn.connect(
    host="localhost",
    user="root",
    password="newlight",
    database="Academics"
)
print("Hi")

# Create cursor object
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE colleges")
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
mycursor.execute('''CREATE TABLE IF NOT EXISTS proffessor (
teacher_id INT PRIMARY KEY NOT NULL UNIQUE,  
Teacher_Name VARCHAR(100) NOT NULL, 
teacher_Email VARCHAR(255) NOT NULL UNIQUE, 
College_id INT NOT NULL, Date_joined DATE NOT NULL, Speciality VARCHAR(100), Salary REAL, Experience INT(5),
  CONSTRAINT FK_proffeso_college
  FOREIGN KEY (College_id) 
        REFERENCES college(College_id)  )''')
print("Professor table created")

# Create student table
mycursor.execute('''CREATE TABLE IF NOT EXISTS student (
Student_id INT(10) PRIMARY KEY NOT NULL UNIQUE,  
Student_Name VARCHAR(100) NOT NULL, 
Student_Email VARCHAR(255) NOT NULL UNIQUE, 
College_id INT NOT NULL, Date_joined DATE NOT NULL, Major_taken VARCHAR(100) NOT NULL, College_Level VARCHAR(100) NOT NULL,
  CONSTRAINT FK_student_college
  FOREIGN KEY (College_id) 
        REFERENCES college(College_id)  )''')
print("Student table created")
