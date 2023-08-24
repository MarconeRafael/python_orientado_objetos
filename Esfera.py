#Esfera
from Figura import *
class Esfera(Figura):
     def __init__(self, nome, raio):
          Figura.__init__(self, nome)
          self.raio = raio
     def calcula_volume(self):
          volume = (self.raio **3)*(4/3)*3.14
          return volume 