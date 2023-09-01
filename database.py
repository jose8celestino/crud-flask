# DATABSE.PY REPRESENTA A INSTANCIA DO BANCO DE DADOS
# É importante que o db fique num arquivo a parte para que não gere redundanccia de importação (erro de importe circular) 

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()