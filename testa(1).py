from Peixe import *
from Ave import *
from Pato import *
from Animal import *

eu = Animal(15)
eu.respirar()

nemo = Peixe(2)
nemo.nadar()

urubu = Ave(4, 5000)
urubu.voar()

patolino = Pato(3, 4000)
patolino.caminhar()
print(patolino.mergulhar())