from Animal import *
class Ave(Animal):
    def __init__(self, idade, qtde_aprox_penas):
        self.qtde_aprox_penas = qtde_aprox_penas
        Animal.__init__(self, idade)
    def voar(self):
        print("Animal voando...")      
        
     
#Ave

from Animal import *

class Ave(Animal):
    
    def init(self, idade, qtde_aprox_penas):
        Animal.__init__(self, idade)
        self.qtde_aprox_penas = qtde_aprox_penas

    def voar(self):
        print("Animal voando...")
