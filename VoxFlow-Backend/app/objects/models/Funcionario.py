from app.config.imports.create_table import *

class Funcionario(Base):
    # Nome da tabela
    __tablename__ = 'funcionario'

    # Atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    cpf = Column(String(11), nullable=False, unique=True)
    telefone = Column(String(11), nullable=False)
    funcao = Column(Integer, nullable=False)
    login = Column(String(50), nullable=False, unique=True)
    senha = Column(String(50), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento N:1
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='funcionarios')

    # Relacionamento 1:N
    itens_mesa = relationship('ItemMesa', back_populates='funcionario')
    itens_delivery = relationship('ItemDelivery', back_populates='funcionario')
    itens_retirada = relationship('ItemRetirada', back_populates='funcionario')