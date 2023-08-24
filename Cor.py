from ConexaoBd import *
class Cor():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def incluir(self):
        conn = ConexaoBD()
        sql = F"INSERT INTO TbCor (CoCor, NoCor) "
        sql += f"VALUES({self.codigo}, '{self.nome}')"
        conn.executa_DML(sql)

    def alterar(self, codigo, nome):
        conn = ConexaoBD()
        sql = F"UPDATE TbCor SET TbCor = '{nome}' "
        sql += f"WHERE CoCor = {codigo}"
        conn.executa_DML(sql)

    def excluir(self, codigo):
        conn = ConexaoBD()
        sql = F"DELETE FROM  TbCor WHERE CoCor = '{codigo}' "
        conn.executa_DML(sql)

    def consultar(self, codigo):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbCor WHERE CoCor = '{codigo}' "
        res = conn.executa_DQL(sql)

        for linha in res:
            codigo = linha[0]
            nome = linha[1]
            
            c = Marca(codigo, nome)

        return c

    def listar(self):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbCor ORDER BY NoCor "
        res = conn.executa_DQL(sql)
        
        cor = []
        for linha in res:
            codigo = linha[0]
            nome = linha[1]

            c = Cor(codigo, nome)
            cor.append(c)

        return c
