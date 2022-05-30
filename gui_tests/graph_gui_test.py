
import tkinter as tk 
from tkinter import *
from PIL import Image, ImageTk
from requests import delete

import matplotlib.pyplot as plt
import numpy as np
from math import log, sqrt, pi, exp
import pandas as pd 
from scipy.stats import norm



root = tk.Tk()



class GBM:

    def simulate(self):
        while(self.total_time > 0):
            dS = self.current_price*self.drift*self.time_period + self.current_price*self.volatility*np.random.normal(0, sqrt(self.time_period))
            self.prices.append(self.current_price + dS)
            self.current_price += dS
            self.total_time -= self.time_period

    def __init__(self, initial_price, drift, volatility, time_period, total_time):
        # Initialize fields
        self.initial_price = initial_price
        self.current_price = initial_price
        self.drift = drift
        self.volatility = volatility
        self.time_period = time_period
        self.total_time = total_time
        self.prices = []
        # Simulate the diffusion process
        self.simulate()   # Simulate the diffusion proces
#Buttons 

#inital price entry box
inital_price_entry_box = tk.Entry(root, width=18, fg="grey")

inital_price_entry_box.grid(row=0, column=1, padx=10, pady=(10,0))


#current price entry box
current_price_entry_box = tk.Entry(root, width=18, fg="grey")

current_price_entry_box.grid(row=1, column=1, padx=10, pady=(10,0))


#volatility entry box
volatility_entry_box = tk.Entry(root, width=18, fg="grey")

volatility_entry_box.grid(row=2, column=1, padx=10, pady=(10,0))


#drift entry box
drift_entry_box = tk.Entry(root, width=18, fg="grey")

drift_entry_box.grid(row=3, column=1, padx=10, pady=(10,0))


#time period entry box
time_period_entry_box = tk.Entry(root, width=18, fg="grey")

time_period_entry_box.grid(row=4, column=1, padx=10, pady=(10,0))


#total time entry box
total_time_entry_box = tk.Entry(root, width=18, fg="grey")

total_time_entry_box.grid(row=5, column=1, padx=10, pady=(10,0))

#number of simulations entry box
number_of_simulations_entry_box = tk.Entry(root, width=18, fg="grey")

number_of_simulations_entry_box.grid(row=6, column=1, padx=10, pady=(10,0))

# Display the placeholder image 
img = Image.open(r'C:\Users\44786\Desktop\GIT_REPOS\login_system\GBM_GRAPH.png') 

test = ImageTk.PhotoImage(img)




#TextBox labels


#image label 
image_label = tk.Label(root, image=test)
image_label.grid(row=0, column=2, rowspan=6, padx=10, pady=(10,0))



#inital price label 
init_price_box_label = tk.Label(root, text="Initial Stock Price")
init_price_box_label.grid(row=0, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#current price label
current_price_box_label = tk.Label(root, text="Current Stock Price")
current_price_box_label.grid(row=1, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#volaity label
volatility_box_label = tk.Label(root, text="Volatility")
volatility_box_label.grid(row=2, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#drift label
drift_box_label = tk.Label(root, text="Drift")
drift_box_label.grid(row=3, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#time period label
time_period_box_label = tk.Label(root, text="Time Period")
time_period_box_label.grid(row=4, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#total time label
total_time_box_label = tk.Label(root, text="Total Time")
total_time_box_label.grid(row=5, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))


#number of simulations label
number_of_simulations_box_label = tk.Label(root, text="Number of Simulations")
number_of_simulations_box_label.grid(row=6, column=0, sticky=tk.W, padx=(10,0), pady=(10,0))

def submit_button_clicked():
    print("Submit button clicked")
    print("Initial Stock Price: " + inital_price_entry_box.get())
    print("Current Stock Price: " + current_price_entry_box.get())
    print("Volatility: " + volatility_entry_box.get())
    print("Drift: " + drift_entry_box.get())
    print("Time Period: " + time_period_entry_box.get())
    print("Total Time: " + total_time_entry_box.get())
    print("Number of Simulations: " + number_of_simulations_entry_box.get())
    inital_price_entry_box.delete(0, END)
    current_price_entry_box.delete(0, END)
    volatility_entry_box.delete(0, END)
    drift_entry_box.delete(0, END)
    time_period_entry_box.delete(0, END)
    total_time_entry_box.delete(0, END)
    number_of_simulations_entry_box.delete(0, END)


submit_button = tk.Button(root, text="Submit", command=lambda: submit_button_clicked())
submit_button.grid(row=7, column=1, padx=10, pady=(10,0))





# simulations = []
# n = float(number_of_simulations_entry_box.get())
# initial_price = float(inital_price_entry_box.get())
# drift = float(drift_entry_box.get())
# volatility = float(volatility_entry_box.get())
# time_period = float(time_period_entry_box.get())
# total_time = float(total_time_entry_box.get())


# for i in range(0, n):
#     simulations.append(GBM(initial_price, drift, volatility, time_period, total_time))

# for sim in simulations:
#     plt.plot(np.arange(0, len(sim.prices)), sim.prices)
#     plt.title('Simulation of GBM')
#     plt.xlabel('Time (Days)')
#     plt.ylabel('Price ($)')


root.mainloop()
