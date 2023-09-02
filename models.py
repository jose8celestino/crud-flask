from database import db

class Usuario(db.Model): # Model é uma classe que existe dentro de instancia de SQLalchemy
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __init__(self, nome, email, senha): # instancia o objeto
        self.nome = nome
        self.email = email
        self.senha = senha
    
    def __repr__(self):    # representa o objeto
        return "Usuário {}".format(self.nome)

    