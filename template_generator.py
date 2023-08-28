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
        flow = f.flow(self.filePath)
        flow.createFile()
        roadblocks = f.roadblocks(self.filePath)
        roadblocks.createFile()
        reminder = f.reminder(self.filePath)
        reminder.createFile()
        resources = f.resources(self.filePath)
        resources.createFile()
        requirements = f.requirements(self.ticketNumber, self.ticketName, self.filePath)
        requirements.createFile()
        visualization = f.visualization(self.filePath)
        visualization.createFile()
