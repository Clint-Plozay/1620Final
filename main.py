from person import *
import os

directoryPath = r"Employee"
objectList = []
directory = os.listdir(directoryPath)

for filename in directory:
    objectList.append(Person(open(f"Employee/{filename}", 'r')))

for employee in objectList:
    print(employee)
