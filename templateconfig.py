import customtkinter
from tkinter import messagebox

class config(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("1000x1000")
        self.title("Template Configuration")
        self.resizeable(False,False)
        submitButton = customtkinter.CTkButton(self, text = "Submit", command = self.submitTemplate)
        ticketNameLabel = customtkinter.CTkLabel(self, text = "Name of the ticket", font = ("American Typewriter"),25)
        ticketNumberLabel = customtkinter.CTkLabel(self, text = "Number of the ticket", font = ("American Typewriter"),25)
        
    def __init__(self):
        super().__init__()
        self.ticketNumber = ""
        self.ticketName = ""
        self.initializeWidget()

    def submitTemplate(self):
        if self.validateInput() == "TRUE":
            print("YAS QUEEN")
        else
           messagebox.showerror(title = "Inputs not found", message = "Error: One or more inputs not found.")             
           

    def validateInput(self):
        return "TRUE"

    def grid_configurate(self):
       self.grid_rowconfigure(0, weight = 1)
       self.grid_rowconfigure(1, weight = 1)
       self.grid_rowconfigure(2, weight = 1)
       self.grid_rowconfigure(3, weight = 1)
       self.grid_columnconfigure(0, weight = 1)
       self.grid_columnconfigure(1, weight = 1)

        
