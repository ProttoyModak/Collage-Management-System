from tkinter import*

# ======Class Define====== #
class Student:
        def __init__(self, root):
            self.root = root
            self.root.title("Collage Management System")
            self.root.geometry("1350x750+0+0")
            self.root.configure(background="#393E46")

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
            txtRoll= Entry(manageFrame, font=("times new roman", 15, "bold"), bd= 5, relief= GROOVE)
            txtRoll.grid(row=1, column=1, padx=20, pady=10, sticky="w")

            lblName = Label(manageFrame, text="Name: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblName.grid(row=2, column=0, padx=20, pady=10, sticky="w")
            txtName = Entry(manageFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            txtName.grid(row=2, column=1, padx=20, pady=10, sticky="w")

            lblEmail = Label(manageFrame, text="Email: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblEmail.grid(row=3, column=0, padx=20, pady=10, sticky="w")
            txtRoll = Entry(manageFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            txtRoll.grid(row=3, column=1, padx=20, pady=10, sticky="w")

            lblGender = Label(manageFrame, text="Gender: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblGender.grid(row=4, column=0, padx=20, pady=10, sticky="w")
            comboGender= ttk.Combobox(manageFrame, font=("times new roman", 15, "bold"), state= "readonly")
            comboGender['values'] = ("Male", "Female", "Other")
            comboGender.grid(row=4, column=1, padx=20, pady=10, sticky="w")

            lblContact = Label(manageFrame, text="Contact No: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblContact.grid(row=5, column=0, padx=20, pady=10, sticky="w")
            txtContact = Entry(manageFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            txtContact.grid(row=5, column=1, padx=20, pady=10, sticky="w")

            lblBirth = Label(manageFrame, text="D.O.B: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblBirth.grid(row=6, column=0, padx=20, pady=10, sticky="w")
            txtBirth = Entry(manageFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            txtBirth.grid(row=6, column=1, padx=20, pady=10, sticky="w")

            lblGPA = Label(manageFrame, text="SSC Result: ", font=("times new roman", 20, "bold"), bg="#006778", fg="#FFFFFF")
            lblGPA.grid(row=7, column=0, padx=20, pady=10, sticky="w")
            txtGPA = Entry(manageFrame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
            txtGPA.grid(row=7, column=1, padx=20, pady=10, sticky="w")


# ======Objects====== #
root = Tk()
ob = Student(root)
root.mainloop()