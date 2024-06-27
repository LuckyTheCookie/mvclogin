import customtkinter
from tkinter import Frame
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("light")

class TeachJobsView(Frame):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(bg="white")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        # Top bar frame
        self.top_bar = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#404B50")
        self.top_bar.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Top bar components
        self.hand_icon = customtkinter.CTkButton(self.top_bar, text="✋", width=30, border_width=2, fg_color="#00B4CD")
        self.hand_icon.pack(side="left", padx=5, pady=5)

        self.battery_icon = customtkinter.CTkButton(self.top_bar, text="🪫", width=30, border_width=2, fg_color="#00B4CD")
        self.battery_icon.pack(side="left", padx=5, pady=5)

        self.plus_plus_button = customtkinter.CTkButton(self.top_bar, text="++", width=30, fg_color="#00B4CD")
        self.plus_plus_button.pack(side="right", padx=5, pady=5)
        
        self.plus_button = customtkinter.CTkButton(self.top_bar, text="+", width=30, fg_color="#00B4CD")
        self.plus_button.pack(side="right", padx=5, pady=5)
        
        self.speed_label = customtkinter.CTkLabel(self.top_bar, text="⚡ 100", text_color="white")
        self.speed_label.pack(side="right", padx=10, pady=10)

        self.minus_button = customtkinter.CTkButton(self.top_bar, text="-", width=30, fg_color="#00B4CD")
        self.minus_button.pack(side="right", padx=5, pady=5)

        self.minus_minus_button = customtkinter.CTkButton(self.top_bar, text="- -", width=30, fg_color="#00B4CD")
        self.minus_minus_button.pack(side="right", padx=5, pady=5)

        self.robot_icon = customtkinter.CTkButton(self.top_bar, text="🤖", width=30, fg_color="#00B4CD")
        self.robot_icon.pack(side="right", padx=5, pady=5)

        # Left sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#404B50")
        self.sidebar_frame.grid(row=1, column=0, rowspan=5, sticky="nsew")

        # Main content frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="#E8E8E8")
        self.main_frame.grid(row=1, column=1, sticky="nsew")

        # Sidebar content
        self.sidebar_label = customtkinter.CTkLabel(self.sidebar_frame, text="NOM_DU_PROGRAMME", anchor="w")
        self.sidebar_label.grid(row=0, column=0, padx=10, pady=10)

        # Load icons
        # current_path = os.path.dirname(os.path.realpath(__file__))
        # icons = [ImageTk.PhotoImage(Image.open(os.path.join(current_path, f"icon{i+1}.png")).resize((20, 20))) for i in range(5)]

        # Define the buttons in the sidebar
        # buttons = [
        #     ("NŒUD MÉTIER 1", True, icons[0]),
        #     ("NŒUD MÉTIER 2", True, icons[1]),
        #     ("NŒUD MÉTIER 3", True, icons[2]),
        #     ("NŒUD MÉTIER 4", True, icons[3]),
        #     ("NŒUD MÉTIER 5", True, icons[4])
        # ]

        # Create the buttons in the sidebar
        # for i, (text, active, icon) in enumerate(buttons):
        #     button = customtkinter.CTkButton(sidebar_frame, text=text, image=icon, compound="left", state="normal", border_width=2)
        #     button.grid(row=i+1, column=0, padx=10, pady=10, sticky="ew")

        # Define the buttons in the sidebar
        buttons = [
            ("⚡ NŒUD MÉTIER 1"),
            ("❓NŒUD MÉTIER 2"),
            ("❓NŒUD MÉTIER 3"),
            ("❓NŒUD MÉTIER 4"),
            ("❓NŒUD MÉTIER 5")
        ]


        # Create the buttons in the sidebar
        for i, (text) in enumerate(buttons):
            button = customtkinter.CTkButton(self.sidebar_frame, text=text, fg_color="#00B4CD", corner_radius=10)
            button.grid(row=i+1, column=0, padx=10, pady=10, sticky="ew")

        # Main content area
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="NŒUD MÉTIER 1", font=customtkinter.CTkFont(size=24))
        self.main_label.pack(pady=20)

        # Grid layout in the main content area
        self.grid_frame = customtkinter.CTkFrame(self.main_frame, fg_color="#404B50")
        self.grid_frame.pack(pady=30, padx=50)

        for row in range(2):
            for col in range(4):
                cell = customtkinter.CTkFrame(self.grid_frame, width=100, height=100, fg_color="#F5F5F5")
                cell.grid(row=row, column=col, padx=5, pady=5)


