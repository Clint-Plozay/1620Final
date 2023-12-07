from win1 import Win1
from win2 import Win2
from tkinter import *
import csv
import os
class Logic(Win1,Win2):
    def __init__(self,root):
        self.widget1 = Frame(root)
        self.widget2 = Frame(root)
        Win1.__init__(self,self.widget1)
        Win2.__init__(self,self.widget2)
        self.widget1.pack()
        self.loggedUser = None

    def hide2(self):
        self.widget2.pack_forget()
        self.widget1.pack()

    def hide1(self):
        self.widget1.pack_forget()
        self.widget2.pack()

    def submit(self):
        pass

    def clear(self):
        pass

    def login(self):
        user = self.usernamevar.get()
        passw = self.passwordvar.get()
        try:
            employeeFile = open(f"Employee/{user}.py",'r')
            employeeFile.readline()
            filePass = employeeFile.readline()
            print(filePass," pass in file")
            print(passw," pass we entered")
            if filePass == passw:
                self.loggedUser = employeeFile
                print("match")
            else:
                employeeFile.close()
                raise FileNotFoundError
        except FileNotFoundError:
            print("Username or Password incorrect")

    def logout(self):
        pass

    def signup(self):
        pass
