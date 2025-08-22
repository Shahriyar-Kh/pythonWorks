from tkinter import*
import mysql.connector
import csv
from tkinter import ttk

root=Tk()
root.title("CRM Project")
root.geometry("550x600")

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


#clear function
def clear():
    Label_Entry.fname_e.delete(0,END)
    Label_Entry.lname_e.delete(0,END)
    Label_Entry.add1_e.delete(0,END)
    Label_Entry.add2_e.delete(0,END)
    Label_Entry.city_e.delete(0,END)
    Label_Entry.state_e.delete(0,END)
    Label_Entry.phone_e.delete(0,END)
    Label_Entry.email_e.delete(0,END)
    Label_Entry.payment_m_e.delete(0,END)
    Label_Entry.Discount_code_e.delete(0,END)
    Label_Entry.price_paid_e.delete(0,END)
def add_data():
    sql_commond=("insert into customers(first_name,last_name,price_paid,phone_no,Email,address_1,address_2,city,state,payment_method,discount_code) \
        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    values=(Label_Entry.fname_e.get(),Label_Entry.lname_e.get(),Label_Entry.price_paid_e.get(),Label_Entry.phone_e.get(),Label_Entry.email_e.get(),Label_Entry.add1_e.get()
            ,Label_Entry.add2_e.get(),Label_Entry.city_e.get(),Label_Entry.state_e.get(),Label_Entry.payment_m_e.get(),Label_Entry.Discount_code_e.get())
    cr.execute(sql_commond,values)

    with open("Customers1.csv", "a", newline="") as f:
        w= csv.writer(f, dialect="excel")
        # for record1 in cr:
        w.writerow(values)
    
    conn.commit()
    #clear the fields 
    clear()

def Save(records):
    # file="E:\Python_Prac\Customers.csv"
    with open("Customers.csv", "a", newline="") as f:
        w = csv.writer(f, dialect="excel")
        for record1 in records:
            w.writerow(record1)



def Customers():
    root2=Tk()
    root2.title("List of Customers")
    
    #Reterive  Data from db
    cr.execute("Select * from customers")
    records=cr.fetchall()
    for index,record in enumerate(records):  
        lb=Label(root2,text=record)
        lb.grid(row=index,column=0)

    
    btn_Save=Button(root2,text="Save to Excel",font="Arial 13 bold",fg="White",bg="green",command=lambda:Save(records))
    btn_Save.grid(row=index+3,column=0)

    root2.mainloop()

def search():
    search_root=Tk()
    search_root.title("Search Customer")
    search_root.geometry("700x500")

    def Edit_now(id,idx):
        Edit_root=Tk()
        Edit_root.title("Edit Customer")
        Edit_root.geometry("700x500")

        def update_now():
            pass

        Label_Entry(Edit_root)
        user_id_l=Label(Edit_root,text="User ID",font="Locida 14")
        user_id_l.grid(row=12,column=0,sticky=W,padx=10)
        user_id_e=Entry(Edit_root,font="Locida 12 bold")
        user_id_e.grid(row=12,column=1,pady=5,ipadx=40)

        btn_update=Button(Edit_root,text="Update Record ",font="Locida 14 bold ",fg="white",bg="black",command=update_now)
        btn_update.grid(row=13,column=0,padx=10,pady=20)

        sql_com="Select * from customers where user_id=%s "
        id1=(id,)
        cr.execute(sql_com,id1)
        get_record=cr.fetchall()
        print(get_record)
        widget_e=[]
        for widget in Label_Entry(Edit_root):
            widget_e.append(widget)
           
        fname=widget_e[0]
        print(fname)
        lname=widget_e[1]
        print(lname)
        user_id_e.insert(0,get_record[0][0])
        fname.insert(0,get_record[0][2])


        Edit_root.mainloop()




    def search_now():
        # Remove previous result labels if they exist
        if hasattr(search_now, 'result_labels'):
            for label in search_now.result_labels:
                label.destroy()
        selected=drop_box.get()
        if selected=="First Name":
            sql_command = "SELECT * FROM customers WHERE first_name = %s"
        elif selected=="Last Name":
            sql_command = "SELECT * FROM customers WHERE last_name = %s"
        elif selected=="Customer ID":
            sql_command = "SELECT * FROM customers WHERE user_id = %s"
        else:
            Label(search_root,text="Hey! You Forget picked  a Selection",font="Locida 12 bold").grid(row=5,column=0,sticky=W,columnspan=5)

        searched = sr_e.get()
        search_value = (searched,)
        cr.execute(sql_command, search_value)
        result = cr.fetchall()

        if not result:
            result_text = "Record not found"
            result_l = Label(search_root, text=result_text, font="Locida 12 bold")
            result_l.grid(row=4, column=0, padx=10, columnspan=2)
            search_now.result_labels = [result_l]  # Store the label reference
        else:
            search_now.result_labels = []
            for idx, record in enumerate(result):
                id_ref=str(record[0])
                btn_edit=Button(search_root,text=f"Edit {id_ref}",font="Locida 14 bold ",fg="white",bg="black",command=lambda:Edit_now(id_ref,idx))
                btn_edit.grid(row=5+idx,column=0,padx=10,pady=20)
                record_text = ', '.join(map(str, record))
                result_l = Label(search_root, text=record_text, font="Locida 12 bold")
                result_l.grid(row=5+idx, column=1, padx=10, columnspan=25,sticky=W)
                
                search_now.result_labels.append(result_l)  # Store the label reference

        sr_e.delete(0, END)
        drop_box.delete(0,END)
        drop_box.current(0)

    
    sr_l=Label(search_root,text="Search",font="Arial 14 bold")
    sr_l.grid(row=1,column=0,padx=10,pady=10)

    sr_e=Entry(search_root,font="Locida 13 bold",fg="blue")
    sr_e.grid(row=1,column=1,padx=10,pady=10)

    btn_search1=Button(search_root,text="Search now",font="Locida 14 bold ",fg="white",bg="black",command=search_now)
    btn_search1.grid(row=3,column=1,padx=10,pady=20)

    drop_box=ttk.Combobox(search_root,value=["Search by...","First Name","Last Name","Customer ID"])
    drop_box.current(0)
    drop_box.grid(row=1,column=2,padx=10,pady=10)
    search_root.mainloop()


#Create a label
title_label=Label(root,text="Shary Customer database",font="Helvitica 16 bold",fg="white",bg="Black")
title_label.grid(row=0,column=0,columnspan=2,padx=50,pady=10)

def Label_Entry(root):
    #Create Main form for customer data
    fname_l=Label(root,text="First Name",font="Locida 14").grid(row=1,column=0,sticky=W,padx=10)
    lname_l=Label(root,text="Last Name",font="Locida 14").grid(row=2,column=0,sticky=W,padx=10)
    add1_l=Label(root,text="Address 1",font="Locida 14").grid(row=3,column=0,sticky=W,padx=10)
    add2_l=Label(root,text="Address 2",font="Locida 14").grid(row=4,column=0,sticky=W,padx=10)
    city_l=Label(root,text="City",font="Locida 14").grid(row=5,column=0,sticky=W,padx=10)
    state_l=Label(root,text="State",font="Locida 14").grid(row=6,column=0,sticky=W,padx=10)
    phone_l=Label(root,text="Phone No",font="Locida 14").grid(row=7,column=0,sticky=W,padx=10)
    pp_l=Label(root,text="Price_Paid",font="Locida 14").grid(row=8,column=0,sticky=W,padx=10)
    email_l=Label(root,text="Email",font="Locida 14").grid(row=9,column=0,sticky=W,padx=10)
    pm_l=Label(root,text="Payment Method",font="Locida 14").grid(row=10,sticky=W,padx=10)
    dc_l=Label(root,text="Dicount Code",font="Locida 14").grid(row=11,sticky=W,padx=10)


    fname_e=Entry(root,font="Locida 12 bold")
    fname_e.grid(row=1,column=1,pady=5,ipadx=40)
    lname_e=Entry(root,font="Locida 12 bold")
    lname_e.grid(row=2,column=1,padx=10,pady=5,ipadx=40)
    add1_e=Entry(root,font="Locida 12 bold")
    add1_e.grid(row=3,column=1,padx=10,pady=5,ipadx=40)
    add2_e=Entry(root,font="Locida 12 bold")
    add2_e.grid(row=4,column=1,padx=10,pady=5,ipadx=40)
    city_e=Entry(root,font="Locida 12 bold")
    city_e.grid(row=5,column=1,padx=10,pady=5,ipadx=40)
    state_e=Entry(root,font="Locida 12 bold")
    state_e.grid(row=6,column=1,padx=10,pady=5,ipadx=40)
    phone_e=Entry(root,font="Locida 12 bold")
    phone_e.grid(row=7,column=1,padx=10,pady=5,ipadx=40)
    price_paid_e=Entry(root,font="Locida 12 bold")
    price_paid_e.grid(row=8,column=1,padx=10,pady=5,ipadx=40)
    email_e=Entry(root,font="Locida 12 bold")
    email_e.grid(row=9,column=1,padx=10,pady=5,ipadx=40)
    payment_m_e=Entry(root,font="Locida 12 bold")
    payment_m_e.grid(row=10,column=1,padx=10,pady=5,ipadx=40)
    Discount_code_e=Entry(root,font="Locida 12 bold")
    Discount_code_e.grid(row=11,column=1,padx=10,pady=5,ipadx=40)
    return {
        "fname": fname_e,
        "lname": lname_e,
        "add1": add1_e,
        "add2": add2_e,
        "city": city_e,
        "state": state_e,
        "phone": phone_e,
        "pp": price_paid_e,
        "email": email_e,
        "pm": payment_m_e,
        "dc": Discount_code_e
    }


Label_Entry(root)

#Create buttons
btn_add=Button(root,text="Add Record to database",font="Arial 13 bold",fg="White",bg="green"
       ,command=add_data).grid(row=13,column=0,pady=10)
btn_add=Button(root,text="Clear Feilds",font="Arial 13 bold",padx=25,fg="White",bg="green"
    ,command=clear).grid(row=13,column=1,pady=10)

btn_list=Button(root,text="List of Customers",font="Arial 13 bold",fg="White",bg="green"
    ,command=Customers,padx=25).grid(row=14,column=0,pady=10)

btn_search=Button(root,text="Search Customer",font="Arial 13 bold",fg="White",bg="green"
    ,command=search).grid(row=14,column=1,pady=10)

root.mainloop()
