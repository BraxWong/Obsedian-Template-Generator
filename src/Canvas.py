import json
import os

def createCanvasFile(fileName, list_of_nodes, list_of_node_types):
    if len(list_of_nodes) != len(list_of_node_types):
        print("No good")
        return
    canvaFile = open(fileName, "a")
    canvaFile.write("{\n    \"nodes\":[\n")

    #Writing nodes section of the canvas file
    for x in range(len(list_of_nodes)):
        canvaFile.write(f"       {{\"type\":\"{list_of_node_types[x]}\",\"{list_of_node_types[x]}\":\"{list_of_nodes[x]}\"}}")
        if x != len(list_of_nodes) - 1:
            canvaFile.write(",\n")
        else:
            canvaFile.write("\n     ],")

createCanvasFile("testing.canva", ["HI","Bye"], ["hi","bye"])
   
    
