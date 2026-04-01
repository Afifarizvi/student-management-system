import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql 

win=tk.Tk()
win.config(bg="#1E1E2F")
win.geometry("1350x700+0+0")
win.title("Student Management System")


title_label=tk.Label(win,text="Student Management System", font=("Segoe UI",30,"bold"),border=8,relief=tk.GROOVE,bg="#2C2F33",foreground="white")
title_label.pack(side=tk.TOP,fill=tk.X)                                       #heading

detail_frame=tk.LabelFrame(win,text="Enter Details",font=("Segoe UI",20),bg="#2C2F33",fg="white",bd=8,relief=tk.GROOVE)
detail_frame.place(x=30,y=90,width=420,height=575)

data_frame=tk.Frame(win, bd=8,bg="#2C2F33",relief=tk.GROOVE)
data_frame.place(x=485,y=90,width=810,height=575)

#------------------------------VARIABLES-------------------------------------#

rollno=tk.StringVar()
name=tk.StringVar()
class_var=tk.StringVar()
section=tk.StringVar()
contact=tk.StringVar()
fathersnm=tk.StringVar()
address=tk.StringVar()
gender=tk.StringVar()
dob=tk.StringVar()

search_by=tk.StringVar()
search_entry=tk.StringVar() 

#---------------------------------ENTRY--------------------------------------#

rollno_lbl = tk.Label(detail_frame,text= "Roll no",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

name_lbl = tk.Label(detail_frame,text= "Name",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

class_lbl = tk.Label(detail_frame,text= "Class",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)

section_lbl = tk.Label(detail_frame,text= "Section",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
section_lbl.grid(row=3,column=0,padx=2,pady=2)

section_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=section)
section_ent.grid(row=3,column=1,padx=2,pady=2)

contact_lbl = tk.Label(detail_frame,text= "Contact",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

father_lbl = tk.Label(detail_frame,text= "Father's Name",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
father_lbl.grid(row=5,column=0,padx=2,pady=2)

father_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=fathersnm)
father_ent.grid(row=5,column=1,padx=2,pady=2)

address_lbl = tk.Label(detail_frame,text= "Address",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
address_lbl.grid(row=6,column=0,padx=2,pady=2)

address_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

gender_lbl = tk.Label(detail_frame,text= "Gender",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent=ttk.Combobox(detail_frame,font=("Segoe UI",15),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female","Others")
gender_ent.grid(row=7,column=1,padx=2,pady=2)

dob_lbl = tk.Label(detail_frame,text= "D.O.B",font=("Segoe UI",15),bg="#2C2F33",foreground="white")
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent=tk.Entry(detail_frame,bd=4,font=("Segoe UI",15),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)

#------------------------------------------------------------------------#
#------------------------------FUNCTIONS----------------------------------#

def fetch_data():
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr=conn.cursor()
    curr.execute("SELECT * FROM data") #query to execute
    rows=curr.fetchall()
    if len(rows)!=0:
       student_table.delete(*student_table.get_children())
       for row in rows:
           student_table.insert('',tk.END,values=row)
    conn.close()

def add_func():
    if rollno.get()== "" or name.get()=="" or class_var.get()=="":
        messagebox.showerror("Error!","Please fill all the fields!")
    else:
        conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
        curr=conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),section.get(),contact.get(),fathersnm.get(),address.get(),gender.get(),dob.get()))          
        conn.commit()
        conn.close()

        fetch_data()

def get_cursor(event):
    '''this function will fetch data for the selected row '''
    cursor_row=student_table.focus()
    content=student_table.item(cursor_row)
    row=content['values']
    if row:
        rollno.set(row[0])
        name.set(row[1])
        class_var.set(row[2])
        section.set(row[3])
        contact.set(row[4])
        fathersnm.set(row[5])
        address.set(row[6])
        gender.set(row[7])
        dob.set(row[8])

def clear():
    '''this function will clear the function boxes'''
    rollno.set("")
    name.set("")
    class_var.set("")
    section.set("")
    contact.set("")
    fathersnm.set("")
    address.set("")
    gender.set("")
    dob.set("")



def update_func():
    '''this function will update data acc to user'''
    conn=pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr=conn.cursor()
    curr.execute("UPDATE data set name=%s,class=%s,section=%s,contact=%s,fathersnm=%s,address=%s,gender=%s,dob=%s WHERE rollno=%s",(name.get(),class_var.get(),section.get(),contact.get(),fathersnm.get(),address.get(),gender.get(),dob.get(),rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()

def delete_func():
    if rollno.get() == "":
        messagebox.showerror("Error!", "Please select a record to delete!")
    else:
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to delete Roll No: {rollno.get()}?")
        if confirm:
            conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
            curr = conn.cursor()
            curr.execute("DELETE FROM data WHERE rollno=%s", (rollno.get(),))
            conn.commit()
            conn.close()
            fetch_data()
            clear()
            messagebox.showinfo("Success", "Record deleted successfully!")

def search_func():
    if search_by.get() == "" or search_entry.get() == "":
        messagebox.showerror("Error!", "Please select search criteria and enter a value!")
    else:
        conn = pymysql.connect(host="localhost", user="root", password="", database="sms1")
        curr = conn.cursor()

        if search_by.get() == "Name":
            curr.execute("SELECT * FROM data WHERE name LIKE %s", ('%' + search_entry.get() + '%',))
        elif search_by.get() == "Roll no":
            curr.execute("SELECT * FROM data WHERE rollno=%s", (search_entry.get(),))
        elif search_by.get() == "Contact":
            curr.execute("SELECT * FROM data WHERE contact=%s", (search_entry.get(),))
        elif search_by.get() == "D.O.B":
            curr.execute("SELECT * FROM data WHERE dob=%s", (search_entry.get(),))

        rows = curr.fetchall()
        conn.close()

        student_table.delete(*student_table.get_children())
        if len(rows) != 0:
            for row in rows:
                student_table.insert('', tk.END, values=row)
        else:
            messagebox.showinfo("Info", "No records found!")

def show_all_func():
    fetch_data()
    search_entry.set("")
    search_by.set("")
        

#--------------------------------BUTTONS---------------------------------#
btn_frame=tk.Frame(detail_frame,bg="#2C2F33",bd=10,relief=tk.GROOVE)
btn_frame.place(x=20,y=390,width=352,height=110)

add_btn=tk.Button(btn_frame,bg="#2C2F33",text="ADD",bd=7,font=("Arial",14),width=14,command=add_func )
add_btn.grid(row=0,column=0,padx=4,pady=2)

update_btn=tk.Button(btn_frame,bg="#2C2F33",text="UPDATE",bd=7,font=("Arial",14),width=14,command=update_func)
update_btn.grid(row=0,column=1,padx=4,pady=2)

delete_btn=tk.Button(btn_frame,bg="#2C2F33",text="DELETE",bd=7,font=("Arial",14),width=14,command=delete_func)
delete_btn.grid(row=1,column=0,padx=4,pady=2)

clear_btn=tk.Button(btn_frame,bg="#2C2F33",text="CLEAR",bd=7,font=("Arial",14),width=14,command=clear)
clear_btn.grid(row=1,column=1,padx=4,pady=2)


#-------------------------------------------------------------------------#
#--------------------------------SEARCH-----------------------------------#
search_frame=tk.Frame(data_frame,bg="#2C2F33",bd=6,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lbl=tk.Label(search_frame,text="Search",bg="#2C2F33",fg="white",font=("Arial",18))
search_lbl.grid(row=0,column=0,padx=15,pady=2)

search_in=ttk.Combobox(search_frame,font=("Arial",14),state="readonly",textvariable=search_by)
search_in['values']=("Name","Roll no","Contact","D.O.B")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_ent=tk.Entry(search_frame,bd=4,font=("Arial",14),textvariable=search_entry,width=15)  
search_ent.grid(row=0,column=2,padx=10,pady=2)                                                

search_btn=tk.Button(search_frame,text="SEARCH",font=("Arial",13),bd=9,width=14,bg="black",command=search_func)
search_btn.grid(row=0,column=3,padx=10,pady=2)

showall_btn=tk.Button(search_frame,text="SHOW ALL",font=("Arial",13),bd=9,width=14,bg="black",command=show_all_func)
showall_btn.grid(row=0,column=4,padx=10,pady=2)

#------------------------------------------------------------------------#

#--------------------------DATABASE FRAME--------------------------------#

main_frame=tk.Frame(data_frame,bg="#2C2F33",bd=6,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll=tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll=tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table=ttk.Treeview(main_frame,columns=("Roll_No","Name","Class","Section","Contact","Father's Name","Address","Gender","D.O.B"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Roll_No",text="Roll_No")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Section",text="Section")
student_table.heading("Contact",text="Contact")
student_table.heading("Father's Name",text="Father's Name")
student_table.heading("Address",text="Address")
student_table.heading("Gender",text="Gender")
student_table.heading("D.O.B",text="D.O.B")


student_table['show']='headings'

student_table.column("Roll_No",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Section",width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Address",width=100)
student_table.column("Gender",width=100)
student_table.column("D.O.B",width=100)



student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

win.mainloop()