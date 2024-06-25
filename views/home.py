from tkinter import Frame, Label, Button

import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class HomeView(Frame):
    width = 900
    height = 600


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "../../test_images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create home frame
        self.greeting_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.greeting_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.greeting_frame, text="Home",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.greeting = customtkinter.CTkLabel(self.greeting_frame, text="")
        self.greeting.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.signout_btn = customtkinter.CTkButton(self.greeting_frame, text="Sign Out")
        self.signout_btn.grid(row=3, column=0, padx=10, pady=10)
