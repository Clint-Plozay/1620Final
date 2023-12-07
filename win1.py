import tkinter as tk
import tkinter.font as tkFont

class Win1:
    def __init__(self, root):

        self.GLabel_706=tk.Label(root)
        self.ft = tkFont.Font(family='Times',size=38)
        self.GLabel_706["font"] = self.ft
        self.GLabel_706["fg"] = "#333333"
        self.GLabel_706["justify"] = "center"
        self.GLabel_706["text"] = "Time Sheet"
        self.GLabel_706.pack()

        self.GLabel_622=tk.Label(root)
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLabel_622["font"] = self.ft
        self.GLabel_622["fg"] = "#333333"
        self.GLabel_622["justify"] = "center"
        self.GLabel_622["text"] = "Username"
        self.GLabel_622.pack()

        self.GLineEdit_61=tk.Entry(root)
        self.GLineEdit_61["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_61["font"] = self.ft
        self.GLineEdit_61["fg"] = "#333333"
        self.GLineEdit_61["justify"] = "center"
        self.usernamevar = tk.StringVar(root, "")
        self.GLineEdit_61["textvariable"] = self.usernamevar
        self.GLineEdit_61.pack()

        self.GLabel_138 = tk.Label(root)
        self.ft = tkFont.Font(family='Times', size=10)
        self.GLabel_138["font"] = self.ft
        self.GLabel_138["fg"] = "#333333"
        self.GLabel_138["justify"] = "center"
        self.GLabel_138["text"] = "Password"
        self.GLabel_138.pack()

        self.GLineEdit_85=tk.Entry(root)
        self.GLineEdit_85["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_85["font"] = self.ft
        self.GLineEdit_85["fg"] = "#333333"
        self.GLineEdit_85["justify"] = "center"
        self.passwordvar = tk.StringVar(root,"")
        self.GLineEdit_85["textvariable"] = self.passwordvar
        self.GLineEdit_85.pack()

        self.GButton_131=tk.Button(root)
        self.GButton_131["bg"] = "#f0f0f0"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_131["font"] = self.ft
        self.GButton_131["fg"] = "#000000"
        self.GButton_131["justify"] = "center"
        self.GButton_131["text"] = "Login"
        self.GButton_131.pack()
        self.GButton_131["command"] = self.login

        self.GButton_266=tk.Button(root)
        self.GButton_266["bg"] = "#f0f0f0"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_266["font"] = self.ft
        self.GButton_266["fg"] = "#000000"
        self.GButton_266["justify"] = "center"
        self.GButton_266["text"] = "Sign Up"
        self.GButton_266.pack()
        self.GButton_266["command"] = self.signup

if __name__ == "__main__":
    root = tk.Tk()
    #app = App(root)
    #root.mainloop()
