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
            csvWriter = csv.writer(employeeFile,delimiter=",")
            csvReader = csv.reader(employeeFile,delimiter=",")
            date = self.datevar.get() # in file entry[:8]
            start = self.startedvar.get()
            end = self.endedvar.get()
            if re.match("^[0-9][0-9]{1,1}\/[0-9][0-9]{1,1}\/[0-9][0-9]{1,1}$",date) and re.match("^[0-9]{1,2}:[0-9]{2,2}$",start) and re.match("^[0-9]{1,2}:[0-9]{2,2}$",end):
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
            else:
                self.outputvar.set("Date should be in mm/dd/yy format, and time should be in 24:00 time")
    def overwrite(self,index):
        start = self.startedvar.get()
        end = self.endedvar.get()
        date = self.datevar.get()
        if re.match("^[0-9][0-9]{1,1}\/[0-9][0-9]{1,1}\/[0-9][0-9]{1,1}$", date) and re.match("^[0-9]{1,2}:[0-9]{2,2}$",start) and re.match("^[0-9]{1,2}:[0-9]{2,2}$", end):
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
            self.clear()
            self.outputvar.set("Time recorded!")
        else:
            self.outputvar.set("Date should be in mm/dd/yy format, and time should be in 24:00 time")
            self.GButton_submit["command"] = self.submit


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
                self.outputvar1.set("")
                self.hide1()
                employeeFile.close()
            else:
                employeeFile.close()
                raise FileNotFoundError
        except FileNotFoundError:
            self.outputvar1.set("Username or Password incorrect")
        except:
            self.outputvar1.set("Username or Password incorrect")

    def logout(self):
        self.hide2()
        self.clear()

    def validPassword(self,passw):

        hasLower = False
        hasUpper = False
        hasSpecial = False
        hasNum = False

        for char in passw:
            if char.islower():
                hasLower = True
            if char.isupper():
                hasUpper = True
            if char.isalnum():
                hasSpecial = True
            if char.isdigit():
                hasNum = True

        return hasLower and hasUpper and hasSpecial and hasNum

    def signup(self):
        user = self.usernamevar.get()
        passw = self.passwordvar.get()
        directory = os.listdir("Employee")

        if user not in directory:
            if self.validPassword(passw) and len(passw) >= 5:
                employeeFile = open(f"Employee/{user}","w")
                employeeFile.writelines([f"Username,{user}\n",f"Password,{passw}\n"])
                employeeFile.close()
                self.outputvar1.set("User successfully created!")
            else:
                self.outputvar1.set("password must be longer than 5 characters, and must include:\n1 uppercase letter\n1 lowercase letter\n1 integer\n1 special character (!@#$%^&*!?)")
        else:
            self.outputvar1.set("User name already being used")
