#Paralelepipedo
from Figura import *
class Paralelepipedo(Figura):
     def __init__(self, nome, aresta1, aresta2, aresta3):
          Figura.__init__(self, nome)
          self.aresta1 = aresta1
          self.aresta2 = aresta2
          self.aresta3 = aresta3
     def calcula_volume(self):
          return self.aresta1 * self.aresta2 self.aresta3 