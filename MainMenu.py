import customtkinter
import pathSelector as gt

class Home(customtkinter.CTk):

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
        print("Coming Soon.")
    

    def generateTemplate(self):
        self.destroy()
        templateGenerator = gt.generator()
        templateGenerator.mainloop()



    
