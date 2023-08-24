#Comissionado
from Empregado import *
class Comissionado(Empregado):
     def __init__(self, nome, salario_base, comissao, quantidade):
          Empregado.__init__(self, nome)
          self.salario_base = salario_base
          self.comissao     = comissao
          self.quantidade   = quantidade
     def calcula_salario(self):
          return self.salario_base + self.comissao * self.quantidade