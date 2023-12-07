directoryPath = r"Employee"
directory = os.listdir(directoryPath)
found = False

for filename in directory:
    file = open(f"Employee/{filename}", 'r')
    fuser = file.readline()[9:]
    fpassw = file.readline()[9:]
    euser = self.usernamevar.get()
    epassw = self.passwordvar.get()
    print(fuser)
    print(fpassw)
    print(euser)
    print(epassw)
    if (fuser == euser) & (fpassw == epassw):
        self.loggedUser = file
        found = True
        print(found)
        self.hide1()
        break
    else:
        file.close()