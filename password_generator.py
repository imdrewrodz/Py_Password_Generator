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

