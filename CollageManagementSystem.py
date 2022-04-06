from tkinter import*
from tkinter import ttk
import pymysql

# ======Class Define====== #

class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Collage Management System")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background="#393E46")

        # ======All Variables====== #

        self.RollNo_var= StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Gender_var = StringVar()
        self.Contact_var = StringVar()
        self.DOB_var = StringVar()
        self.Result_var = StringVar()


        # ======Project Title====== #

        title = Label(self.root, text="Collage Management System", bg="#222831", fg="#00ADB5", bd=20, relief=GROOVE, font=("merriweather", 40, "bold"), padx=2, pady=6)
        title.pack(side=TOP, fill=X)

        # ======Project Frame: Adding section====== #

        manageFrame= Frame(self.root,bd=4, relief=RIDGE, bg="#006778")
        manageFrame.place(x=25, y=130, width=460, height=600)

        mTitle= Label(manageFrame, text="Manage Students", font=("merriweather", 30, "bold"), bg="#006778", fg="#FFD124")
        mTitle.grid(row= 0, columnspan= 2, padx= 50, pady= 20)

        lblRoll= Label(manageFrame, text="Student ID: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblRoll.grid(row= 1, column= 0, padx= 20, pady= 10, sticky= "w")
        txtRoll= Entry(manageFrame, textvariable= self.RollNo_var, font=("times new roman", 15, "bold"), bd= 5, relief= GROOVE)
        txtRoll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        lblName = Label(manageFrame, text="Name: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblName.grid(row=2, column=0, padx=20, pady=10, sticky="w")
        txtName = Entry(manageFrame, textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtName.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        lblEmail = Label(manageFrame, text="Email: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblEmail.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        txtEmail = Entry(manageFrame, textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtEmail.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        lblGender = Label(manageFrame, text="Gender: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblGender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
        comboGender= ttk.Combobox(manageFrame, textvariable=self.Gender_var, font=("times new roman", 15, "bold"), state= "readonly")
        comboGender['values'] = ("Male", "Female", "Other")
        comboGender.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        lblContact = Label(manageFrame, text="Contact No: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblContact.grid(row=5, column=0, padx=20, pady=10, sticky="w")
        txtContact = Entry(manageFrame, textvariable=self.Contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtContact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        lblBirth = Label(manageFrame, text="D.O.B: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblBirth.grid(row=6, column=0, padx=20, pady=10, sticky="w")
        txtBirth = Entry(manageFrame, textvariable=self.DOB_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtBirth.grid(row=6, column=1, padx=20, pady=10, sticky="w")

        lblGPA = Label(manageFrame, text="SSC Result: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
        lblGPA.grid(row=7, column=0, padx=20, pady=10, sticky="w")
        txtGPA = Entry(manageFrame, textvariable=self.Result_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txtGPA.grid(row=7, column=1, padx=20, pady=10, sticky="w")

        # ======Project Frame: Detail section====== #

        detailFrame = Frame(self.root, bd=4, relief=RIDGE, bg= "#5584AC")
        detailFrame.place(x=500, y=130, width=825, height=600)

        lblSearch = Label(detailFrame, text="Search Student: ", font=("times new roman", 20, "bold"), bg="#5584AC", fg="#FFFFFF")
        lblSearch.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        comboSearch = ttk.Combobox(detailFrame, width=12, font=("times new roman", 15, "bold"), state="readonly")
        comboSearch['values'] = ("ID", "Name", "Contact No")
        comboSearch.grid(row=0, column=1, pady=10, sticky="w")

        txtSearch = Entry(detailFrame, font=("times new roman", 14, "bold"), bd=5, relief=GROOVE)
        txtSearch.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        Searchbtn = Button(detailFrame, text="Search", width= 10).grid(row=0, column= 3, padx=10, pady= 10)
        Showbtn = Button(detailFrame, text="Show all", width=10).grid(row=0, column=4, padx=10, pady=10)

        # ======Project Frame: Detail table section====== #

        tableFrame= Frame(detailFrame, bd= 4, relief= RIDGE)
        tableFrame.place(x= 10, y= 70, width= 795, height= 510)

        scrollX= Scrollbar(tableFrame, orient= HORIZONTAL)
        scrollY = Scrollbar(tableFrame, orient=VERTICAL)
        self.Student_table= ttk.Treeview(tableFrame, column=("Roll", "Name", "Email", "Gender", "Contact", "DOB", "Result"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side= BOTTOM, fill= X)
        scrollX.config(command=self.Student_table.xview)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollY.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll",text="Student ID")
        self.Student_table.heading("Name", text="Student Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact No")
        self.Student_table.heading("DOB", text="Date of Birth")
        self.Student_table.heading("Result", text="SSC Result")

        self.Student_table.column("Roll", width= 150)
        self.Student_table.column("Name", width=150)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("DOB", width=150)
        self.Student_table.column("Result", width=100)

        self.Student_table['show'] = 'headings'
        self.Student_table.pack(fill= BOTH, expand= 1)
        self.Student_table.bind("<ButtonRelease-1>",self.getCursor)
        self.fetch_data()


        # ======Button Frame:====== #

        btnFrame = Frame(manageFrame, bd=4, relief=RIDGE, bg="#393E46")
        btnFrame.place(x=10, y=510, width=430)

        Addbtn = Button(btnFrame, command=self.addStudents, text="Add", width=11).grid(row=0, column=0, padx=8.5, pady=5)
        Updatebtn = Button(btnFrame, command= self.update_data, text="Update", width=11).grid(row=0, column=1, padx=8.5, pady=5)
        Clearbtn = Button(btnFrame, command= self.clear, text="Clear", width=11).grid(row=0, column=2, padx=8.5, pady=5)
        Deletetn = Button(btnFrame, command= self.delete_data, text="Delete", width=11).grid(row=0, column=3, padx=8.5, pady=5)

    # ======My SQL Connection====== #
    def addStudents(self):
        con = pymysql.connect(host='localhost', user='root',password='',database='cms')
        cur = con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(
            self.RollNo_var.get(),
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.DOB_var.get(),
            self.Result_var.get()))

        con.commit()
        self.clear()
        self.fetch_data()
        con.close()

    def fetch_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='cms')
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values= row)
            con.commit()
        con.close()

    def clear(self):
        self.RollNo_var.set("")
        self.Name_var.set("")
        self.Email_var.set("")
        self.Gender_var.set("")
        self.Contact_var.set("")
        self.DOB_var.set("")
        self.Result_var.set("")

    def getCursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.RollNo_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.DOB_var.set(row[5])
        self.Result_var.set(row[6])

    def update_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='cms')
        cur = con.cursor()
        cur.execute("update students set Roll= %s,Name= %s, Email= %s,Gender= %s,Contact= %s,Dob= %s,Result= %s", (
            self.RollNo_var.get(),
            self.Name_var.get(),
            self.Email_var.get(),
            self.Gender_var.get(),
            self.Contact_var.get(),
            self.DOB_var.get(),
            self.Result_var.get()))

        con.commit()
        self.clear()
        self.fetch_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host='localhost', user='root', password='', database='cms')
        cur = con.cursor()
        cur.execute("delete from students where Roll= %s", self.RollNo_var.get())
        con.commit()
        con.close()
        self.clear()
        self.fetch_data()





# ======Main Function====== #

root = Tk()
ob = Student(root)
root.mainloop()