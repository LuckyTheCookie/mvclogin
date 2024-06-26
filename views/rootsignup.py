from tkinter import Frame, Label, Entry, Checkbutton, Button, BooleanVar
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class RootSignUpView(Frame):
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

        # create root_signup frame
        self.root_signup_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.root_signup_frame.grid(row=0, column=0, sticky="ns")
        self.root_signup_label = customtkinter.CTkLabel(self.root_signup_frame, text="Create a new account",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.root_signup_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        # Full Name
        self.fullname_entry = customtkinter.CTkEntry(self.root_signup_frame, width=200, placeholder_text="full name")
        self.fullname_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        # Username
        self.username_entry = customtkinter.CTkEntry(self.root_signup_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        # Password
        self.password_entry = customtkinter.CTkEntry(self.root_signup_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))

        # Radio Button Opérateur / Fabricant / Intégrateur
        self.user_type = customtkinter.StringVar()
        self.operator = customtkinter.CTkRadioButton(
            self.root_signup_frame,
            text="Operator",
            variable=self.user_type,
            value="Operator",
            state="normal"
        )
        self.operator.grid(row=4, column=0, padx=30, pady=(0, 0))
        self.manufacturer = customtkinter.CTkRadioButton(
            self.root_signup_frame,
            text="Manufacturer",
            variable=self.user_type,
            value="Manufacturer",
            state="normal"
        )
        self.manufacturer.grid(row=5, column=0, columnspan=3, padx=30, pady=(0, 0))
        self.integrator = customtkinter.CTkRadioButton(
            self.root_signup_frame,
            text="Integrator",
            variable=self.user_type,
            value="Integrator",
            state="normal"
        )
        self.integrator.grid(row=6, column=0, columnspan=3, padx=30, pady=(0, 0))

        self.root_signup_btn = customtkinter.CTkButton(self.root_signup_frame, text="Sign Up")
        self.root_signup_btn.grid(row=8, column=0, padx=0, pady=10)

        self.home_option_label = customtkinter.CTkLabel(self.root_signup_frame, text="Cancel registration?")
        self.home_btn = customtkinter.CTkButton(self.root_signup_frame, text="Cancel")
        self.home_option_label.grid(row=9, column=0)
        self.home_btn.grid(row=10, column=0)


        self.update_state()

    # Désactiver le bouton de root_signup tant que l'utilisateur n'a pas coché la case d'acceptation des conditions et rempli tous les champs
    def check_trace(self, *args):
        if self.fullname_entry.get() and self.username_entry.get() and self.password_entry.get() and self.user_type.get():
            self.root_signup_btn.configure(state="normal")
        else:
            self.root_signup_btn.configure(state="disabled")
            

    def update_state(self):
        # Désactiver le bouton de root_signup tant que l'utilisateur n'a pas coché la case d'acceptation des conditions et rempli tous les champs
        self.root_signup_btn.configure(state="disabled")
        
        # Update the state of the signup button
        self.user_type.trace_add("write", self.check_trace)
        self.fullname_entry.bind("<KeyRelease>", self.check_trace)
        self.username_entry.bind("<KeyRelease>", self.check_trace)
        self.password_entry.bind("<KeyRelease>", self.check_trace)