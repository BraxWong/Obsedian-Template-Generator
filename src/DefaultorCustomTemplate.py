import customtkinter
import pathSelector
import tkinter
class ChooseTemplate(customtkinter.CTk):

#                        ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#                        ┃                               ┃
#                        ┃ ChooseTemplate Documentation  ┃
#                        ┃                               ┃
#                        ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

    """
    ChooseTemplate is a class that is used to give users the ability to whether generate a default obsidian vault, or a custom 
    template made by the user.

    Attributes
    ────────────────────────────────────────────────────────────

    radio_var : tkinter.IntVar
        It indicates the value of the radio buttons that posses this object.

    initializeWidget()
        Just like any other classes in this program, it is used to initialize all the widgets in that page.
        It will call grid_configurate() to set up the grid, create a CTkLabel and CTkButton. When the CTkButton
        is clicked, it will call checkTemplateOption().

    grid_configurate()
        Just like any other classes in this program, it will configurate the grid system for this page.

    checkTemplateOption()
        When the CTkButton is clicked, it will check the radio_var object. If the radio_var's value is 1, that
        indicates the Default radio button has been selected. It will create the generator object and passing in 
        the string "Default". Else, it will still create the generator object but passing in the string "Custom" instead.
        After that, the mainloop method will be called for the generator object.

    """

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
        self.destroy()
        if self.radio_var.get() == 1:
            templateGenerator = pathSelector.generator("Default",None)
        else:
            templateGenerator = pathSelector.generator("Custom",None)
        templateGenerator.mainloop()
