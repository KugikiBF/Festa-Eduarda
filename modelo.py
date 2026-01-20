import sqlite3

class Convidado:
    def __init__(self,nome,confirmado,quantidade=1):
        self.nome=None
        self.con