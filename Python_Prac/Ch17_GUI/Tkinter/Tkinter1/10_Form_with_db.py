from tkinter import *
import sqlite3

root=Tk()
root.title("Form")
root.geometry("450x600")
#Create a form entry widget

def add():
    #create or access db
    conn=sqlite3.connect("Student_db.db")

    #create curser instant
    cr=conn.cursor()

    #create Table with feilds
    
    cr.execute(""" Create table if not exists Students(
               f_name text,
               l_name text,
               address text,
               city text,
               phone integer
    )
""")
    
    #Insert data into table 
    cr.execute("insert into Students values (:f_name,:l_name,:address,:city,:phone)",
    {
        "f_name":f_name_e.get(),
        "l_name":l_name_e.get(),
        "address":address_e.get(),
        "city":city_e.get(),
        "phone":phone_e.get()})
    #Save changes
    conn.commit()
    #close connection
    conn.close()

    #clear the textboxes
    f_name_e.delete(0,END)
    l_name_e.delete(0,END)
    address_e.delete(0,END)
    city_e.delete(0,END)
    phone_e.delete(0,END)

def show():
        #create or access db
    conn=sqlite3.connect("Student_db.db")
    #create curser instant
    cr=conn.cursor()
    cr.execute("Select *,oid from Students")
    records=cr.fetchall()
    print_records=''
    for record in records:
        print_records+=str(record[0])+" "+str(record[1])+"\t"+str(record[5])+"\n"
    
    Label(root,text=print_records,padx=20,pady=10).grid(row=13,column=0,columnspan=2)

    #Save changes
    conn.commit()
    #close connection
    conn.close()

def save():
    #create or access db
    conn=sqlite3.connect("Student_db.db")
    #create curser instant
    cr=conn.cursor()   
    record_id=deletebox_e.get() 
    cr.execute("""Update Students set
               
               f_name=:fname,
               l_name=:lname,
               address=:address,
               city=:city,
               phone=:phone
               where oid=:oid""",
               {
                   "fname":Edit_fname_e.get(),
                   "lname":Edit_lname_e.get(),
                   "address":Edit_address_e.get(),
                   "city":Edit_city_e.get(),
                   "phone":Edit_phone_e.get(),
                   "oid":record_id
               }
               )
    Edit_fname_e.delete(0,END)
    Edit_lname_e.delete(0,END)
    Edit_address_e.delete(0,END)
    Edit_city_e.delete(0,END)
    Edit_phone_e.delete(0,END)
    deletebox_e.delete(0,END)
    conn.commit()
    conn.close()
def update():
    root2=Tk()
    root2.title("Edit Form")
    root2.geometry("450x600") 
            #create or access db
    conn=sqlite3.connect("Student_db.db")
    #create curser instant
    cr=conn.cursor()
    select_id=deletebox_e.get()
    cr.execute(f"Select * from Students where oid={select_id}")
    records=cr.fetchall()

    global Edit_fname_e
    global Edit_lname_e
    global Edit_address_e
    global Edit_city_e
    global Edit_phone_e
        
    Edit_fname_e=Entry(root2,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
    Edit_fname_e.grid(row=1,column=1,padx=20,pady=10)
    Edit_lname_e=Entry(root2,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
    Edit_lname_e.grid(row=2,column=1,padx=20,pady=10)
    Edit_address_e=Entry(root2,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
    Edit_address_e.grid(row=3,column=1,padx=20,pady=10)
    Edit_city_e=Entry(root2,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
    Edit_city_e.grid(row=4,column=1,padx=20,pady=10)
    Edit_phone_e=Entry(root2,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
    Edit_phone_e.grid(row=5,column=1,padx=20,pady=10)

    #Create labels for entry widget
    Label(root2,text="First Name",font="Locida 14 bold").grid(row=1,column=0,padx=20)
    Label(root2,text="Last Name",font="Locida 14 bold").grid(row=2,column=0,padx=20)
    Label(root2,text="Address",font="Locida 14 bold").grid(row=3,column=0,padx=20)
    Label(root2,text="City",font="Locida 14 bold").grid(row=4,column=0,padx=20)
    Label(root2,text="Phone No",font="Locida 14 bold").grid(row=5,column=0,padx=20)

    for record in records:
        Edit_fname_e.insert(0,record[0])
        Edit_lname_e.insert(0,record[1])
        Edit_address_e.insert(0,record[2])
        Edit_city_e.insert(0,record[3])
        Edit_phone_e.insert(0,record[4])
    btn_Save=Button(root2,text="Save Record",font="Locida 14 bold",bg="Blue",command=save)
    btn_Save.grid(row=11,column=0,columnspan=2,padx=20,pady=10,ipadx=125)
    conn.commit()
    conn.close()

def delete():
    #create or access db
    conn=sqlite3.connect("Student_db.db")
    #create curser instant
    cr=conn.cursor()
    cr.execute(f"Delete from students where oid={deletebox_e.get()}")
    deletebox_e.delete(0,END) 
    #Save changes
    conn.commit()
    #close connection
    conn.close()


f_name_e=Entry(root,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
f_name_e.grid(row=1,column=1,padx=20,pady=10)
l_name_e=Entry(root,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
l_name_e.grid(row=2,column=1,padx=20,pady=10)
address_e=Entry(root,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
address_e.grid(row=3,column=1,padx=20,pady=10)
city_e=Entry(root,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
city_e.grid(row=4,column=1,padx=20,pady=10)
phone_e=Entry(root,textvariable=StringVar(),font="Locida 14 bold",fg="Blue")
phone_e.grid(row=5,column=1,padx=20,pady=10)

#Create entrybox for delete
deletebox_e=Entry(root,font="Locida 14 bold",fg="red")
deletebox_e.grid(row=10,column=1,padx=20,pady=10)

#Create labels for entry widget
Label(root,text="First Name",font="Locida 14 bold").grid(row=1,column=0,padx=20)
Label(root,text="Last Name",font="Locida 14 bold").grid(row=2,column=0,padx=20)
Label(root,text="Address",font="Locida 14 bold").grid(row=3,column=0,padx=20)
Label(root,text="City",font="Locida 14 bold").grid(row=4,column=0,padx=20)
Label(root,text="Phone No",font="Locida 14 bold").grid(row=5,column=0,padx=20)

#label for deletebox
Label(root,text="Select ID",font="Locida 14 bold").grid(row=10,column=0,padx=20)

#Create buttons

btn_add=Button(root,text="Add Record to Database",font="Locida 14 bold",bg="green",command=add)
btn_add.grid(row=6,column=0,columnspan=2,padx=20,pady=10,ipadx=65)

btn_show=Button(root,text="Show Record",font="Locida 14 bold",bg="green",command=show)
btn_show.grid(row=7,column=0,columnspan=2,padx=20,pady=10,ipadx=115)

btn_delete=Button(root,text="Delete Record",font="Locida 14 bold",bg="red",command=delete)
btn_delete.grid(row=9,column=0,columnspan=2,padx=20,pady=10,ipadx=113)

btn_update=Button(root,text="Edit Record",font="Locida 14 bold",bg="Blue",command=update)
btn_update.grid(row=11,column=0,columnspan=2,padx=20,pady=10,ipadx=125)


root.mainloop()