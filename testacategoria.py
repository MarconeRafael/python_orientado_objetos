from Categoria import *
c = Categoria()
a = c.listar()
for obj in a:
     print(f"código:{obj.codigo}")
     print(f"nome:{obj.nome}\n")