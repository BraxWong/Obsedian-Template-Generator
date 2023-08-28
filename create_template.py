import customtkinter

class template_creator(customtkinter.CTk):
    
    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("500x200")
        self.title("Obsidian Template Creator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text= "Template Creator", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = "nsew")
        startButton = customtkinter.CTkButton(self, text = "Generate Template", command = self.generateTemplate)
        startButton.grid(row = 2, column = 0, padx = (90,5), pady = (20,0))
        moreFiles = customtkinter.CTkButton(self, text = "More Files", command = self.generateTemplate)
        moreFiles.grid(row = 2, column = 1, padx = (10,5), pady = (20,0), sticky = "ew")
        self.optionmenu.grid(row = 1, column = 0, padx = (10,5), pady = (5,0), sticky = "ew")
        self.quantitymenu.grid(row = 1, column = 1, padx = (5,20), pady = (4,0), sticky = "ew")
         
    def __init__(self):
        super().__init__()
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Flow","Roadblocks","Reminder","Resources","Requirements","Visualization","Others"])
        self.quantitymenu = customtkinter.CTkOptionMenu(self, values=["1","2","3","4","5","Other"])
        self.initializeWidget()

    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_columnconfigure(3, weight = 1)
        self.grid_columnconfigure(4, weight = 1)
        
        
    def generateTemplate(self):
        print("SOON")


