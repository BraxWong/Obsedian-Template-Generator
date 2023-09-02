import customtkinter
import tkinter as tk
from tkinter import messagebox

class template_name(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("500x200")
        self.title("Obsidian Template Name")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text= "Please provide the name of the template", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = (10,0))
        self.TemplateName.insert("0.0","Template Name: ")
        self.TemplateName.grid(row = 1, column = 0, padx = (5,10))

    def __init__(self):
        super().__init__()
        self.TemplateName = customtkinter.CTkTextbox(self, width = 450, height = 50, border_width = 3)
        self.initializeWidget()

    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_configurate(1, weight = 1)
