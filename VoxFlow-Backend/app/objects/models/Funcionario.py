from app.config.imports.create_table import *

class Funcionario(Base):
    # Nome da tabela
    __tablename__ = 'funcionario'

    # Atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150))
    cpf = Column(String(11), unique=True)
    telefone = Column(String(11))
    funcao = Column(Integer, nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    senha = Column(String(50), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento N:1
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='funcionarios')

    # Relacionamento 1:N
    itens_mesa = relationship('ItemMesa')
    itens_delivery = relationship('ItemDelivery')
    itens_retirada = relationship('ItemRetirada')

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'cpf': self.cpf,
            'telefone': self.telefone,
            'funcao': self.funcao,
            'login': self.login,
            'senha': self.senha,
            'active': self.active,
            'restaurante_id': self.restaurante_id
        }
    