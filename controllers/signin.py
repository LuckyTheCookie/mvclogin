from models.main import Model
from models.auth import User
from views.main import View
import hashlib
import sqlite3
import pyotp
import time

mydb = sqlite3.connect("test.db")
mycursor = mydb.cursor()

print("[UNSECURE - LOCAL] Connecting to the database")
if mydb:
    print("[UNSECURE - LOCAL] Connection established")
else:
    print("Connection failed")




class SignInController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["signin"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.login_button.configure(command=self.signin)
        self.frame.signup_btn.configure(command=self.signup)

    def signup(self) -> None:
        self.view.switch("signup")

    def signin(self) -> None:
        username = self.frame.username_entry.get()
        password = self.frame.password_entry.get()
        data = {"username": username, "password": password}
        print(data)

        password = data["password"]
        passwordforotp = password
        password = hashlib.sha256(password.encode()).hexdigest()
        print("Encrypting password")
        # Check if the user exists in the database
        sql = "SELECT * FROM users WHERE username = ? "
        val = (data["username"],)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            print("User exists in the database")
            # Check if the password is correct
            sql = "SELECT * FROM users WHERE username = ? AND password = ?"
            val = (data["username"], password)
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
            if result:
                print("Password is correct")
                self.connection()
            else:
                print("Password is incorrect")
                self.frame.password_entry.delete(0, len(password))
                # Verify if the user has entered his otp
                sql = "SELECT otp_key FROM users WHERE username = ?"
                val = (data["username"],)
                mycursor.execute(sql, val)
                result = mycursor.fetchall()
                print("fetching otp key")
                # Convert the result to a string
                result = str(result)
                # If result is not empty, the user already has a secret key
                if result != "[('',)]":
                    print("otp key found")
                    print("OTP key is " + result)
                    totp = pyotp.TOTP(result[0][0])
                    print("Password entered is" + passwordforotp)
                    print("OTP is" + totp.now())
                    if totp.verify(passwordforotp):
                        print("OTP is correct")
                        self.connection()
        else:
            print("User does not exist in the database")

    def clear_form(self) -> None:
        username = self.frame.username_entry.get()
        password = self.frame.password_entry.get()
        self.frame.username_entry.delete(0, len(username))
        self.frame.password_entry.delete(0, len(password))

    def connection(self) -> None:
        username = self.frame.username_entry.get()
        password = self.frame.password_entry.get()
        data = {"username": username, "password": password}

        self.frame.password_entry.delete(0, len(password))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)
        self.clear_form()



        
