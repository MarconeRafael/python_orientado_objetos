import mysql.connector
class ConexaoBD():
    def __init__(self, host = "localhost", user = "root", pwd = "", bd = "dbAmazon"):
          self.host = host
          self.user = user
          self.pwd  = pwd
          self.bd   = bd
     
    def conecta(self):
          self.con = mysql.connector.connect(host     = self.host,
                                             user     = self.user,
                                             password = self.pwd,
                                             database = self.bd)
          self.cur = self.con.cursor()
     
    def desconecta(self):
          self.con.close()

    def executa_DML(self, sql):
          self.conecta() 
          self.cur.execute(sql)
          self.con.cummit()
          res = self.cur.fetchall()
          self.desconecta()
          return res     
    
    def executa_DQL(self, sql):
          self.conecta() 
          self.cur.execute(sql)
          res = self.cur.fetchall()
          self.desconecta()
          return res