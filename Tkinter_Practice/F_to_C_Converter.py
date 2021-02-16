from tkinter import *

window = Tk()

def f_to_c():
    celcius = (float(e1_value.get()) - 32)/1.8
    t1.delete("1.0", END)
    t1.insert(END, celcius)

def c_to_f():
    farh = (float(e2_value.get())* 1.8) + 32
    t2.delete("1.0", END)
    t2.insert(END, farh)

b1 = Button(window, text = "Convert", command = f_to_c)
b1.grid(row = 0, column = 2)

b2 = Button(window, text = "Convert", command = c_to_f)
b2.grid(row = 2, column = 2)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

e2_value = StringVar()
e2 = Entry(window, textvariable = e2_value)
e2.grid(row = 2, column = 1)

lab1 = Label(window, text = "Fahrenheit to Celcius")
lab1.grid(row = 0, column = 0)

lab2 = Label(window, text = "Celcius")
lab2.grid(row = 1, column = 0)

lab3 = Label(window, text = "Celcius to Fahrenheit")
lab3.grid(row = 2, column = 0)

lab4 = Label(window, text = "Fahrenheit")
lab4.grid(row = 3, column = 0)

t1 = Text(window, height = 1, width = 20)
t1.grid(row = 1, column = 1)

t2 = Text(window, height = 1, width = 20)
t2.grid(row = 3, column = 1)

window.mainloop()