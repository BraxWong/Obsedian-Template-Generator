import customtkinter
import tkinter as tk
from tkinter import messagebox
import JsonConverter
import FileNQuantity
import pathSelector

class template_creator(customtkinter.CTk):
    
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
         
    def __init__(self, template_name):
        super().__init__()
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
        json = JsonConverter.json_converter(self.list_of_files, "template", self.template_name) 
        json.write_to_file()

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
        

