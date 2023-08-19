import customtkinter
from tkinter.filedialog import askdirectory
class generator(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure((0,1), weight = 1)
        self.geometry("500x200")
        self.title("Template Generator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text="Please choose the target location", font = ("American Typewriter",25))
        titleLabel.grid(row = 1, column = 0, padx = 20, pady = 20)
        directoryButton = customtkinter.CTkButton(self, text = "Choose Location", command = self.chooseLocation)
        directoryButton.grid(row = 3, column = 0, padx = 20, pady = 20)
 

    def __init__(self):
        super().__init__()
        self.initializeWidget()


    def createTemplate(self):
        print("Coming Soon.")
    

    def chooseLocation(self):
        path = askdirectory(title='Select Folder')
