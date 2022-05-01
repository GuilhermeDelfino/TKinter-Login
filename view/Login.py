import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font
from view.Signup import Signup
from controller.userController import UserController

class Login(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Users Login')
        self.grid()
        self.columnconfigure(0, weight=1)
        root_width = 600
        root_height = 400

        center_x = int(self.winfo_screenwidth() / 2 - root_width / 2)
        center_y = int(self.winfo_screenheight() / 2 - root_height / 2)

        self.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
        self.resizable(False, False)
        self.config(bg='#181818', padx=100)
        self.iconbitmap("assets/image/icon.ico")
        
        self.createWidget()
    
    def loginUser(self, email: str, password: str):
        user = UserController()
        data = user.login(email, password)
        if data['status_code'] == 200:
            messagebox.showinfo('Welcome!', data['message'])
            time.sleep(3)
            messagebox.showwarning('Success!', 'Now, you has been logged in own system. See you later!')
            time.sleep(3)
            self.destroy()
            
        else:
            messagebox.showwarning('Warning!', data['message'])
            
          
    def createWidget(self):
        email, password = tk.StringVar(), tk.StringVar()
        
        self.image_lock = tk.PhotoImage(file='./assets/image/padlock.png', palette=50)
        ttk.Label(self,foreground='#eeeeee',background='#181818', image=self.image_lock, compound='top',  text='Login', font=('Arial', 20, 'bold')).grid(column=0, row=0, pady=(20, 5))


        ttk.Label(self, width=50,text='E-mail',foreground='#eeeeee',background='#181818', font=('Arial', 16)).grid(column=0, row=1)
        ttk.Entry(self,textvariable=email, width=50, font=('Arial', 14)).grid(column=0, row=2)

        ttk.Label(self, width=50,text='Password',foreground='#eeeeee',background='#181818', font=('Arial', 16)).grid(column=0, row=3,  pady=(10,0))
        ttk.Entry(self, width=50,show='*', textvariable=password, font=('Arial', 14)).grid(column=0, row=4)

        self.image_singin = tk.PhotoImage(file='./assets/image/sign-in.png')
        button_font = font.Font(family='Arial', weight='bold', size=16)
        tk.Button(self, command=lambda: self.loginUser(email.get(), password.get()), activebackground='#DD5555', background='#CC5555', width=200, borderwidth=0,font=button_font, text='Sign In ', image=self.image_singin, compound='right').grid(ipady=5,column=0, sticky=tk.E, row=5, pady=10)

        button_font_create = font.Font(family='Arial', weight='normal', size=13)
        tk.Button(self, command=lambda: self.createAccount(), activebackground='#181818', foreground='#eeeeee', activeforeground='#eeeeee', background='#181818', borderwidth=0,font=button_font_create, text='Create new account ').grid(sticky=tk.W, ipady=5,column=0, row=5, pady=10)

    def createAccount(self):
        signup = Signup()
        signup.mainloop()