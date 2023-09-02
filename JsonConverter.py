import os

class json_converter():

    def __init__(self, array, filePath):
        self.array = array
        self.filePath = filePath

    def write_to_file(self):
        if os.path.exists(filePath):        
            messagebox.showerror(title = "File exists", message = "Error: " + filePath + " exists." )
        else:
            f = open(self.filePath, "x")

