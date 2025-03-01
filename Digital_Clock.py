import tkinter as tk
from time import strftime

# Function to update time and date
def update_time():
    current_time = strftime('%H:%M:%S %p')  
    current_date = strftime('%A, %B %d, %Y')  
    
    time_label.config(text=current_time)  
    date_label.config(text=current_date) 

    time_label.after(1000, update_time)  

# Create the main window
root = tk.Tk()
root.title("Digital Clock") 
root.geometry("350x150")  
root.resizable(False, False)

# Create a label to display the date
date_label = tk.Label(root, font=('calibri', 20, 'bold'), background='black', foreground='cyan')
date_label.pack(anchor='center', pady=10)  

# Create a label to display the time
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
time_label.pack(anchor='center')

# Call function to update time and date
update_time()

# Run the application
root.mainloop()

