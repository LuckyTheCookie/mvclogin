from models.main import Model
from models.auth import User
from views.main import View
import hashlib
import sqlite3
from tkinter import messagebox
mydb = sqlite3.connect("test.db")
mycursor = mydb.cursor()

class SignUpController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["signup"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signup_btn.configure(command=self.signup)
        self.frame.signin_btn.configure(command=self.signin)

    def signin(self) -> None:
        self.frame.signup_btn.configure(state="disabled")
        self.view.switch("signin")

    def signup(self) -> None:
        data = {
            "rank": self.frame.user_type.get(),
            "fullname": self.frame.fullname_entry.get(),
            "username": self.frame.username_entry.get(),
            "password": self.frame.password_entry.get(),
            "has_agreed": self.frame.has_agreed.get(),
        }
        print(data)
        user: User = {"username": data["username"]}
        self.clear_form()

        print("[UNSECURE - LOCAL] Connecting to the database")
        if mydb:
            print("[UNSECURE - LOCAL] Connection established")
            # Verify that the user hasn't already signed up
            sql = "SELECT * FROM users WHERE username = ?"
            val = (data["username"],)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
            if result:
                messagebox.showerror("User already exists", "The username already exists. Please choose another username.")
                return
            # Check if the user has a very complex password
            if len(data["password"]) < 8:
                messagebox.showerror("Weak password", "The password should be at least 8 characters long.")
                return
            # Check if the user has lowercase, uppercase, and special characters in the password
            has_lowercase = False
            has_uppercase = False
            has_special_char = False
            for char in data["password"]:
                if char.islower():
                    has_lowercase = True
                if char.isupper():
                    has_uppercase = True
                if not char.isalnum():
                    has_special_char = True
            if not has_lowercase or not has_uppercase or not has_special_char:
                messagebox.showerror("Weak password", "The password should contain lowercase, uppercase, and special characters.")
                return
            else:
                print("Creating a new account")
                # Encrypt password before saving to database
                password = data["password"]
                password = hashlib.sha256(password.encode()).hexdigest()
                print("Encrypting password")
                # Save the user data to the database - Table: users - Columns: id, user_type, full_name, username, password
                sql = "INSERT INTO users (rank, full_name, username, password) VALUES (?, ?, ?, ?)"
                val = (data["rank"], data["fullname"], data["username"], password)
                mycursor.execute(sql, val)
                mydb.commit()
                print("User saved to the database")
                self.model.auth.login(user)

        else:
            print("Connection failed")


    def clear_form(self) -> None:
        fullname = self.frame.fullname_entry.get()
        username = self.frame.username_entry.get()
        password = self.frame.password_entry.get()
        self.frame.fullname_entry.delete(0, len(fullname))
        self.frame.fullname_entry.focus()
        self.frame.username_entry.delete(0, len(username))
        self.frame.password_entry.delete(0, len(password))
        self.frame.user_type.set("")

        self.frame.has_agreed.set(False)

