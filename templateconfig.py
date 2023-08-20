import customtkinter

class config(customtkinter.CTk):

    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("1000x1000")
        self.title("Template Configuration")
        self.resizeable(False,False)

    def __init__(self):
        super().__init__()
        self.initializeWidget()
