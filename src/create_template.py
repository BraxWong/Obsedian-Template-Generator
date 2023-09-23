import customtkinter
from tkinter import messagebox
import JsonConverter
import FileNQuantity

class template_creator(customtkinter.CTk):

#                       ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#                       ┃                                 ┃
#                       ┃ template_creator Documentations ┃
#                       ┃                                 ┃
#                       ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

    """
    template_creator is a class that is used to give the user the option to choose what and how many 
    to be included in the obsidian vault template.

    Attributes
    ────────────────────────────────────────────────────────────

    optionmenu : customtkinter.CTkOptionMenu
        The item to be included in the obsidian vault template

    quantitymenu : customtkinter.CTkOptionMenu
        The amount of that item to be included in the obsidian vault template

    template_name : str
        The name of the obsidian vault template

    counter : int 
       Counter to make sure the tops message box does not display twice

    list_of_files : list
       a list of FileNQuantity item to be used for the Json object 

    initializeWidget()
        Just like any other classes in this program, it is used to initialize all the widgets in that page.
        It will call grid_configurate() to set up the grid, create a CTkLabel and two CTkButtons. When the startButton
        is clicked, it will call the ConvertJson() method. When the moreFiles button is clicked, it will call
        the AddFiles() method.

    grid_configurate()
        Just like any other classes in this program, it will configurate the grid system for this page.

    ConvertJson()
       This method will create a jsonConverter object by passing in the list_of_files, the template target path,
       and the name of the template. The write_to_file() method will be called to create the Json object using 
       the list_of_files list.

    AddFiles()
        This method will append the value of optionmenu and quantitymenu into a FileNQuantity object. This object
        will then be appended to the list_of_files list.
    """

   
    def initializeWidget(self):
        self.grid_configurate()
        self.geometry("500x200")
        self.title("Obsidian Template Creator")
        self.resizable(False,False)
        titleLabel = customtkinter.CTkLabel(self,text= "Template Creator", font = ("American Typewriter",25))
        titleLabel.grid(row = 0, column = 0, columnspan = 2, pady = (10,0))
        startButton = customtkinter.CTkButton(self, text = "Generate Template", command = self.ConvertJson)
        startButton.grid(row = 2, column = 0, padx = 20, pady = 10, sticky = "w")
        moreFiles = customtkinter.CTkButton(self, text = "More Files", command = self.AddFiles)
        moreFiles.grid(row = 2, column = 1, padx = 20, pady = 10, sticky = "e")
        self.optionmenu.grid(row = 1, column = 0, padx = 20, pady = 5, sticky = "w")
        self.quantitymenu.grid(row = 1, column = 1, padx = 20, pady = 5, sticky = "e")
         
    def __init__(self, template_name, path):
        super().__init__()
        self.path = path
        self.optionmenu = customtkinter.CTkOptionMenu(self, values=["Select Option","Flow","Roadblocks","Reminder","Resources","Requirements","Visualization","Others"])
        self.quantitymenu = customtkinter.CTkOptionMenu(self, values=["Select Quantity","1","2","3","4","5","Other"])
        self.list_of_files = []
        self.counter = '0'
        self.template_name = template_name
        print(self.template_name)
        self.initializeWidget()

    def grid_configurate(self):
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_rowconfigure(2, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        
    def ConvertJson(self):
        json = JsonConverter.json_converter(self.list_of_files, self.path, self.template_name) 
        json.write_to_file()
        self.destroy()

    def AddFiles(self):
        if self.optionmenu.get() == "Select Option" or self.quantitymenu.get() == "Select Option":
            messagebox.showerror(title = "Input Error", message = "Error: Please select the file type and the quantity") 
        else:
            self.list_of_files.append(FileNQuantity.FileTypeNQuantity(self.optionmenu.get(),self.quantitymenu.get())) 
            self.optionmenu.set("Select Option")
            self.quantitymenu.set("Select Quantity")
            if self.counter == '0':
                self.counter = '1'
                messagebox.showinfo(title = "Item added", message = "Item added. Please press Generate Template if you do not require more files in your template.")
        

