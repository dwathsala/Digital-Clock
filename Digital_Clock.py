import tkinter as tk
from time import strftime

# Function to update time and date
def update_time():
    current_time = strftime('%H:%M:%S %p')  # Get current time in HH:MM:SS AM/PM format
    current_date = strftime('%A, %B %d, %Y')  # Get current date (e.g., Monday, January 01, 2025)
    
    time_label.config(text=current_time)  # Update time label
    date_label.config(text=current_date)  # Update date label

    time_label.after(1000, update_time)  # Refresh every 1000ms (1 second)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")  # Set window title
root.geometry("350x150")  # Set window size
root.resizable(False, False)  # Disable resizing

# Create a label to display the date
date_label = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='cyan')
date_label.pack(anchor='center', pady=10)  # Add padding for spacing

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
time_label.pack(anchor='center')

# Call function to update time and date
update_time()

# Run the application
root.mainloop()

