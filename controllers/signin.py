from models.main import Model
from models.auth import User
from views.main import View
from tkinter import messagebox
import hashlib
import sqlite3
import pyotp
import time

mydb = sqlite3.connect("test.db")
mycursor = mydb.cursor()

# Create the database if it does not exist
try:
    mycursor.execute("SELECT * FROM users")
    print("[UNSECURE - LOCAL] Database connected")

except sqlite3.OperationalError:
    if messagebox.askyesno(title="Database error !", message="Error connecting to the database, do you want to create a new database ?", icon="error"):
        mycursor.execute("CREATE TABLE users (username TEXT, password TEXT, otp_key TEXT, rank TEXT)")
        mydb.commit()
        print("[UNSECURE - LOCAL] Database created")
    else:
        messagebox.showerror(title="Database error !", message="You won't be able to use the application without a database, exiting...")
        exit()
finally:
    mydb.close()





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

        # Encrypt the password
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        print("Encrypting password")

        try:
            # Connect to the database
            mydb = sqlite3.connect("test.db")
            mycursor = mydb.cursor()

            # Check if the user exists in the database
            sql = "SELECT * FROM users WHERE username = ?"
            val = (username,)
            mycursor.execute(sql, val)
            result = mycursor.fetchone()  # Use fetchone() to get a single result
            if result:
                print("User exists in the database")

                # Check if the password is correct
                sql = "SELECT * FROM users WHERE username = ? AND password = ?"
                val = (username, encrypted_password)
                mycursor.execute(sql, val)
                result = mycursor.fetchone()  # Use fetchone() to get a single result
                if result:
                    print("Password is correct")
                    self.connection()
                else:
                    print("Password is incorrect")
                    self.frame.password_entry.delete(0, len(password))

                    # Verify if the user already has a secret key
                    sql = "SELECT otp_key FROM users WHERE username = ?"
                    val = (username,)
                    mycursor.execute(sql, val)
                    result = mycursor.fetchone()  # Use fetchone() to get a single result
                    print("fetching otp key")
                    if result and result[0]:  # Check if result is not empty and has a valid OTP key
                        otp_key = result[0]
                        print("otp key found")
                        totp = pyotp.TOTP(otp_key)
                        print("Current OTP:", totp.now())
                        print("Verifying OTP")
                        if totp.verify(password):
                            print("OTP is correct")
                            self.connection()
                        else:
                            print("OTP is incorrect")
                    else:
                        print("No OTP key found for the user")
            else:
                print("User does not exist in the database")
        except sqlite3.Error as e:
            print(f"Database error: {e}")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            if mydb:
                mydb.close()

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
        user = {"username": data["username"]}
        self.model.auth.login(user)
        self.clear_form()



        
