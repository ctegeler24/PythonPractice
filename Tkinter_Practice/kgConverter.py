from tkinter import *
#Creates a Tkinter window
window = Tk()

# Defining a function that converts a user entry in kg into grams, pounds and ounces
def kg_converter():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274

    # empties the text boxes if they have been previously used
    t1.delete("1.0", END)
    t1.insert(END, grams)
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)
    
# Creating a button widget that uses the kg_converter when pressed
b1 = Button(window, text = 'convert', command = kg_converter) # Odd, you don't pass brackets in the function call
b1.grid(row = 0, column = 2) # grid is better then the pack function generally because you have more control over the button

# Creates a string variable object and an entry box 
e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

# Creates the label "kg"
e2 = Label(window, text = "kg")
e2.grid(row = 0, column = 0)

# Creates three empty text boxes where grams, pounds and ounces will be printed out
t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 20)
t3.grid(row = 1, column = 2)

# Keeps the main window open
window.mainloop()

