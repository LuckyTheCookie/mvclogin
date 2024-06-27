from typing import TypedDict

from .root import Root
from .home import HomeView
from .signin import SignInView
from .signup import SignUpView
from .rootsignup import RootSignUpView
from .otpconfig import OtpConfigView
from .teachjobs import TeachJobsView



class Frames(TypedDict):
    signup: SignUpView
    signin: SignInView
    home: HomeView
    rootsignup: RootSignUpView


class View:
    def __init__(self):
        self.root = Root()
        self.frames: Frames = {}  # type: ignore

        self._add_frame(SignUpView, "signup")
        self._add_frame(RootSignUpView, "rootsignup")
        self._add_frame(SignInView, "signin")
        self._add_frame(HomeView, "home")
        self._add_frame(OtpConfigView, "otpconfig")
        self._add_frame(TeachJobsView, "teachjobs")

    def _add_frame(self, Frame, name: str) -> None:
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str) -> None:
        frame = self.frames[name]
        frame.tkraise()

    def start_mainloop(self) -> None:
        self.root.mainloop()
