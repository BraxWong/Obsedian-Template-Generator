import os
from tkinter import messagebox

class templateGenerator():

    def __init__(self, filePath, ticketNumber, ticketName):
        self.filePath = filePath
        self.ticketName = ticketName
        self.ticketNumber = ticketNumber
        self.createTemplate()


    def createFile(self, fileType, fileName):
        if os.path.exists(self.filePath + "/" + fileName + "." + fileType): 
           messagebox.showerror(title = "File exists", message = "Error: This file already exists.") 
        else:
            f = open(self.filePath + "/" + fileName + "." + fileType, "x")

    def createTemplate(self):
        self.createFile("md","Flow")
        self.createFile("md","Roadblocks")
        self.createFile("md","Reminder")
        self.createFile("md","Resources")
        self.createFile("md",self.ticketNumber + " - " + self.ticketName + " Requirements")
        self.createFile("canvas","Ticket Visualization")
