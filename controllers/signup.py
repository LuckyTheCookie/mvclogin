from models.main import Model
from models.auth import User
from views.main import View
import mysql.connector
import hashlib

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="testlogin"
)
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
        self.model.auth.login(user)
        self.clear_form()

        print("[UNSECURE] Connecting to the database")
        if mydb.is_connected():
            print("[UNSECURE] Connection established")
        else:
            print("[UNSECURE] Connection failed")

        # Encrypt password before saving to database
        password = data["password"]
        password = hashlib.sha256(password.encode()).hexdigest()
        print("Encrypting password")
        # Save the user data to the database - Table: users - Columns: id, user_type, full_name, username, password
        sql = "INSERT INTO users (rank, full_name, username, password) VALUES (%s, %s, %s, %s)"
        val = (data["rank"], data["fullname"], data["username"], password)
        mycursor.execute(sql, val)
        mydb.commit()
        print("[UNSECURE] User data saved to the database")


    def clear_form(self) -> None:
        fullname = self.frame.fullname_entry.get()
        username = self.frame.username_entry.get()
        password = self.frame.password_entry.get()
        self.frame.fullname_entry.delete(0, len(fullname))
        self.frame.fullname_entry.focus()
        self.frame.username_entry.delete(0, len(username))
        self.frame.password_entry.delete(0, len(password))

        self.frame.has_agreed.set(False)
