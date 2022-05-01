import time
import tkinter as tk
from tkinter import Toplevel, ttk, messagebox
from tkinter import font
from controller.userController import UserController

class Signup(Toplevel):
  
    def __init__(self):
        super().__init__()
        
        self.title('Create new account')
        self.grid()
        self.columnconfigure(0, weight=1)
        root_width = 400
        root_height = 300

        center_x = int(self.winfo_screenwidth() / 2 - root_width / 2)
        center_y = int(self.winfo_screenheight() / 2 - root_height / 2)

        self.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.config(bg='#181818', padx=50)
        self.iconbitmap("./assets/image/icon.ico")
        
        self.createWidget()
        
    def create(self):
        email, password = self.email.get(), self.password.get()
        user = UserController()
        res = user.createUser(email, password)
        if  res['status_code'] == 201:
            messagebox.showinfo('Success', res['message'])
            time.sleep(2)
            self.destroy()
        else:
            messagebox.showerror('Error', res['message'])
        
            
    def createWidget(self):
        
        self.email = tk.StringVar()
        self.password = tk.StringVar()

        ttk.Label(self,foreground='#eeeeee',background='#181818', compound='top',  text='Sign Up', font=('Arial', 20, 'bold')).grid(column=0, row=0, pady=(30, 5))

        ttk.Label(self, width=50,text='Enter your e-mail',foreground='#eeeeee',background='#181818', font=('Arial', 16)).grid(column=0, row=1)
        ttk.Entry(self,textvariable=self.email, width=50, font=('Arial', 14)).grid(column=0, row=2)

        ttk.Label(self, width=50,text='Enter your password',foreground='#eeeeee',background='#181818', font=('Arial', 16)).grid(column=0, row=3,  pady=(10,0))
        ttk.Entry(self, textvariable=self.password, width=50,show='*', font=('Arial', 14)).grid(column=0, row=4)

        button_font = font.Font(family='Arial', weight='bold', size=16)
        tk.Button(self, command=self.create, activebackground='#DD5555', background='#CC5555', width=200, borderwidth=0,font=button_font, text='Create').grid(ipady=5,column=0, sticky=tk.E, row=5, pady=10)

        