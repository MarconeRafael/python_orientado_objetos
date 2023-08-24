#Cone
from Figura import *
class Cone(Figura):
     def __init__(self, nome, raio, altura):
          Figura.__init__(self, nome)
          self.raio = raio
          self.altura = altura
     def calcula_volume(self):
          volume = (self.altura * (self.raio**2) * 3.14)/3
          return volume