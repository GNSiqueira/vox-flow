from app.config.imports.create_table import *

class Restarante(Base):
    # Nome da tabela
    __tablename__ = 'restaurante'

    # Atributos
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    cnpj = Column(String(14), nullable=False, unique=True)
    logradouro = Column(String(200), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade = Column(String(100), nullable=False)
    estado = Column(String(2), nullable=False)
    cep = Column(String(8), nullable=False)
    email = Column (String(150), nullable=False)
    telefone = Column(String(11), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento
    funcionarios = relationship('Funcionario', back_populates='restaurante')
    mesas = relationship('Mesa', back_populates='restaurante')
    produtos = relationship('Produto', back_populates='restaurante')
    categorias = relationship('Categoria', back_populates='restaurante')
    retiradas = relationship('Retirada', back_populates='restaurante')
    deliveries = relationship('Delivery', back_populates='restaurante')