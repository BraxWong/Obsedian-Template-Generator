import customtkinter
import tkinter as tk
from tkinter import messagebox
import create_template
from pathvalidate import is_valid_filename, sanitize_filename

class template_name(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("600x300")
        self.title("Obsidian Template Name")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text= "Please provide the name of the template", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2,padx = (10,0), pady = (10,0), sticky = "nsew")
        submit = customtkinter.CTkButton(self,text = "Next", command = self.create_template)
        submit.grid(row = 1, column = 1, padx = (5,10))
        self.TemplateName.grid(row = 1, column = 0, padx = (5,10))

    def __init__(self):
        super().__init__()
        self.TemplateName = customtkinter.CTkTextbox(self, width = 450, height = 50, border_width = 3)
        self.initializeWidget()

    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

    def create_template(self):
        templatename = self.TemplateName.get("1.0","end-1c")
        if not is_valid_filename(templatename):
            templatename = sanitize_filename(templatename)
            messagebox.showinfo(title = "Illegal template name", message = "Notice: The template name you provided is not a legal file name. Your template name has been changed to: " + templatename)
        templatename = templatename.strip()
        if self.TemplateName != 0:
            self.destroy()
            template = create_template.template_creator(templatename)
            template.mainloop()
        else:
            messagebox.showerror(title = "Input Errors", message = "Error: Template Name cannot be empty.")
