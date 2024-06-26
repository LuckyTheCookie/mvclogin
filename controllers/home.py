from models.main import Model
from views.main import View
import sqlite3
from .otpconfig import OtpController


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
            else:
                self.frame.root_signup_btn.configure(state="disabled")
        else:
            self.frame.root_signup_btn.configure(state="disabled")
