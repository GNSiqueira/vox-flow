from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def conectar(self):
        self.engine = create_engine('sqlite:///database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        return self
    
    def desconectar(self) -> None:
        self.session.close()