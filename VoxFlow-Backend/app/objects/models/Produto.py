from app.config.imports.create_table import *

class Produto(Base):
    # Nome da tabela
    __tablename__ = 'produto'

    # Campos da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(170), nullable=False)
    descricao = Column(String(255), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    sku = Column(String(8), nullable=False)
    quantidade = Column(Integer)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento N:1
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='produtos')
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    categoria = relationship('Categoria', back_populates='produtos')

    # Relacionamento 1:N
    itens_retirada = relationship('ItemRetirada', back_populates='produto')
    itens_delivery = relationship('ItemDelivery', back_populates='produto')
    itens_mesa = relationship('ItemMesa', back_populates='produto')
    itens_customizacao = relationship('ItemCustomizacao', secondary='item_customizacao')
    itens_customizacao_permitida = relationship('ItemCustomizacaoPermitida', secondary='item_customizacao_permitida', back_populates='produto')

    # Relacionamento 1:1
    customizacao_permitida = relationship('CustomizacaoPermitida', back_populates='produto', uselist=False)

    itens_combo = relationship('ItemCombo', back_populates='produto')

    combo = relationship('Combo', back_populates='produto', uselist=False)
