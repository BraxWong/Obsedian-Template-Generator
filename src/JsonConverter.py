import os
from tkinter import messagebox

class json_converter():

#                        ╭━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╮
#                        ┃                              ┃
#                        ┃ json_converter Documentation ┃
#                        ┃                              ┃
#                        ╰━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╯

    """
    json_converter is a class that is used to generate a Json object.

    Attributes
    ────────────────────────────────────────────────────────────

    array : array<FileNQuantity> 
        An array of FileNQuantity object used to populate the Json object.
    
    filePath: str
        Target directory for the Json object

    template_name : str
        The name of the Json object

    write_to_file()
        When this method is called, it will first check whether the Json object already exists. If so, a message box 
        will be displayed to show users the error. If the Json object does not exist, it will create the Json object
        in the designated directory, and populate the object with the array of FileNQuantity object.

    """

    def __init__(self, array, filePath, template_name):
        self.array = array
        self.filePath = filePath
        self.template_name = template_name

    def write_to_file(self):
        if os.path.exists(self.filePath + "/" + self.template_name + ".json"):
            messagebox.showerror(title = "File exists", message = "Error: " + self.filePath + "/" + self.template_name + " exists." )
        else:
            f = open(self.filePath + "/" + self.template_name + ".json", "x")
            f.write("{\n")
            index = 0
            for i in self.array:
                f.write("\t\"" + i.fileName + "\" : "  + i.fileQuantity)
                if index != len(self.array) - 1:
                    f.write(",")
                f.write("\n")
                index += 1
            f.write("}")
