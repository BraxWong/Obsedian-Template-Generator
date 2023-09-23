import customtkinter
import ConfigName
import DefaultorCustomTemplate
import pathSelector

class Home(customtkinter.CTk):

#                             ╭━━━━━━━━━━━━━━━━━━━━━╮
#                             ┃                     ┃
#                             ┃ Home Documentations ┃
#                             ┃                     ┃
#                             ╰━━━━━━━━━━━━━━━━━━━━━╯

    """
    Home is a class that is used to the user options to either generate an obsidian vault template,
    or generate an obsidian vault.

    Attributes
    ────────────────────────────────────────────────────────────

    initializeWidget()
        Just like any other classes in this program, it is used to initialize all the widgets in that page.
        It will call grid_configurate() to set up the grid, create a CTkLabel and two CTkButtons. When the startButton
        is clicked, it will call the generateTemplate() method. When the newAccountButton is clicked, it will call
        the createTemplate() method.

    grid_configurate()
        Just like any other classes in this program, it will configurate the grid system for this page.

    generateTemplate()
       This method will create a ChooseTemplate object and call the mainloop method.  

    createTemplate()
        This method will create a template_name object and call the mainloop method.
         
    """

    def initializeWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.geometry("500x200")
        self.title("Obsidian Template Generator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Obsidian Template Generator", font = ("American Typewriter",25))
        titleLabel.grid(row = 1, column = 0, padx = 20, pady = 20)
        startButton = customtkinter.CTkButton(self, text = "Generate Template", command = self.generateTemplate)
        startButton.grid(row = 3, column = 0, padx = 20, pady = 20)
        newAccountButton = customtkinter.CTkButton(self,text = "Create New Template", command = self.createTemplate)
        newAccountButton.grid(row = 2, column = 0, padx = 10, pady = 10)
    

    def __init__(self):
        super().__init__()
        self.initializeWidget()


    def createTemplate(self):
        self.destroy()
        configPath = pathSelector.generator("CreateTemplate",None)
        configPath.mainloop()

    def generateTemplate(self):
        self.destroy()
        TemplateGenerate = DefaultorCustomTemplate.ChooseTemplate()
        TemplateGenerate.mainloop()



    
