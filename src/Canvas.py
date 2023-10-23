import json
import os

def createCanvasFile(fileName, list_of_nodes, list_of_node_types):
    if len(list_of_nodes) != len(list_of_node_types):
        print("No good")
        return
    canvaFile = open(fileName, "a")
    canvaFile.write("{\n    \"nodes\":[\n")
    for x in list_of_nodes:
        canvaFile.write("       {\"type\":\"\"}\n")
createCanvasFile("testing.canva", {"HI","Bye"}, {"hi","bye"})
   
    
