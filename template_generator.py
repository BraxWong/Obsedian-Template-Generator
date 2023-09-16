import os
from tkinter import messagebox
import files as f
import json

class templateGenerator():

    def __init__(self, configFile, filePath, ticketNumber, ticketName, config):
        print(config)
        self.filePath = filePath
        self.ticketName = ticketName
        self.ticketNumber = ticketNumber
        self.config = config
        self.configFile = configFile
        if configFile == None:
            self.createDefaultTemplate()
        else:
            self.createCustomTemplate()


# ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
# ┃                                                                              ┃
# ┃       #WARNING: These are blasphemy, both createDefaultTemplate() and        ┃
# ┃createCustomTemplate() have to be refactored. And it all begins with files.py ┃
# ┃                                                                              ┃
# ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

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
        if 'Flow' in data:
            FlowQuantity = data['Flow']
            flow = f.flow(self.filePath)
            flow.createMultipleFiles(FlowQuantity)
        if 'Roadblocks' in data:
            RoadblocksQuantity = data['Roadblocks']
            roadblocks = f.roadblocks(self.filePath)
            roadblocks.createMultipleFiles(RoadblocksQuantity)
        if 'Reminder' in data:
            ReminderQuantity = data['Reminder']
            reminder = f.reminder(self.filePath)
            reminder.createMultipleFiles(ReminderQuantity)
        if 'Requirements' in data:
            RequirementQuantity = data['Requirements']
            requirements = f.requirements(self.ticketNumber, self.ticketName, self.filePath)
            requirements.createMultipleFiles(RequirementQuantity)
        if 'Resources' in data:
            ResourcesQuantity = data['Resources']
            resources = f.resources(self.filePath)
            resources.createMultipleFiles(ResourcesQuantity)
        if 'Visualization' in data:
            VisualizationQuantity = data['Visualization']
            visualization = f.visualization(self.filePath)
            visualization.createMultipleFiles(VisualizationQuantity)


