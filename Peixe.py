from Animal import *
class Peixe(Animal):
    def __init__(self, idade):
        Animal.__init__(self, idade)
    def nadar(self):
        print("Animal nadando...")

#Peixe

from Animal import *

class Peixe(Animal):
    
    def init(self, idade):
        Animal.init(self, idade)
        
    def nadar(self):
        print("Animal nadando...")