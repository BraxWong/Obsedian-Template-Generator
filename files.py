import random_seed_generator

class markdown():

    def __init__(self, filePath):
        rgen = random_seed_generator.SeedGenerator()
        self.seed = rgen.generator()
        self.fileType = ""
        self.fileName = ""
        self.filePath = filePath

    def createFile(self):
        if os.path.exists(self.filePath + "/" + self.fileName + "." + self.fileType): 
           messagebox.showerror(title = "File exists", message = "Error: This file already exists.") 
        else:
            f = open(self.filePath + "/" + self.fileName + "." + self.fileType, "x")



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
        self.ticketNumber = ticketNumber
        self.tickerName = ticketName
        self.fileName = self.ticketNumber + " - " + self.ticketName + " Requirements" 

    def printSeed(self):
        print(self.seed)




