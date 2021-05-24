# Small app to experiment with data visualization and Tkinter

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

root = tk.Tk()
root.title("Plotting")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(20000, 25000, 5000)
    plt.fill(house_prices)
    plt.show()

my_button = tk.Button(root, text = 'Graph It!', command = graph)
my_button.pack()


root.mainloop()