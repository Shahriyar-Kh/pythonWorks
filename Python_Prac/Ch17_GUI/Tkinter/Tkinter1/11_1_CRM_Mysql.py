from tkinter import*
import mysql.connector

root=Tk()
root.title("CRM Project")
root.geometry("400x600")

#Create db connection 
conn=mysql.connector.connect(
    host="localhost",
    user="Shahriyar",
    password="shary786",
    #chose to database
    database="mydatabase",
)
#Check connection
if conn.is_connected:
    print("Connection is done")
else:
    print("wrong connection")

#create curser instance
cr=conn.cursor()

#check databases
cr.execute("Show databases")
for db in cr:
    print(db)

#create table 
cr.execute("""Create table if not exists Customers
           (
           user_id int auto_increment primary key,
           first_name varchar(255),
           last_name varchar(255),
           price_paid decimal(10,2),
           phone_no int(11)
           )
""")
#Alter table update structur of table
# cr.execute("Alter table Customers  add (\
#            Emial varchar(50),\
#            address_1 varchar(255),\
#            address_2 varchar(255),\
#            city varchar(50),\
#            state varchar(50),\
#            payment_method varchar(50),\
#            discount_code varchar(255))")

cr.execute("Alter table customers modify column phone_no int(20)")

#Show tables structure
cr.execute("Select * from customers")
for things in cr.description:
    print(things) 



root.mainloop()