import mysql.connector
def conectar():
 """Abre e devolve uma conexão com o banco 'escola'."""
 return mysql.connector.connect(
 host="localhost",
 user="root",
 password="sua_senha_aqui", # troque pela senha do seu MySQL
 database="escola",
 )
