from models.main import Model
from views.main import View
import sqlite3
from .otpconfig import OtpController


class TeachJobsController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["teachjobs"]
        self._bind()

    def _bind(self) -> None:
        """Binds controller functions with respective buttons in the view"""
        # self.frame.signout_btn.configure(command=self.logout)
        
    