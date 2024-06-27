from models.main import Model
from views.main import View
import sqlite3
from .otpconfig import OtpController


class AccountManagerController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["accountmanager"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        self.frame.home_btn.configure(command=self.home)

    def home(self) -> None:
        self.view.switch("home")