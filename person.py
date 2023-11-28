class Person:
    def __init__(self,inputFile):
        self.name = inputFile.readline()
        inputFile.close()

    def __str__(self):
        return self.name
