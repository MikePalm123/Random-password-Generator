# Random Password generator
# 5 letters 3 numbers 1 charactor
#Imports
import tkinter as tk
import string
import random
import time
# Symbol Dictionaries
symbols = ["!","@","#","$","%","^","*","(",")","-","+","_",":",";"]
numbers = list(string.digits)
letters = list(string.ascii_letters)
#Simulate Generation
def passGen(label,generate_button):
    generate_button.config(state= tk.DISABLED)
    for i in range(0,100,10):
        label.config(text = f"Generating Password... {i}%")
        label.update()
        time.sleep(.03)
    generate_button.config(state=tk.NORMAL)
# Password creation
def createPassWord():
    password = ""
    for _ in range(5):
        letter = random.randint(0,51)
        password += letters[letter]
    for _ in range(3):
        num = random.randint(0,9)
        password += numbers[num]
    for _ in range(1):
        symbol = random.randint(0,13)
        password += symbols[symbol]
    return password
def gui():
    #password get and return
    def passwordGet():
        passGen(output_label, generate_button)
        password = createPassWord()
        output_label.config(text = f"Generated Password: {password}")
    #intialize Window
    window = tk.Tk()
    window.title("Password Gen")
    window.geometry("400x200")
    #Text
    instruction_label = tk.Label(window, text="Click the button to generate a password")
    instruction_label.pack(pady=10)
    #Password Gen
    generate_button = tk.Button(window, text="Generate Password",command= passwordGet)
    generate_button.pack(pady=10)
    #Output Label
    output_label = tk.Label(window, text="")
    output_label.pack(pady=10)
    #MainLoop
    window.mainloop()
gui()

 