from flask import Flask, render_template
from database import db

app = Flask(__name__)
db.init_app(app) # LEMBRA QUE NO TUTORIAL ELA FAZ UM ARQ .flaskenv PODE SER ALI QUE O ERRO APARECA, INSTANCIAÇÃO DO VIRTUAL ENV
app.config['SECRET_KEY'] = 'minha-chave' # deve ser uma palavra robusta para segurança
conexao = "sqlite:///meubanco.sqlite" #string de conexao,


@app.route('/')
def index():
    return 'Hello from flask app!'

if __name__ == '__main__':
    app.run()