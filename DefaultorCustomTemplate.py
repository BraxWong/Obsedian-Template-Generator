import customtkinter
import pathSelector
import tkinter
class ChooseTemplate(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("500x200")
        self.title("Choose Your Template")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Choose Your Template", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, padx = 20, pady = 20)
        self.DefaultTemplate.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "w") 
        self.CustomTemplate.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = "e")
        continueButton = customtkinter.CTkButton(self, text = "Continue", command = self.checkTemplateOption)
        continueButton.grid(row = 2, column = 0, columnspan = 2, sticky = "nsew", pady = (30,0))
 
 
    def __init__(self):
        super().__init__()
        self.radio_var = tkinter.IntVar(value= 0 )
        self.DefaultTemplate = customtkinter.CTkRadioButton(self, text = "Default Template",variable = self.radio_var, value = 1)
        self.CustomTemplate = customtkinter.CTkRadioButton(self, text = "Custom Template",variable = self.radio_var, value = 2)
        self.initializeWidget()

    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

    def checkTemplateOption(self):
        templateGenerator = pathSelector.generator()
        templateGenerator.mainloop()
