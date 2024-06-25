from tkinter import Frame, Label, Entry, Checkbutton, Button, BooleanVar
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class SignUpView(Frame):
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

        # create signup frame
        self.signup_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.signup_frame.grid(row=0, column=0, sticky="ns")
        self.signup_label = customtkinter.CTkLabel(self.signup_frame, text="Create a new account",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.signup_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        # Full Name
        self.fullname_entry = customtkinter.CTkEntry(self.signup_frame, width=200, placeholder_text="full name")
        self.fullname_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        # Username
        self.username_entry = customtkinter.CTkEntry(self.signup_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        # Password
        self.password_entry = customtkinter.CTkEntry(self.signup_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=3, column=0, padx=30, pady=(0, 15))

        # Agreement
        self.has_agreed = BooleanVar()
        self.agreement = customtkinter.CTkCheckBox(
            self.signup_frame,
            text="I've agreed to the Terms & Conditions",
            variable=self.has_agreed,
            onvalue=True,
            offvalue=False,
        )
        self.agreement.grid(row=4, column=0, padx=30, pady=(0, 15))

        self.signup_btn = customtkinter.CTkButton(self.signup_frame, text="Sign Up")
        self.signup_btn.grid(row=5, column=0, padx=0, pady=10)

        self.signin_option_label = Label(self, text="Already have an account?")
        self.signin_btn = customtkinter.CTkButton(self, text="Sign In")
        self.signin_option_label.grid(row=6, column=0)
        self.signin_btn.grid(row=7, column=0)

        self.update_state()

    # Désactiver le bouton de signup tant que l'utilisateur n'a pas coché la case d'acceptation des conditions et rempli tous les champs
    def check_trace(self, *args):
        if self.has_agreed.get() and self.fullname_entry.get() and self.username_entry.get() and self.password_entry.get():
            self.signup_btn.configure(state="normal")
        else:
            self.signup_btn.configure(state="disabled")
            

    def update_state(self):
        # Désactiver le bouton de signup tant que l'utilisateur n'a pas coché la case d'acceptation des conditions et rempli tous les champs
        self.signup_btn.configure(state="disabled")
        
        # Update the state of the signup button
        self.has_agreed.trace_add("write", self.check_trace)
        self.fullname_entry.bind("<KeyRelease>", self.check_trace)
        self.username_entry.bind("<KeyRelease>", self.check_trace)
        self.password_entry.bind("<KeyRelease>", self.check_trace)






        


