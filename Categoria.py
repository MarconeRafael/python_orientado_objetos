from ConexaoBd import * 
class Categoria():

    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome

    def incluir(self):
        conn = ConexaoBD()
        sql = F"INSERT INTO TbCategoria (CoCategoria, NoCategoria) "
        sql += f"VALUES({self.codigo}, '{self.nome}')"
        conn.executa_DML(sql)

    def alterar(self, codigo, nome):
        conn = ConexaoBD()
        sql = F"UPDATE TbCategoria SET NoCategoria = '{nome}' "
        sql += f"WHERE CoCategoria = {codigo}"
        conn.executa_DML(sql)

    def excluir(self, codigo):
        conn = ConexaoBD()
        sql = F"DELETE FROM  TbCategoria WHERE CoCategoria = '{codigo}' "
        conn.executa_DML(sql)

    def consultar(self, codigo):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbCategoria WHERE CoCategoria = '{codigo}' "
        res = conn.executa_DQL(sql)

        for linha in res:
            codigo = linha[0]
            nome = linha[1]
            
            c = Categoria(codigo, nome)

        return c

    def listar(self):
        conn = ConexaoBD()
        sql = f"SELECT * FROM TbCategoria ORDER BY NoCategoria"
        res = conn.executa_DQL(sql)
        
        categoria = []
        for linha in res:
            codigo = linha[0]
            nome = linha[1]

            c = Categoria(codigo, nome)
            categoria.append(c)

        return c