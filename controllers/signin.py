from models.main import Model
from models.auth import User
from views.main import View


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
        self.frame.password_entry.delete(0, len(password))
        user: User = {"username": data["username"]}
        self.model.auth.login(user)
