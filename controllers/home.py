from models.main import Model
from views.main import View
import sqlite3
from .otpconfig import OtpController
from tkinter import messagebox
from .root_account_manager import RootAccountManagerController


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signout_btn.configure(command=self.logout)
        self.frame.root_signup_btn.configure(command=self.admin_signup)
        self.frame.config_otp_btn.configure(command=self.otp)
        self.frame.manage_account_btn.configure(command=self.manage_account)

    def otp(self) -> None:
        self.view.switch("otpconfig")
        # Generate the OTP for the user
        otp_controller = OtpController(self.model, self.view)
        otp_controller.generate_otp()

    def logout(self) -> None:
        self.model.auth.logout()

    def admin_signup(self) -> None:
        self.view.switch("rootsignup")

    def update_view(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            username = current_user["username"]
            self.frame.greeting.configure(text=f"Login successful, welcome {username} !")
        else:
            self.frame.greeting.configure(text=f"")

        # Get the rank of the user from the database
        mydb = sqlite3.connect("test.db")
        mycursor = mydb.cursor()
        sql = "SELECT rank FROM users WHERE username = ?"
        val = (username,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            rank = result[0][0]
            self.frame.greeting_rank.configure(text=f"You've been connected as : {rank}")
        else:
            self.frame.greeting_rank.configure(text=f"Rank: Error fetching rank")
        
        if result:
            rank = result[0][0]
            if rank == "Integrator" or rank == "Manufacturer":
                self.frame.root_signup_btn.configure(state="normal")
                self.frame.manage_account_btn.configure(text="Root Manage Accounts")
                self.frame.root_signup_btn.grid(row=4, column=0, padx=10, pady=5)
            else:
                self.frame.root_signup_btn.configure(state="disabled")
                self.frame.manage_account_btn.configure(text="Manage Account")
                self.frame.root_signup_btn.grid_forget()
        else:
            self.frame.root_signup_btn.configure(state="disabled")

    def manage_account(self) -> None:
        current_user = self.model.auth.current_user
        if current_user:
            username = current_user["username"]
        else:
            return
        # Get the rank of the user from the database
        mydb = sqlite3.connect("test.db")
        mycursor = mydb.cursor()
        sql = "SELECT rank FROM users WHERE username = ?"
        val = (username,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            rank = result[0][0]
            if rank == "Integrator" or rank == "Manufacturer":
                self.view.switch("rootaccountmanager")
                root_account_manager_controller = RootAccountManagerController(self.model, self.view)
                root_account_manager_controller.update_view()
            else:
                self.view.switch("accountmanager")
                messagebox.showerror("Permission Denied", "This feature has been disabled by your administrator")
        else:
            self.view.switch("accountmanager")
            messagebox.showerror("Permission Denied", "This feature has been disabled by your administrator")
    

