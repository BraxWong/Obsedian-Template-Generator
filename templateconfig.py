import customtkinter
from tkinter import messagebox

class config(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("1000x500")
        self.title("Template Configuration")
        self.resizable(False,False)
        title = customtkinter.CTkLabel(self, text = "Template Configuration", font = ("American Typewriter",25))
        title.grid(row = 0, column = 0, sticky = "nsew")
        submitButton = customtkinter.CTkButton(self, text = "Submit", command = self.submitTemplate)
        ticketNameLabel = customtkinter.CTkLabel(self, text = "Name of the ticket", font = ("American Typewriter",25))
        ticketNameLabel.grid(row = 1, column = 0)
        ticketName = customtkinter,CTkTextbox(master = self, height = 20, width = 20)
        ticketName.grid(row = 1, column = 1)
        ticketNumberLabel = customtkinter.CTkLabel(self, text = "Number of the ticket", font = ("American Typewriter",25))
        ticketNumberLabel.grid(row = 2, column = 1)
        ticketNumber = customtkinter.CTkTextbox(master = self, height = 50, width = 450)
        ticketNumber.grid(row = 2, column = 0)
         
    def __init__(self):
        super().__init__()
        self.ticketNumber = ""
        self.ticketName = ""
        self.initializeWidget()

    def submitTemplate(self):
        if self.validateInput() == "TRUE":
            print("YAS QUEEN")
        else:
           messagebox.showerror(title = "Inputs not found", message = "Error: One or more inputs not found.")             
           

    def validateInput(self):
        return "TRUE"

    def grid_configurate(self):
       self.grid_rowconfigure(0, weight = 1)
       self.grid_rowconfigure(1, weight = 1)
       self.grid_rowconfigure(2, weight = 1)
       self.grid_columnconfigure(0, weight = 1)
       self.grid_columnconfigure(1, weight = 1)
       

        
