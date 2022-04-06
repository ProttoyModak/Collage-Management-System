from tkinter import*

# Class Define
class Student:
        def __init__(self, root):
            self.root = root
            self.root.title("Collage Management System")
            self.root.geometry("1350x750+0+0")
            self.root.configure(background="#393E46")



# Objects
root = Tk()
ob = Student(root)
root.mainloop()