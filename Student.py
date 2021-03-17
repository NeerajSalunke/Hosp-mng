from  tkinter import *
from tkinter import ttk
import pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="FORTIS HOSPITAL(covid ward)",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="red",fg="white")
        title.pack(side=TOP,fill=X)

        #All Variables
        self.name_var=StringVar()
        self.id_var=StringVar()
        self.age_var=StringVar()
        self.date_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.condition_var=StringVar()
        self.aod_var=StringVar()
        self.add_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()



        #Manage_Frame
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Manage_Frame.place(x=20,y=100,width=600,height=580)

        #Manage_Frame components
        m_title=Label(Manage_Frame,text="Enter Patient Details",font=("times new roman",30,"bold"),bg="pink",fg="black")
        m_title.grid(row=0,columnspan=2,padx=100,pady=0)

        lbl_name=Label(Manage_Frame,text="Enter name",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_name.grid(row=1,column=0,padx=20,pady=0,sticky="w")
        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_name.grid(row=1,column=1,pady=0,padx=10,sticky="w")

        lbl_id=Label(Manage_Frame,text="Enter ID",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_id.grid(row=2,column=0,padx=20,pady=0,sticky="w")
        txt_id=Entry(Manage_Frame,textvariable=self.id_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_id.grid(row=2,column=1,pady=0,padx=10,sticky="w")

        lbl_age=Label(Manage_Frame,text="Enter AGE",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_age.grid(row=3,column=0,pady=0,padx=20,sticky="w")
        txt_age=Entry(Manage_Frame,textvariable=self.age_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_age.grid(row=3,column=1,pady=0,padx=10,sticky="w")

        lbl_date=Label(Manage_Frame,text="Admit Date",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_date.grid(row=4,column=0,pady=0,padx=20,sticky="w")
        txt_date=Entry(Manage_Frame,textvariable=self.date_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_date.grid(row=4,column=1,pady=0,padx=10,sticky="w")

        lbl_gender=Label(Manage_Frame,text="Gender",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_gender.grid(row=5,column=0,pady=0,padx=20,sticky="w")
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"),state="readonly")
        combo_gender['values']=("Male","Female")
        combo_gender.grid(row=5,column=1,pady=0,padx=10,sticky="w")

        lbl_contact=Label(Manage_Frame,text="Contact no",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_contact.grid(row=6,column=0,pady=0,padx=20,sticky="w")
        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_contact.grid(row=6,column=1,pady=0,padx=10,sticky="w")

        lbl_status=Label(Manage_Frame,text="Condition",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_status.grid(row=7,column=0,pady=0,padx=20,sticky="w")
        combo_status=ttk.Combobox(Manage_Frame,textvariable=self.condition_var,font=("times new roman",15,"bold"),state="readonly")
        combo_status['values']=("No Symptoms","Mild","Critical")
        combo_status.grid(row=7,column=1,pady=0,padx=10,sticky="w")

        lbl_history=Label(Manage_Frame,text="Any other Disease",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_history.grid(row=8,column=0,pady=0,padx=20,sticky="w")
        combo_history=ttk.Combobox(Manage_Frame,textvariable=self.aod_var,font=("times new roman",15,"bold"))
        combo_history['values']=("None","BP","Diabetes","Hypertension","Kidney Disorder","Chronic Lung Disorder")
        combo_history.grid(row=8,column=1,pady=0,padx=10,sticky="w")

        lbl_add=Label(Manage_Frame,text="Address",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_add.grid(row=9,column=0,pady=0,padx=20,sticky="w")
        self.txt_add=Text(Manage_Frame,width=20,height=4,font=("times new roman",15),bd=5,relief=GROOVE)
        self.txt_add.grid(row=9,column=1,pady=0,padx=10,sticky="w")

        #Button_Frame
        Button_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="pink")
        Button_Frame.place(x=80,y=475,width=410)

        #Button in Button_Frame
        addbtn=Button(Button_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(Button_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(Button_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(Button_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        #Detail_Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Detail_Frame.place(x=650,y=100,width=670,height=580)

        #Detail_Frame components
        lbl_search=Label(Detail_Frame,text="SEARCH",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_search.grid(row=0,column=0,pady=0,padx=10,sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",15),state="readonly")
        combo_search['values']=("Name","Admit Date","id","Contact")
        combo_search.grid(row=0,column=1,pady=0,padx=0,sticky="w")

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=10,font=("times new roman",15),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=0,padx=10,sticky="w")
        searchbtn=Button(Detail_Frame,text="SEARCH",width=10,command=self.search_data).grid(row=0,column=3,padx=0,pady=0)
        showallbtn=Button(Detail_Frame,text="SHOW ALL",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=0)

        #Table_Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="pink")
        Table_Frame.place(x=5,y=50,width=650,height=515)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        #Student_Table
        self.Student_Table=ttk.Treeview(Table_Frame,columns=("name","id","age","adm","gender","contact","condition","aod","add"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("name",text="Name")
        self.Student_Table.heading("id",text="ID")
        self.Student_Table.heading("age",text="Age")
        self.Student_Table.heading("adm",text="Admit Date")
        self.Student_Table.heading("gender",text="Gender")
        self.Student_Table.heading("contact",text="Contact")
        self.Student_Table.heading("condition",text="Condition")
        self.Student_Table.heading("aod",text="Other Disease")
        self.Student_Table.heading("add",text="Address")
        self.Student_Table["show"]="headings"
        self.Student_Table.column("name",width=100)
        self.Student_Table.column("id",width=50)
        self.Student_Table.column("age",width=50)
        self.Student_Table.column("adm",width=100)
        self.Student_Table.column("gender",width=50)
        self.Student_Table.column("contact",width=100)
        self.Student_Table.column("condition",width=50)
        self.Student_Table.column("aod",width=100)
        self.Student_Table.column("add",width=100)
        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="hospital")
        cur=con.cursor()
        cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.name_var.get(),
                                                                              self.id_var.get(),
                                                                              self.age_var.get(),
                                                                              self.date_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.condition_var.get(),
                                                                              self.aod_var.get(),
                                                                              self.txt_add.get('1.0',END)))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="hospital")
        cur=con.cursor()
        cur.execute("select * from patient")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.name_var.set("")
        self.id_var.set("")
        self.age_var.set("")
        self.date_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.condition_var.set("")
        self.aod_var.set("")
        self.txt_add.delete('1.0',END)

    def get_cursor(self,ev):
        cursor_row=self.Student_Table.focus()
        contents=self.Student_Table.item(cursor_row)
        row=contents['values']
        self.name_var.set(row[0])
        self.id_var.set(row[1])
        self.age_var.set(row[2])
        self.date_var.set(row[3])
        self.gender_var.set(row[4])
        self.contact_var.set(row[5])
        self.condition_var.set(row[6])
        self.aod_var.set(row[7])
        self.txt_add.delete('1.0',END)
        self.txt_add.insert(END,row[8])

    #update_data not working
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="hospital")
        cur=con.cursor()
        cur.execute("update patient set name=%s,age=%s,adm=%s,gender=%s,contact=%s,condition=%s,aod=%s,add=%s where id=%s",(
                                                                              self.name_var.get(),                                                                        
                                                                              self.age_var.get(),
                                                                              self.date_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.condition_var.get(),
                                                                              self.aod_var.get(),
                                                                              self.txt_add.get('1.0',END),
                                                                              self.id_var.get()
                                                                              ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="hospital")
        cur=con.cursor()
        cur.execute("delete from patient where id=%s",self.id_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    #search_data not working
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="root",database="hospital")
        cur=con.cursor()
        cur.execute("select * from patient where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('',END,values=row)
            con.commit()
        con.close()


root=Tk()
ob=Student(root)
root.mainloop()
