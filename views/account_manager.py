from tkinter import Frame, Label, Button

import customtkinter
from PIL import Image
import os
import sqlite3

customtkinter.set_appearance_mode("dark")


class AccountManagerView(Frame):
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

        # create home frame
        self.account_manager_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.account_manager_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.account_manager_frame, text="Manage your Account",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.sorry_label = customtkinter.CTkLabel(self.account_manager_frame, text="Sorry, this feature has been disabled by your administrator")
        self.sorry_label.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        self.home_btn = customtkinter.CTkButton(self.account_manager_frame, text="Go back")
        self.home_btn.grid(row=2, column=0, padx=10, pady=5)