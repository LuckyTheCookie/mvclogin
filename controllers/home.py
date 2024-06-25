from models.main import Model
from views.main import View
import sqlite3


class HomeController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["home"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.signout_btn.configure(command=self.logout)

    def logout(self) -> None:
        self.model.auth.logout()

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