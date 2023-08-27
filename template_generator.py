import os
from tkinter import messagebox
import files as f

class templateGenerator():

    def __init__(self, filePath, ticketNumber, ticketName):
        self.filePath = filePath
        self.ticketName = ticketName
        self.ticketNumber = ticketNumber
        self.createTemplate()

    def createTemplate(self):
        self.createFile("md","Flow")
        self.createFile("md","Roadblocks")
        self.createFile("md","Reminder")
        self.createFile("md","Resources")
        self.createFile("md",self.ticketNumber + " - " + self.ticketName + " Requirements")
        self.createFile("canvas","Ticket Visualization")
