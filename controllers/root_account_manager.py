from models.main import Model
from views.main import View
import sqlite3
from .otpconfig import OtpController
from tkinter import messagebox


class RootAccountManagerController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["rootaccountmanager"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.configure(command=self.home)
        self.frame.suppress_account_btn.configure(command=self.suppress_account)

    def home(self) -> None:
        self.view.switch("home")

    def update_view(self) -> None:
        # Parse all users from the database and add them to the "user_combobox"
        mydb = sqlite3.connect("test.db")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT username FROM users")
        result = mycursor.fetchall()
        users = [user[0] for user in result]
        self.frame.user_combobox.configure(values=users)
        self.frame.user_combobox.set("Select User")

    def suppress_account(self) -> None:
        username = self.frame.user_combobox.get()
        if username == "Select User":
            return
        if messagebox.askyesno(title="Warning", message="Are you sure you want to suppress this account ?", icon="warning"):
            # Suppress the account
            mydb = sqlite3.connect("test.db")
            mycursor = mydb.cursor()
            sql = "DELETE FROM users WHERE username = ?"
            val = (username,)
            mycursor.execute(sql, val)
            mydb.commit()
            messagebox.showinfo(title="Account suppression", message="Account successfully suppressed !")
            self.update_view()
            mydb.close()
        else:
            messagebox.showinfo(title="Account suppression", message="The account has not been suppressed")


