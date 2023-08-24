#TestaClasses
from Chefe import *
from Comissionado import *
from Paralelepipedo import *
from Esfera import *
from Cone import *

P = Chefe("Procopio", 25000)
print(P.calcula_salario())

A = Comissionado("Aguém", 1500, 100, 15)
print(A.calcula_salario())

b = Paralelepipedo("Paralelepipedo", 1, 2, 1.5)
print(b.calcula_volume())

g = Esfera("Esfera", 2)
print(g.calcula_volume())

c = Cone("Cone", 0.5, 1)
print(c.calcula_volume())