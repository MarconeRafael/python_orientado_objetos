from Marca import *
m = Marca()
a = m.listar()
for obj in a:
     print(f"código:{obj.codigo}")
     print(f"nome:{obj.nome}\n")