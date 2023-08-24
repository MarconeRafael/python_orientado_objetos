from Ave import *
from Peixe import *
class Pato(Ave, Peixe):
    def __init__(self, idade, qtde_aprox_penas):
        Ave.__init__(self, idade, qtde_aprox_penas)
        Peixe.__init__(self)
    def caminhar(self):
        print("Pato caminhando...")
    def mergulhar(self):
        return "Pato mergulhando..."
        
          
          
          
          
#Pato

from Ave import *

from Peixe import *

class Pato(Ave, Peixe):
    
    def init(self, qtde_aprox_penas):
        Ave.init(self, idade, qtde_aprox_penas)
        Peixe.init(self)

    def caminhar(self):
        print("Pato caminhando...")
        
    def mergulhar(self):
        return "Pato mergulhando..."