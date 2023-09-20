import random

class SeedGenerator():
    """
    SeedGenerator is a class that is used to generate a random seed for the files within the template.
    This will be used in the future when interacting with a canva file type.

    Attributes
    ────────────────────────────────────────────────────────────

    seed : str 
        This will be the seed for the files within the template 

    character : list<char>
        This is a list of character to be used for the seed.

    generator()
        This method will generate a random seed. If random.randint(0,1) is 1, then the next character of
        the speed will be an integer ranging from 0 to 9. Else, it will be a character retrieved from the
        list of character.

    """


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
            
            
