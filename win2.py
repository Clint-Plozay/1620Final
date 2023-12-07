import tkinter as tk
import tkinter.font as tkFont

class Win2:
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
        self.GLabel_622["text"] = "Date (mm/dd/yy)"
        self.GLabel_622.pack()

        self.GLineEdit_61=tk.Entry(root)
        self.GLineEdit_61["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_61["font"] = self.ft
        self.GLineEdit_61["fg"] = "#333333"
        self.GLineEdit_61["justify"] = "center"
        self.datevar = tk.StringVar(root, "")
        self.GLineEdit_61["textvariable"] = self.datevar
        self.GLineEdit_61.pack()

        self.GLabel_138 = tk.Label(root)
        self.ft = tkFont.Font(family='Times', size=10)
        self.GLabel_138["font"] = self.ft
        self.GLabel_138["fg"] = "#333333"
        self.GLabel_138["justify"] = "center"
        self.GLabel_138["text"] = "Started"
        self.GLabel_138.pack()

        self.GLineEdit_85=tk.Entry(root)
        self.GLineEdit_85["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_85["font"] = self.ft
        self.GLineEdit_85["fg"] = "#333333"
        self.GLineEdit_85["justify"] = "center"
        self.startedvar = tk.StringVar(root,"")
        self.GLineEdit_85["textvariable"] = self.startedvar
        self.GLineEdit_85.pack()

        self.GLabel_1382 = tk.Label(root)
        self.ft = tkFont.Font(family='Times', size=10)
        self.GLabel_1382["font"] = self.ft
        self.GLabel_1382["fg"] = "#333333"
        self.GLabel_1382["justify"] = "center"
        self.GLabel_1382["text"] = "Ended"
        self.GLabel_1382.pack()

        self.GLineEdit_852=tk.Entry(root)
        self.GLineEdit_852["borderwidth"] = "1px"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_852["font"] = self.ft
        self.GLineEdit_852["fg"] = "#333333"
        self.GLineEdit_852["justify"] = "center"
        self.endedvar = tk.StringVar(root,"")
        self.GLineEdit_852["textvariable"] = self.endedvar
        self.GLineEdit_852.pack()

        self.GButton_submit=tk.Button(root)
        self.GButton_submit["bg"] = "#f0f0f0"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_submit["font"] = self.ft
        self.GButton_submit["fg"] = "#000000"
        self.GButton_submit["justify"] = "center"
        self.GButton_submit["text"] = "Submit"
        self.GButton_submit.pack()
        self.GButton_submit["command"] = self.submit

        self.GButton_Clear=tk.Button(root)
        self.GButton_Clear["bg"] = "#f0f0f0"
        self.ft = tkFont.Font(family='Times',size=10)
        self.GButton_Clear["font"] = self.ft
        self.GButton_Clear["fg"] = "#000000"
        self.GButton_Clear["justify"] = "center"
        self.GButton_Clear["text"] = "Clear"
        self.GButton_Clear.pack()
        self.GButton_Clear["command"] = self.clear

        self.GButton_logout = tk.Button(root)
        self.GButton_logout["bg"] = "#f0f0f0"
        self.ft = tkFont.Font(family='Times', size=10)
        self.GButton_logout["font"] = self.ft
        self.GButton_logout["fg"] = "#000000"
        self.GButton_logout["justify"] = "center"
        self.GButton_logout["text"] = "Logout"
        self.GButton_logout.pack()
        self.GButton_logout["command"] = self.logout

        self.Label_output = tk.Label(root)
        self.ft = tkFont.Font(family='Times', size=10)
        self.Label_output["font"] = self.ft
        self.Label_output["fg"] = "#333333"
        self.Label_output["justify"] = "center"
        self.outputvar = tk.StringVar(root, "")
        self.Label_output["textvariable"] = self.outputvar
        self.Label_output.pack()

    def GButton_266_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    #app = App(root)
    #root.mainloop()
