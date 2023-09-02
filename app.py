from flask import Flask
from database import db
from flask_migrate import Migrate  # PERMITE FAZER MAPEAMENTO OBJETO RELACIONAL 

app = Flask(__name__)

db.init_app(app) # LEMBRA QUE NO TUTORIAL ELA FAZ UM ARQ .flaskenv PODE SER ALI QUE O ERRO APARECA, INSTANCIAÇÃO DO VIRTUAL ENV
conexao = "sqlite:///meubanco.sqlite" #string de conexao,

app.config['SECRET_KEY'] = 'minha-chave' # deve ser uma palavra robusta para segurança
app.config['SQLALCHEMY_DATABASE_URI'] = conexao # URL DO BANCO
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False

migrate = Migrate(app, db) # ASSOSSIA A MINHA APLICAÇÃO COM O BANCO DE DADOS.

@app.route('/')
def index():
    return 'Hello from flask app!'

if __name__ == '__main__':
    app.run()