import os 
from app.objects.models import *

from sqlalchemy import create_engine

os.system("rm -rf database.db")
engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
