from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Connection:
    def connectar(self):
        self.engine = create_engine('sqlite:///database.db')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        return self.session