# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
    # Use a breakpoint in the code line below to debug your script.
# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random
from tkinter import messagebox
from tkinter import *

#password generating function
def generate_password():
    try:
        repeat = int(repeat_entry.get())
        length = int(length_entry.get())
    except:
        messagebox.showerror(message="Enter the required fields")
        return

    #Check if password allow for character repitition
    if repeat == 1:
        password = random.sample(character_string,length)
    else:
        password = random.sample(character_string,k=length)

    