import tkinter as tk

root = tk.Tk()
root.title("Simple Calculator")

e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10) # spans 3 columns

def button_click(number):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, tk.END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_equal():
    second_number = e.get()
    e.delete(0, tk.END)

    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, tk.END)

def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, tk.END)

# My buttons
# Lambda is added so a number could be passed into the function inside the paranthesis
# if no lambda is added, then don't add paranthesis
button1 = tk.Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button2 = tk.Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button3 = tk.Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))
button4 = tk.Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button5 = tk.Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button6 = tk.Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))
button7 = tk.Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button8 = tk.Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button9 = tk.Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))
button0 = tk.Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
buttonAdd = tk.Button(root, text = '+', padx = 39, pady = 20, command = button_add)
buttonEqual = tk.Button(root, text = '=', padx = 91, pady = 20, command = button_equal)
buttonClear = tk.Button(root, text = 'Clear', padx = 79, pady = 20, command = button_clear)

buttonSubtract = tk.Button(root, text = '-', padx = 41, pady = 20, command = button_sub)
buttonMultiply = tk.Button(root, text = '*', padx = 40, pady = 20, command = button_mult)
buttonDivide = tk.Button(root, text = '/', padx = 41, pady = 20, command = button_div)

# Put buttons on screen
# Third Row
button1.grid(row = 3, column = 0)
button2.grid(row = 3, column = 1)
button3.grid(row = 3, column = 2)
# Second Row
button4.grid(row = 2, column = 0)
button5.grid(row = 2, column = 1)
button6.grid(row = 2, column = 2)
# First Row
button7.grid(row = 1, column = 0)
button8.grid(row = 1, column = 1)
button9.grid(row = 1, column = 2)
# Forth Row
button0.grid(row = 4, column = 0)

# command buttons
buttonAdd.grid(row = 5, column = 0)
buttonClear.grid(row = 4, column = 1, columnspan = 2)
buttonEqual.grid(row = 5, column = 1, columnspan = 2)

buttonSubtract.grid(row = 6, column = 0)
buttonMultiply.grid(row = 6, column = 1)
buttonDivide.grid(row = 6, column = 2)

root.mainloop()