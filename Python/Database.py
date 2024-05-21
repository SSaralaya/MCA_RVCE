import mysql.connector

try:
	db=mysql.connector.connect(host="localhost",user="mca081",password="mca081",auth_plugin="mysql_native_password",database="db_mca081")
	myCursor=db.cursor()
	print("Connected To Database Successfully...")
except Exception as e:
	print("Error in connceting to Database",e)

def create_table():
	query="""CREATE TABLE IF NOT EXISTS employee(
		slno INT,
		name VARCHAR(30),
		address VARCHAR(30),
		empcode VARCHAR(20) PRIMARY KEY,
		dob DATE,
		age INT,
		mobile VARCHAR(10),
		designation VARCHAR(30))"""
	myCursor.execute(query)
	db.commit()	
	print("Table Created Succesfully")


def insert_record():
	sno=int(input("Enter Serial Number:"))
	name=input("Enter Name:")
	address=input("Enter Address:")
	empcode=input("Enter Employee code:")
	dob=input("Enter Date of Birth:")
	age=int(input("Enter age:"))
	mobile=input("Enter mobile number:")
	designation=input("Enter Designation")
	query = """INSERT INTO employee (slno,name, address, empcode, dob, age, mobile, designation)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """
	values = (sno,name, address, empcode, dob, age, mobile, designation)
	myCursor.execute(query, values)
	db.commit()
	print("Record Inserted")
	
def show_records():
	myCursor.execute("SELECT * FROM employee")
	rows = myCursor.fetchall()
	print("Records in employee Table:")
	for row in rows:
		print(row)

def modify_record():
	empid=input("Enter employee code to update Designation:")
	des=input("Enter designation:")
	query = """UPDATE employee SET designation=%s WHERE empcode=%s """
	values = (des, empid)
	myCursor.execute(query, values)
	db.commit()
	print("Record Updated")

def delete_record():
	empid=input("Enter employee id to delete:")
	query = """DELETE FROM employee WHERE empcode=%s """
	values = (empid)
	myCursor.execute(query, values)
	db.commit()
	print("Record deleted")


f=1
while(f):
	print("\nMenu \n1.Create Table \n2.Insert Record \n3.Show All Records \n4.Update Designation \n5.Delete Record \n6.Exit")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		create_table()
	elif(ch==2):
		insert_record()
	elif(ch==3):
		show_records()
	elif(ch==4):
		modify_record()
	elif(ch==5):
		delete_record()
	elif(ch==6):
		f=0
	else:
		print("Invalid choice")
