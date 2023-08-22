import customtkinter
from tkinter import messagebox

class config(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("1000x1000")
        self.title("Template Configuration")
        self.resizeable(False,False)
        submitButton = customtkinter.CTkButton(self, text = "Submit", command = self.submitTemplate)

    def __init__(self):
        super().__init__()
        self.initializeWidget()

    def submitTemplate(self):
        if self.validateInput() == "TRUE":
            print("YAS QUEEN")
        else
           messagebox.showerror(title = "Inputs not found", message = "Error: One or more inputs not found.")             
           

    def validateInput(self):
        return "TRUE"


        
