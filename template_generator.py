import os
from tkinter import messagebox
import files as f
import json

class templateGenerator():

    def __init__(self, configFile, filePath, ticketNumber, ticketName, config):
        self.filePath = filePath
        self.ticketName = ticketName
        self.ticketNumber = ticketNumber
        self.config = config
        self.configFile = configFile
        if self.config == "Default":
            self.createDefaultTemplate()
        else:
            self.createCustomTemplate()

    def createDefaultTemplate(self):
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

    def createCustomTemplate(self):
        with open(self.configFile,'r') as k:
            data = json.load(k)
        FlowQuantity = data['Flow']
        flow = f.flow(self.filePath)
        flow.createFile(FlowQuantity)
        RoadblocksQuantity = data['Roadblocks']
        roadblocks = f.roadblocks(self.filePath)
        roadblocks.createFile(RoadblocksQuantity)
        ReminderQuantity = data['Reminder']
        reminder = f.reminder(self.filePath)
        reminder.createFile(ReminderQuantity)
        RequirementQuantity = data['Requirements']
        requirements = f.requirements(self.ticketNumber, self.ticketName, self.filePath)
        requirements.createFile(RequirementQuantity)
        ResourcesQuantity = data['Resources']
        resources = f.resources(self.filePath)
        resources.createFile(ResourcesQuantity)
        VisualizationQuantity = data['Visualization']
        visualization = f.visualization(self.filePath)
        visualization.createFile(VisualizationQuantity)


