import os
from tkinter import messagebox

class json_converter():

    def __init__(self, array, filePath, template_name):
        self.array = array
        self.filePath = filePath
        self.template_name = template_name

    def write_to_file(self):
        if os.path.exists(self.filePath + "/" + self.template_name + ".json"):
            messagebox.showerror(title = "File exists", message = "Error: " + self.filePath + "/" + self.template_name + " exists." )
        else:
            print(self.filePath + "/" + self.template_name + ".json")
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
