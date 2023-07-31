import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

# Data for the religious groups and their population in India
states = ["andhra", "Madhyapradesh", "tamilnadu", "Sikkim", "telengana", "gujarat", "Other"]
population = [31.5, 14.2, 20.0, 6.4, 21.0, 24.0, 3.9]

# Create a function to display the pie chart
def show_pie_chart():
    fig, ax = plt.subplots()
    ax.pie(population, labels=states, autopct='%1.1f%%', startangle=50)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.title("States Distribution in India (Percentage)")
    plt.show()

# Create a function to display the bar graph
def show_bar_graph():
    plt.bar(states, population)
    plt.xlabel("states in India")
    plt.ylabel("Population (%)")
    plt.title("states Distribution in India")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create the Tkinter application
root = tk.Tk()
root.title("Indian States Distribution")

# Create a button to display the pie chart
pie_button = ttk.Button(root, text="Show Pie Chart", command=show_pie_chart)
pie_button.pack(pady=10)

# Create a button to display the bar graph
bar_button = ttk.Button(root, text="Show Bar Graph", command=show_bar_graph)
bar_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()