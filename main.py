from person import *
import os
from logic import *

def main():
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()

if __name__ == '__main__':
    main()

directoryPath = r"Employee"
objectList = []
directory = os.listdir(directoryPath)

for filename in directory:
    objectList.append(Person(open(f"Employee/{filename}", 'r')))

for employee in objectList:
    print(employee)
