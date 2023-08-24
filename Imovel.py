#Imovel
from abc import ABC, abstractmethod
class Imovel(ABC ):
     metragem = []
     bairro = []
     @abstractmethod
     def retorna_area_util(self):
          pass
     