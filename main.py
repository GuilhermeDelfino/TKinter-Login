import tkinter as tk
from tkinter import ttk
from tkinter import font

root = tk.Tk()

root.title('Users Login')

root_width = 600
root_height = 400

center_x = int(root.winfo_screenwidth() / 2 - root_width / 2)
center_y = int(root.winfo_screenheight() / 2 - root_height / 2)

root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.iconbitmap("./assets/image/icon.ico")

def sum (a,b):
    print(a+b)
    
image_lock = tk.PhotoImage(file='./assets/image/padlock.png', palette=50)
ttk.Label(root, image=image_lock, compound='top', text='Login', font=('Arial', 20, 'bold')).pack(pady=10)

ttk.Label(root, text='E-mail', font=('Arial', 16)).pack()
input_email = ttk.Entry(root, font=('Arial', 14)).pack()

ttk.Label(root, text='Password', font=('Arial', 16)).pack()
input_password = ttk.Entry(root, show='*', font=('Arial', 14)).pack()

image_singin = tk.PhotoImage(file='./assets/image/sign-in.png')
button_font = font.Font(family='Arial', weight='bold', size=16)
tk.Button(root, font=button_font, text='Sign In', image=image_singin, compound='right').pack(ipadx=50, ipady=5, pady=20)

root.mainloop()