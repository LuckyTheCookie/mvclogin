from tkinter import Tk
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class Root(customtkinter.CTk):
    width = 900
    height = 600
    
    def __init__(self):
        super().__init__()

        self.title("MVC Login System")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)