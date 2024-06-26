from models.main import Model
from models.auth import User
from views.main import View
import hashlib
import sqlite3
mydb = sqlite3.connect("test.db")
mycursor = mydb.cursor()

class RootSignUpController:
    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view
        self.frame = self.view.frames["rootsignup"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.root_signup_btn.configure(command=self.signup)
        self.frame.home_btn.configure(command=self.home)

    def home(self) -> None:
        self.clear_form()
        self.frame.root_signup_btn.configure(state="disabled")
        self.view.switch("home")

    def signup(self) -> None:
        data = {
            "rank": self.frame.user_type.get(),
            "fullname": self.frame.fullname_entry.get(),
            "username": self.frame.username_entry.get(),
            "password": self.frame.password_entry.get(),
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
                print("User already exists")
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
                self.home()
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

    
