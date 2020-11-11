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
        updatebtn=Button(Button_Frame,text="UPDATE",width=10).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(Button_Frame,text="DELETE",width=10).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(Button_Frame,text="CLEAR",width=10).grid(row=0,column=3,padx=10,pady=10)

        #Detail_Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink")
        Detail_Frame.place(x=650,y=100,width=670,height=580)

        #Detail_Frame components
        lbl_search=Label(Detail_Frame,text="SEARCH",font=("times new roman",20,"bold"),bg="pink",fg="black")
        lbl_search.grid(row=0,column=0,pady=0,padx=10,sticky="w")
        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",15,"bold"),state="readonly")
        combo_search['values']=("Name","Admit Date","ID","Contact")
        combo_search.grid(row=0,column=1,pady=0,padx=0,sticky="w")

        txt_search=Entry(Detail_Frame,width=10,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=0,padx=10,sticky="w")
        searchbtn=Button(Detail_Frame,text="SEARCH",width=10).grid(row=0,column=3,padx=0,pady=0)
        showallbtn=Button(Detail_Frame,text="SHOW ALL",width=10).grid(row=0,column=4,padx=10,pady=0)

        #Table_Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="pink")
        Table_Frame.place(x=5,y=50,width=650,height=515)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        #Student_Table
        Student_Table=ttk.Treeview(Table_Frame,columns=("name","id","age","adm","gender","contact","condition","aod","add"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_Table.xview)
        scroll_y.config(command=Student_Table.yview)
        Student_Table.heading("name",text="Name")
        Student_Table.heading("id",text="ID")
        Student_Table.heading("age",text="Age")
        Student_Table.heading("adm",text="Admit Date")
        Student_Table.heading("gender",text="Gender")
        Student_Table.heading("contact",text="Contact")
        Student_Table.heading("condition",text="Condition")
        Student_Table.heading("aod",text="Other Disease")
        Student_Table.heading("add",text="Address")
        Student_Table["show"]="headings"
        Student_Table.column("name",width=100)
        Student_Table.column("id",width=50)
        Student_Table.column("age",width=50)
        Student_Table.column("adm",width=100)
        Student_Table.column("gender",width=50)
        Student_Table.column("contact",width=100)
        Student_Table.column("condition",width=50)
        Student_Table.column("aod",width=100)
        Student_Table.column("add",width=100)
        Student_Table.pack(fill=BOTH,expand=1)

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
        con.close()

root=Tk()
ob=Student(root)
root.mainloop()
