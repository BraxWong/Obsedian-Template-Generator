import random

class SeedGenerator():

    def __init__(self):
        self.seed = ""
        self.character = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
         

    def generator(self):
        for x in range(15):
            if random.randint(0,1) == 1:
                self.seed += str(random.randint(0,9))
            else:
                self.seed += self.character[random.randint(0,25)] 
        return self.seed
            
            
