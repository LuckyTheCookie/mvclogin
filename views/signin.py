from tkinter import Frame, Label, Entry, Button
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class SignInView(Frame):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "../../background/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Sign In with existing account",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))


        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        self.signup_option_label = customtkinter.CTkLabel(self.login_frame, text="Don't have an account?")
        self.signup_btn = customtkinter.CTkButton(self.login_frame, text="Sign Up")
        self.signup_option_label.grid(row=4, column=0, padx=10, pady=(15, 15))
        self.signup_btn.grid(row=5, column=0, padx=20)
