     from ConexaoBd import *
class Marca():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def incluir(self):
        conn = ConexaoBD()
        sql = F"INSERT INTO TbMarca (CoMarca, NoMarca) "
        sql += f"VALUES({self.codigo}, '{self.nome}')"
        conn.executa_DML(sql)

    def alterar(self, codigo, nome):
        conn = ConexaoBD()
        sql = F"UPDATE TbMarca SET NoMarca = '{nome}' "
        sql += f"WHERE CoMarca = {codigo}"
        conn.executa_DML(sql)

    def excluir(self, codigo):
        conn = ConexaoBD()
        sql = F"DELETE FROM  TbMarca WHERE CoMarca = '{codigo}' "
        conn.executa_DML(sql)

    def consultar(self, codigo):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbMarca WHERE CoMarca = '{codigo}' "
        res = conn.executa_DQL(sql)

        for linha in res:
            codigo = linha[0]
            nome = linha[1]
            
            m = Marca(codigo, nome)

        return m

    def listar(self):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbMarca ORDER BY NoMarca "
        res = conn.executa_DQL(sql)
        
        marca = []
        for linha in res:
            codigo = linha[0]
            nome = linha[1]

            m = Marca(codigo, nome)
            marca.append(m)

        return m
   
