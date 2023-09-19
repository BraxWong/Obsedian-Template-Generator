import customtkinter
import os
import templateconfig as tc
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

#TODO: Figure out a way to allow users to select their template config file from here.
#NOTE: Maybe set a variable when creating a pathSelector object to trigger another tersion of initializeWidget
class generator(customtkinter.CTk):

    """
    generator is a class that allows users to choose the target path for their obsidian vault template,
    or obsidian vault path.

    Attributes
    ────────────────────────────────────────────────────────────

    config : str
        This decides whether the user wants to generate a default obsidian vault or a obsidian vault using a custom
        template

    config_path : str
        This represents the target path to the obsidian vault custom template

    directoryTextBox : customtkinter.CTkTextbox
        This represents the text box object on screen that displays the target path to the desired item.

    path : str
        The represents the target path to the obsidian vault

    Methods
    ────────────────────────────────────────────────────────────
    
    initializeWidget()
        Just like any other classes in this program, it is used to initialize all the widgets in that page.
        It will call grid_configurate() to set up the grid, create a CTkLabel and two CTkButtons. When the directoryButton
        is clicked, it will call the chooseLocation() method. When the continueButton is clicked, it will call
        the directoryCheck() method.

    grid_configurate()
        Just like any other classes in this program, it will configurate the grid system for this page.

    chooseLocation()
       This method will display a file explorer type of window to allow users to pick the target path to their desired items.
       When the path is picked, the location will be shown on the directoryTextBox.

    directoryCheck()
        This method will first check whether the path provided is valid. If not, a message box will be displayed showing the error.
        Else, if the config value is equal to "Default", it will take the user to the templateConfig page. If the config value is equal
        to "Custom", it will take the user to templateGenerator page. 

    """

    def DefaultInitializeWidget(self):
        self.grid_configurate()
        self.geometry("600x300")
        self.title("Template Generator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Choose the target location", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        directoryButton = customtkinter.CTkButton(self, text = "Choose Location", command = self.chooseLocation)
        directoryButton.grid(row = 1, column = 0, padx = (10,5))
        continueButton = customtkinter.CTkButton(self, text = "Continue", command = self.directoryCheck)
        continueButton.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew", pady = (30,0))
        self.directoryTextBox.insert("0.0","directory: ")
        self.directoryTextBox.grid(row = 1, column = 1, padx = (5,10))

    def CustomInitializeWidget(self):
        self.grid_configurate()
        self.geometry("600x300")
        self.title("Template Generator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Select your template", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, sticky = "nsew")
        directoryButton = customtkinter.CTkButton(self, text = "Choose Location", command = self.chooseLocation)
        directoryButton.grid(row = 1, column = 0, padx = (10,5))
        continueButton = customtkinter.CTkButton(self, text = "Continue", command = self.directoryCheck)
        continueButton.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew", pady = (30,0))
        self.directoryTextBox.insert("0.0","directory: ")
        self.directoryTextBox.grid(row = 1, column = 1, padx = (5,10))

    def __init__(self, config, config_path):
        super().__init__()
        self.config = config 
        self.config_path = config_path
        self.directoryTextBox = customtkinter.CTkTextbox(self, width = 450, height = 50, border_width = 3)
        self.path = "";
        if config == "Default":
            self.DefaultInitializeWidget()
        else:
            self.CustomInitializeWidget()

       
    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        

    def chooseLocation(self):
        if self.config == "Default":
            self.path = askdirectory(title='Select Directory')
            self.directoryTextBox.delete("0.0","end")
            self.directoryTextBox.insert("0.0","directory: " + self.path)
        else:
            self.config_path = askopenfilename(title="Select Configuration File")
            self.directoryTextBox.delete("0.0","end")
            self.directoryTextBox.insert("0.0","directory: " + self.config_path)

    def directoryCheck(self):
        if self.config == "Default":
            if not os.path.isdir(self.path):
                messagebox.showerror(title = "Directory not found", message = "Error: Directory is either not found or no longer exists.")
            else:
                self.destroy()
                templateConfig = tc.config(self.path, self.config, self.config_path)
                templateConfig.mainloop()
        else:
            if self.config_path[-5:] != ".json":
                messagebox.showerror(title = "Template Configuration Not Found", message = "Error: Template configuration file is either not found or no longer exists.")
            else:
                self.destroy()
                templateGenerator = generator("Default",self.config_path)
                templateGenerator.mainloop()



