import os
from tkinter import Frame, messagebox, Label, Button, LabelFrame, Entry, Toplevel, Tk, StringVar, IntVar, END, BOTH
from tkinter import W, E, mainloop, X

"""
EMPLOYEE MANAGEMENT SYSTEM

    This is a Employee management system for the final project of first semester in Softwarica College
"""


class First:
    def __init__(self, master, colour):
        self.__master = master
        self.color = colour
        self.__master.geometry("1000x770+250+10")
        self.__master.title("Employee Management System")
        self.__master.config(background=colour)

    def page(self):
        Label(self.__master, text="User Interface", bg="Red", fg="Light Grey", height="3",
              font=("Didot", 20)).pack(fill=X)
        Label(self.__master, bg=self.color, text="").pack()
        Label(self.__master, bg=self.color, text="").pack()
        Label(self.__master, bg=self.color, text="").pack()

        frame = Frame(self.__master, bg=self.color, pady=80, borderwidth=0)
        frame.pack()
        frame2 = Frame(self.__master, bg=self.color, borderwidth=0)
        frame2.pack()
        register_btn = Button(frame, text="Register", bg="Grey",
                              activebackground="Black", activeforeground="White",
                              padx=20, pady=10, font=("Calibri", 15),
                              command=lambda: (main.withdraw(), Register_window(self.__master, self.color)))
        login_btn = Button(frame2, text="Login!!", activebackground="Black",
                           activeforeground="White", bg="Grey",
                           padx=24, pady=10, font=("Calibri", 15),
                           command=lambda: (self.__master.withdraw(), Login_window(self.__master, self.color)))
        register_btn.pack(side="top")
        login_btn.pack(side="bottom")
        Button(self.__master, text="QUIT!!", bg="Black", fg="White",
               command=self.__master.destroy).pack(pady=150)


class Register_window(First):
    def __init__(self, master, colour):
        self.__reg = Toplevel(master)
        super().__init__(self.__reg, colour)
        self.color = colour
        self.username = StringVar()
        self.password = StringVar()
        Label(self.__reg, text="Enter Your details", bg=colour, fg="White", font=("Calibri", 20)).place(x=400, y=250)
        Label(self.__reg, text="Username", bg=colour, fg="White", font=("Calibri", 15)).place(x=450, y=290)

        self.username_entry = Entry(self.__reg, textvariable=self.username)
        self.username_entry.insert(0, "*")
        self.username_entry.place(x=450, y=325)
        Label(self.__reg, text="Password", bg=colour, fg="White", font=("Calibri", 15)).place(x=450, y=365)
        self.password_entry = Entry(self.__reg, textvariable=self.password, show="*")
        self.password_entry.insert(0, "*")
        self.password_entry.place(x=450, y=400)
        Button(self.__reg, text="Submit", width=10, height=1,
               command=lambda: Register_window.submit(self, self.username.get(), self.password.get())).place(x=425,
                                                                                                             y=450)
        Button(self.__reg, text="Reset", width=10, height=1, command=lambda: Register_window.reset(self)).place(x=525,
                                                                                                                y=450)
        Button(self.__reg, text="Back", width=10, height=1,
               command=lambda: (self.__reg.destroy(), main.deiconify())).place(x=475,
                                                                               y=500)

    def submit(self, username_info, password_info):
        if len(password_info) < 8:
            __response = messagebox.showwarning("Weak Password!!",
                                                "The password should be more than 8 letters")
            if __response == "ok":
                Register_window.reset(self)
            raise Exception(__response)
        empty = [" ", "", "*"]
        if username_info in empty or password_info in empty:
            raise Exception(messagebox.showerror("Empty Entry", "Please fill the form"))
        else:
            try:
                file = open(str(username_info) + ".txt", "x")
            except FileExistsError:
                Register_window.user_exist()
            else:
                file.write(username_info + "\n")
                file.write(password_info)
                file.close()
                Label(self.__reg, text="Registration Success", fg="green", font=("Calibri", 15)).pack()

        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def reset(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.username_entry.insert(0, "*")
        self.password_entry.insert(0, "*")

    @staticmethod
    def user_exist():
        __response = messagebox.showwarning("User Exist", "User name already found!!")


class Login_window(First):
    def __init__(self, master, colour):
        self.__log = Toplevel(master)
        super().__init__(self.__log, colour)

        self.username_verify = StringVar()
        self.password_verify = StringVar()

        Label(self.__log, text="Enter Your Login-details", bg=colour, fg="White", font=("Calibri", 20)).place(x=400,
                                                                                                              y=250)
        Label(self.__log, text="Username", bg=colour, fg="White", font=("Calibri", 15)).place(x=450, y=290)
        self.username_entry1 = Entry(self.__log, textvariable=self.username_verify)
        self.username_entry1.insert(0, "*")
        self.username_entry1.place(x=450, y=325)

        Label(self.__log, text="Password", bg=colour, fg="White", font=("Calibri", 15)).place(x=450, y=365)
        self.password_entry1 = Entry(self.__log, textvariable=self.password_verify, show="*")
        self.password_entry1.insert(0, "*")
        self.password_entry1.place(x=450, y=400)
        Button(self.__log, text="Login", width=12, height=2, command=lambda: Login_window.verify(self)).place(x=465,
                                                                                                              y=450)
        Button(self.__log, text="Back", width=10, height=1,
               command=lambda: (self.__log.destroy(), main.deiconify())).place(x=475,
                                                                               y=500)

    def verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 + ".txt" in list_of_files:
            file1 = open(str(username1) + ".txt", "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.__log.withdraw()
                System(self.__log, color)
            else:
                Login_window.wrong_password()
        else:
            Login_window.user_not_found()

    @staticmethod
    def wrong_password():
        __response = messagebox.showerror("Wrong Password", "The password entered doesn't match")

    @staticmethod
    def user_not_found():
        __response = messagebox.showerror("Invalid User", "The  user data not found")


class System(Login_window):
    def __init__(self, master, colour):
        try:
            os.mkdir("Employee")
            os.mkdir("Department")
        except FileExistsError:
            print("Directory already exists")
        else:
            pass
        self.__logged = Toplevel(master)
        First.__init__(self, self.__logged, colour)
        self.frame1 = LabelFrame(self.__logged)
        self.frame1.pack()

        self.employee_name = StringVar()
        self.mail = StringVar()
        self.employee_code = StringVar()
        self.department_code = StringVar()
        self.department_name = StringVar()
        self.employee_surname = StringVar()

        frame = Frame(self.__logged, padx=15, pady=15)
        frame.place(x=400, y=200)
        Button(frame, text="Employee Details", font=("Calibri", 13), width=20, pady=15,
               command=lambda: (self.frame1.destroy(), frame.pack(side="left"), System.detail_employee(self))).pack()
        Button(frame, text="Add Employee", font=("Calibri", 13), width=20, pady=15,
               command=lambda: (self.frame1.destroy(), frame.pack(side="left"), System.add_employee(self))).pack()
        Button(frame, text="Department Details", font=("Calibri", 13), width=20, pady=15,
               command=lambda: (
                   self.frame1.destroy(), frame.pack(side="left"), System.detail_department(self))).pack()
        Button(frame, text="Add Department", font=("Calibri", 13), width=20, pady=15,
               command=lambda: (self.frame1.destroy(), frame.pack(side="left"), System.add_department(self))).pack()

        Button(self.__logged, text="Back", width=15, pady=10,
               command=lambda: (main.deiconify(), self.__logged.destroy())).pack()

    def add_employee(self):
        self.frame1 = Frame(self.__logged, width="400", height="400", padx=10, pady=10)
        Label(self.frame1, text="Add Employee", bg="Red", fg="Light Grey", height="3", font=("Didot", 13)).grid(
            row=0, column=0, columnspan=2, sticky=W + E)

        Label(self.frame1, text="First Name").grid(row=1, column=0, pady=10)
        self.employeename = Entry(self.frame1, textvariable=self.employee_name)
        self.employeename.grid(row=1, column=1, pady=10)

        Label(self.frame1, text="Last Name").grid(row=2, column=0, pady=10)
        self.employeesurname = Entry(self.frame1, textvariable=self.employee_surname)
        self.employeesurname.grid(row=2, column=1, pady=10)
        Label(self.frame1, text="Email").grid(row=3, column=0, pady=10)
        self.email = Entry(self.frame1, textvariable=self.mail)
        self.email.grid(row=3, column=1, pady=10)

        Label(self.frame1, text="Employee Code").grid(row=4, column=0, pady=10)
        self.employeecode = Entry(self.frame1, textvariable=self.employee_code)
        self.employeecode.grid(row=4, column=1, pady=10)

        Label(self.frame1, text="Department Code").grid(row=5, column=0, pady=10)
        self.departmentcode = Entry(self.frame1, textvariable=self.department_code)
        self.departmentcode.grid(row=5, column=1, pady=10)

        Label(self.frame1, text="Department Name").grid(row=6, column=0, pady=10)
        self.department = Entry(self.frame1, textvariable=self.department_name)
        self.department.grid(row=6, column=1, pady=10)
        print("adding employee")

        System.reset(self)

        Button(self.frame1, text="Submit",
               command=lambda: System.submit(self, self.employee_name.get(), self.employee_surname.get(),
                                             self.employee_code.get(), self.mail.get(),
                                             self.department_name.get(), self.department_code.get())).grid(row=7,
                                                                                                           column=0,
                                                                                                           columnspan=2)
        Button(self.frame1, text="Reset", command=lambda: System.reset(self)).grid(row=8, column=0, columnspan=2)

        self.frame1.pack(side="left", padx=100)

    def detail_employee(self):
        self.frame1 = LabelFrame(self.__logged, width="700", height="600", padx=5, pady=5)

        Label(self.frame1, text="First Name").grid(row=0, column=0)
        Label(self.frame1, text="Last Name").grid(row=0, column=1)
        Label(self.frame1, text="Employee Code").grid(row=0, column=2)
        Label(self.frame1, text="Email Address").grid(row=0, column=3)
        Label(self.frame1, text="Department Name").grid(row=0, column=4)
        Label(self.frame1, text="Department Code").grid(row=0, column=5)

        list_department = os.listdir("Employee/")
        x = 0
        for i in list_department:
            x += 1
            __file = open("Employee/" + i, "r")
            Label(self.frame1, text=__file.readline().replace("First Name:", "")).grid(row=x, column=0)
            Label(self.frame1, text=__file.readline().replace("Last Name:", "")).grid(row=x, column=1)
            Label(self.frame1, text=__file.readline().replace("Code:", "")).grid(row=x, column=2)
            Label(self.frame1, text=__file.readline().replace("Email:", "")).grid(row=x, column=3)
            Label(self.frame1, text=__file.readline().replace("Department:", "")).grid(row=x, column=4)
            Label(self.frame1, text=__file.readline().replace("Department Code:", "")).grid(row=x, column=5)
            __file.close()

        self.frame1.pack(side="left", padx=75, pady=15, fill=BOTH)

    def add_department(self):
        self.frame1 = Frame(self.__logged, width="400", height="400", padx=10, pady=10)
        Label(self.frame1, text="Add Department", bg="Red", fg="Light Grey", height="3", font=("Didot", 13)).grid(
            row=0, column=0, columnspan=2, sticky=W + E)

        Label(self.frame1, text="Department Code").grid(row=1, column=0, pady=10)
        self.departmentcode = Entry(self.frame1, textvariable=self.department_code)
        self.departmentcode.delete(0, END)
        self.departmentcode.insert(0, "*")
        self.departmentcode.grid(row=1, column=1, pady=10)

        Label(self.frame1, text="Department Name").grid(row=2, column=0, pady=10)
        self.department = Entry(self.frame1, textvariable=self.department_name)
        self.department.delete(0, END)
        self.department.insert(0, "*")
        self.department.grid(row=2, column=1, pady=10)

        Button(self.frame1, text="Submit",
               command=lambda: System.submit(self, department_name=self.department_name.get(),
                                             department_code=self.department_code.get())).grid(row=3, column=0,
                                                                                               columnspan=2)
        Button(self.frame1, text="Reset", command=lambda: System.clear(self)).grid(row=4, column=0, columnspan=2)

        self.frame1.pack(side="left", padx=100)

        print("adding department")

    def detail_department(self):
        self.frame1 = LabelFrame(self.__logged, width="700", height="600", padx=5, pady=5)

        Label(self.frame1, text="Department Code").grid(row=0, column=0)
        Label(self.frame1, text="Department Name").grid(row=0, column=1)

        list_department = os.listdir("Department/")
        x = 0
        for i in list_department:
            x += 1
            Label(self.frame1, text=i[:-4]).grid(row=x, column=0)
            __file = open("Department/" + i, "r")
            Label(self.frame1, text=__file.readline().replace("Department:", "")).grid(row=x, column=1)
            __file.close()

        self.frame1.pack(side="left", padx=200, pady=15, fill=BOTH)

        print("detailing department")

    def clear(self):
        self.departmentcode.delete(0, END)
        self.department.delete(0, END)
        self.departmentcode.insert(0, "*")
        self.department.insert(0, "*")

    def reset(self):
        self.employeename.delete(0, END)
        self.employeesurname.delete(0, END)
        self.employeecode.delete(0, END)
        self.email.delete(0, END)
        self.departmentcode.delete(0, END)
        self.department.delete(0, END)
        self.employeename.insert(0, "*")
        self.employeesurname.insert(0, "*")
        self.employeecode.insert(0, "*")
        self.email.insert(0, "*")
        self.departmentcode.insert(0, "*")
        self.department.insert(0, "*")

    def submit(self, employee_name=None, employee_surname=None, employee_code=None, mail=None, department_name=None,
               department_code=None):

        try:
            department_code = int(department_code)
        except ValueError:
            messagebox.showerror("String Input", "Cant input string in code section")
        else:
            dic = {
                "First Name": employee_name,
                "Last Name": employee_surname,
                "Code": employee_code,
                "Email": mail,
                "Department": department_name,
                "Department Code": department_code
            }
            if dic['Code'] is None:
                try:
                    dep = open(r"Department/" + str(department_code) + ".txt", "x")
                except FileExistsError:
                    messagebox.showerror("Duplicate Department", "The department code already exists")
                else:
                    for i, j in dic.items():
                        if j is not None:
                            dep.write("{}:{}\n".format(i, j))
                    messagebox.showinfo("Department Added", "Department has been added")
                finally:
                    System.clear(self)
            else:
                try:
                    dep = open(r"Employee/" + str(employee_code) + ".txt", "x")
                except FileExistsError:
                    messagebox.showerror("Duplicate Employee", "The employee code already exists")
                else:
                    for i, j in dic.items():
                        if j is not None:
                            dep.write("{}:{}\n".format(i, j))
                    messagebox.showinfo("Employee Added", "Employee has been added")
                finally:
                    System.reset(self)


main = Tk()
color = "#00000e"
window = First(main, color)
window.page()

mainloop()
