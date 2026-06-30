#Maze_UI


import tkinter as tk
import customtkinter as ctk
import customtkinter
print(customtkinter.__version__)
root = tk.Tk()
root.geometry('800x500')
root.title('Mouse')

#Enter IP of robot
IP_of_robot = tk.Label(root, text="enter robot IP").grid(row=0, column=0)
IP_entry = tk.Entry(root)
IP_entry.grid(row=0, column=0)

#Enter password of robot
password_of_robot = tk.Label(root, text="enter robot password").grid(row=1, column=0)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=0)

# Quit the application
leave_app_button = tk.Button(root, text="stop", width=25, command=root.destroy)
leave_app_button.grid(row=2, column=0)

root.mainloop()