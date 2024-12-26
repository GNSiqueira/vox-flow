import os 
from app.objects.models import *

from app.config.connection.connection_developer import Connection 

os.system("rm -rf database.db")

conexao = Connection().conectar()

Base.metadata.create_all(conexao.engine)
