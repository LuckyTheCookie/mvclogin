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

print("[UNSECURE] Connecting to the database")
if mydb.is_connected():
    print("[UNSECURE] Connection established")
else:
    print("[UNSECURE] Connection failed")



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
        password = hashlib.sha256(password.encode()).hexdigest()
        print("Encrypting password")
        # Check if the user exists in the database
        sql = "SELECT * FROM users WHERE username = %s AND password = %s"
        val = (data["username"], password)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        if result:
            print("User exists in the database")
            self.frame.password_entry.delete(0, len(password))
            user: User = {"username": data["username"]}
            self.model.auth.login(user)
        else:
            print("User does not exist in the database")




        
