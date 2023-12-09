from tkinter import *
from logic import *

def main():
    """
    This is the main method
    """
    main = Tk()
    main.geometry("400x542")
    logic = Logic(main)
    main.mainloop()

if __name__ == "__main__":
    main()