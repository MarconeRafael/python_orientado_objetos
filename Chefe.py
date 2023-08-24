#Chefe
from Empregado import *
class Chefe(Empregado):
     def __init__(self, nome, salario_mensal):
          self.salario_mensal = salario_mensal
          Empregado.__init__(self, nome)
     def calcula_salario(self):
          return self.salario_mensal