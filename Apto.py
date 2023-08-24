#Apto
from Imovel import *
class Apto(Imovel):
     def __init__(self, metragem, bairro, metragem_garagem)
          self.metragem = metragem
          self.bairros  = bairros 
          self.metragem_garagem = metragem_garagem
     def retorna_area_util(self):
          return (self.metragem+self.metragem_garagem)
     