import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="root")
cur=db.cursor()

def insert():
    uid=input("Enter User Id :- ")
    uname=input("Enter User Name :- ")
    vno=input("Enter Vehicle Number :- ")
    add=input ("Enter Your Address :- ")
    age=int(input("Enter User Age :- "))
    vmod=input("Enter Vehicle Model :- ")
    com=input("Enter Vehicle Company :- ")
    yom=int(input("Enter Vehicle Year Of Manufacturing :- "))
    try:
        cur.execute("INSERT INTO tw values('"+str(vno)+"','"+str(vmod)+"','"+str(com)+"','"+str(yom)+"')")
        db.commit()
        print("INSERTING DATA SUCCESSFULL")
    except:
        print("ERROR WHILE EXECUTING PROGRAM.....!!")
    try:
        cur.execute("INSERT INTO users values('"+str(uid)+"','"+str(uname)+"','"+str(vno)+"','"+str(add)+"','"+str(age)+"')")
        db.commit()
        print("INSERTING DATA SUCCESSFULL")
    except:
        print("ERROR WHILE EXECUTING PROGRAM.....!!")

def q1():
    cur.execute("select user_name from users,tw where tw.vehicle_number= users.vehicle_number and company='HONDA'")
    for i in cur:
        print(i)
def q2():
    cur.execute("select user_name,users.vehicle_number from users,tw where tw.vehicle_number= users.vehicle_number and year_of_manufacture='2018'")
    for i in cur:
        print(i)
def q3():
    cur.execute("select count(*) from users where age='20'")
    for i in cur:
        print(i)
def q4():
    cur.execute("select user_name,users.vehicle_number from users,tw where tw.vehicle_number= users.vehicle_number order by year_of_manufacture desc, user_name asc")
    for i in cur:+
        print(i)
def q5():
    #cur.execute("alter table users add no_of_members int")
    #print("TABLE ALTERED")
    #cur.execute("desc users")
    cur.execute("update users set no_of_members=5 where user_id='1'")
    db.commit()
    print("DATA UPDATED")
def q6():
    uname2=input("Enter Username :- ")
    cur.execute("update users set user_name= '"+str(uname2)+"' where users.vehicle_number='GJ01VM8890'")
    db.commit()
def q8():
    vno2=input("Enter Vehicle Number :- ")
    cur.execute("update users,tw set tw.vehicle_Number,users.vehicle_number= '"+str(vno2)+"' where tw.vehicle_number= users.vehicle_number and user_id='1001'")
    db.commit()
def q9():
    cur.execute("select * from users order by age desc")
    for i in cur:
        print(i)
def q10():
    cur.execute("DELETE from users,tw where tw.vehicle_number= users.vehicle_number and year_of_manufacture<='1980'")
    db.commit()
def main():
    #cur.execute("DROP DATABASE RTO_Ahmedabad")
    cur.execute("create database if not exists RTO_Ahmedabad")
    db.commit()
    #print("DATABASE CREATED")
    cur.execute("Use RTO_Ahmedabad")
    cur.execute("create table if not exists tw(vehicle_number varchar(20) primary key,model varchar(20),company varchar(20),year_of_manufacture int(10))")
    db.commit()
    #print("tw Table Created")
    db.commit()
    cur.execute("create table if not exists users(user_id varchar(20) primary key,user_name varchar(20),vehicle_number varchar(20) references tw(vehicle_number),address varchar(20),age int(3))")
    #print("Users Table Created")
    print("Press 0. To Insert Data.")
    print("Press 1. To Attempt Q1.")
    print("Press 2. To Attempt Q2.")
    print("Press 3. To Attempt Q3.")
    print("Press 4. To Attempt Q4.")
    print("Press 5. To Attempt Q5.")
    print("Press 6. To Attempt Q6.")
    print("Press 7. To Attempt Q7.")
    print("Press 8. To Attempt Q8.")
    print("Press 9. To Attempt Q9.")
    print("Press 10. To Attempt Q10.")
    x=int(input("Enter Your Choice :- "))
    if(x==0):
        insert()
    elif(x==1):
        q1()
    elif(x==2):
        q2()
    elif(x==3):
        q3()
    elif(x==4):
        q4()
    elif(x==5):
        q5()
    elif(x==6):
        q6()
    #elif(x==7):
    elif(x==8):
        q8()
    elif(x==9):
        q9()
    elif(x==10):
        q10()
    else:
        print("------ENTER VALID CHOICE------")
main()
