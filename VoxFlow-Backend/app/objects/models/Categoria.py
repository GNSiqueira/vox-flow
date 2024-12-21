from app.config.imports.create_table import *

class Categoria(Base): 
    # Nome da tabela
    __tablename__ = 'categoria'

    # Campos da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(200), nullable=False)

    # Relacionamento N:1
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='categorias')

    # Relacionamento 1:N
    produtos = relationship('Produto', back_populates='categoria')