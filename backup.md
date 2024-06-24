class SignInView(customtkinter.CTkFrame):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "../../test_images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))

        self.header = customtkinter.CTkLabel(self, text="Sign In with existing account")
        self.header.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.username_label = customtkinter.CTkLabel(self, text="Username")
        self.username_input = customtkinter.CTkEntry(self)
        self.username_label.grid(row=1, column=0, padx=10, sticky="w")
        self.username_input.grid(row=1, column=1, padx=(0, 20), sticky="ew")

        self.password_label = customtkinter.CTkLabel(self, text="Password")
        self.password_input = customtkinter.CTkEntry(self, show="*")
        self.password_label.grid(row=2, column=0, padx=10, sticky="w")
        self.password_input.grid(row=2, column=1, padx=(0, 20), sticky="ew")

        self.signin_btn = customtkinter.CTkButton(self, text="Sign In")
        self.signin_btn.grid(row=3, column=1, padx=0, pady=10, sticky="w")

        self.signup_option_label = customtkinter.CTkLabel(self, text="Don't have an account?")
        self.signup_btn = customtkinter.CTkButton(self, text="Sign Up")
        self.signup_option_label.grid(row=4, column=1, sticky="w")
        self.signup_btn.grid(row=5, column=1, sticky="w")