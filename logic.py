from win1 import Win1
from win2 import Win2
from tkinter import *
import csv
import os
import re
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
        with open(f"Employee/{self.loggedUser}", "r+",newline = "") as employeeFile:
            #TODO: validate that shacleika
            csvWriter = csv.writer(employeeFile,delimiter=",")
            csvReader = csv.reader(employeeFile,delimiter=",")
            date = self.datevar.get() # in file entry[:8]
            start = self.startedvar.get()
            end = self.endedvar.get()
            dateslist = [i[0] for i in csvReader]
            print(dateslist)
            for item in dateslist:
                if item == date:
                    index = dateslist.index(item)
                    self.GButton_submit["command"] = lambda: self.overwrite(index)
                    self.outputvar.set(f"An entry for {date} already exists!\nClick 'Submit' again to overwrite, otherwise click 'clear'")
                    employeeFile.close()
                    return None

            csvWriter.writerow([date, f"{start}-{end}"])
            self.outputvar.set("Time recorded!")

    def overwrite(self,index):
        start = self.startedvar.get()
        end = self.endedvar.get()

        employeeFile = open(f"Employee/{self.loggedUser}",'r')
        csvReader = csv.reader(employeeFile, delimiter=",")
        filelist = [i for i in csvReader]
        print(filelist)
        employeeFile.close()

        employeeFile = open(f"Employee/{self.loggedUser}", 'w',newline="")
        csvWriter = csv.writer(employeeFile, delimiter=",")
        filelist[index][1] = f"{start}-{end}"
        print(filelist)
        csvWriter.writerows(filelist)
        employeeFile.close()
        self.outputvar.set("Time recorded!")
        self.clear()



    def clear(self):
        self.datevar.set("")
        self.startedvar.set("")
        self.endedvar.set("")
        self.outputvar.set("")
        self.GButton_submit["command"] = self.submit

    def login(self):
        user = self.usernamevar.get()
        passw = self.passwordvar.get()
        try:
            employeeFile = open(f"Employee/{user}",'r')
            user = employeeFile.readline()[9:].strip()
            print(user)
            filePass = employeeFile.readline()[9:].strip()
            print(filePass)
            if filePass == passw:
                self.loggedUser = user
                self.usernamevar.set("")
                self.passwordvar.set("")
                self.outputvar.set("")
                self.hide1()
                employeeFile.close()
            else:
                employeeFile.close()
                raise FileNotFoundError
        except FileNotFoundError:
            self.outputvar1.set("Username or Password incorrect")

    def logout(self):
        self.hide2()

    def signup(self):
        user = self.usernamevar.get()
        passw = self.passwordvar.get()
        directory = os.listdir("Employee")
        #regex: (?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[!?])[a-zA-Z0-9!?]{2,}
        if user not in directory:
            # TODO: add actual password validation
            if len(passw) >= 4:
                employeeFile = open(f"Employee/{user}","w")
                employeeFile.writelines([f"Username,{user}\n",f"Password,{passw}\n"])
                employeeFile.close()
                self.outputvar1.set("User successfully created!")
            else:
                self.outputvar1.set("password must be longer than 5 characters")
        else:
            self.outputvar1.set("User name already being used")
