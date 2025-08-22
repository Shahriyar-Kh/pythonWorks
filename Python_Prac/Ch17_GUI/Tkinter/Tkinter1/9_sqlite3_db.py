from tkinter import*
import sqlite3

root=Tk()
root.title("Sqlite3")

#Create or access db
conn=sqlite3.connect("Address_book.db")

#create courser instant
cr=conn.cursor()

#create table with feilds
cr.execute("""CREATE TABLE addresses(
           f_name text,
           l_name text,
           address text,
           City text,
           zipcode integer
)""")

#save changes
conn.commit()


#close connection
conn.close()

root.mainloop()