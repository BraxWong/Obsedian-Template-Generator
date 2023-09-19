import random_seed_generator
import os
from tkinter import messagebox

# ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
# ┃                                                                              ┃
# ┃    #NOTE: markdown should be the only class here. The other classes will     ┃
# ┃                        not be needed down the roadb.                         ┃
# ┃                                                                              ┃
# ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

# ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
# ┃                                                                              ┃
# ┃    #TODO: Refactor markdown to create any type of files except for canva     ┃
# ┃                               and media types.                               ┃
# ┃                                                                              ┃
# ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

class markdown():

#                           ╭━━━━━━━━━━━━━━━━━━━━━━━━━╮
#                           ┃                         ┃
#                           ┃ Markdown Documentations ┃
#                           ┃                         ┃
#                           ╰━━━━━━━━━━━━━━━━━━━━━━━━━╯

    """
    markdown is a class that represents the items in an obsidian vault 

    Attributes
    ────────────────────────────────────────────────────────────

    seed : str 
        Represents the seed a file possesses. It is generated using generator() method
        from SeedGenerator class.

    fileType : str 
        Represents the file type of a file. It can be a markdown file, it can
        be a canva file, it can even be a mp4 file.

    fileName : str
        Represents the name of the file.

    filePath : str 
        Represents the file path to the file.

    Methods
    ────────────────────────────────────────────────────────────

    createFile()
        This method will first check whether the file already exists in the designated directory, if so,
        it will display a message box showing the error message. Else, it will create the file in the 
        designated directory.

    createMultipleFiles()
        This method will identify the amount of files it needs to generate. It will then enter a while loop,
        If the file already exists in the directory, it will display a message box showing the error message.
        Else, it will create the file with the desire quantity, in the designated directory.
        
    """


    def __init__(self, filePath):
        rgen = random_seed_generator.SeedGenerator()
        self.seed = rgen.generator()
        self.fileType = ""
        self.fileName = ""
        self.filePath = filePath

    def createFile(self):
        if os.path.exists(self.filePath + "/" + self.fileName + "." + self.fileType): 
            messagebox.showerror(title = "File exists", message = "Error: " + self.fileName + "." + self.fileType + " already exists." ) 
        else:
            open(self.filePath + "/" + self.fileName + "." + self.fileType, "x")

    def createMultipleFiles(self, quantity):
        index = 0
        quantity = int(quantity)
        while index != quantity:
            if os.path.exists(self.filePath + "/" + self.fileName + str(index + 1) + "." + self.fileType): 
                messagebox.showerror(title = "File exists", message = "Error: " + self.fileName + "." + self.fileType + " already exists." ) 
            else:
                open(self.filePath + "/" + self.fileName + str(index+1) +  "." + self.fileType, "x")
            index += 1


# ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
# ┃                                                                              ┃
# ┃    From this point on to potentially visualization, these will eventually    ┃
# ┃                                not be needed.                                ┃
# ┃                                                                              ┃
# ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

class flow(markdown):

    def __init__(self, filePath):
        super().__init__(filePath)
        self.fileType = "md"
        self.fileName = "Flow"

    def printSeed(self):
        print(self.seed)

    
class roadblocks(markdown):

    def __init__(self, filePath):
        super().__init__(filePath)
        self.fileType = "md"
        self.fileName = "Roadblocks"

    def printSeed(self):
        print(self.seed)


class reminder(markdown):

    def __init__(self, filePath):
        super().__init__(filePath)
        self.fileType = "md"
        self.fileName = "Reminder"

    def printSeed(self):
        print(self.seed)


class resources(markdown):

    def __init__(self, filePath):
        super().__init__(filePath)
        self.fileType = "md"
        self.fileName = "Resources"

    def printSeed(self):
        print(self.seed)


class requirements(markdown):

    def __init__(self, ticketNumber, ticketName, filePath):
        super().__init__(filePath)
        self.fileType = "md"
        self.fileName = ticketNumber + " - " + ticketName + " Requirements" 

    def printSeed(self):
        print(self.seed)

class visualization(markdown):

    def __init__(self, filePath):
        super().__init__(filePath)
        self.fileType = "canva"
        self.fileName = "Ticket Visualization"

    def printSeed(self):
        print(self.seed)


