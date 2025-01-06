from app.config.imports.create_table import *
from app.objects.enums.TipoProduto import TipoProduto

class Produto(Base):
    # Nome da tabela
    __tablename__ = 'produto'

    enums = {
        'tipo_produto': TipoProduto
    }

    # Campos da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(170), nullable=False)
    descricao = Column(String(255))
    valor = Column(Numeric(10, 2), nullable=False)
    sku = Column(String(8))
    quantidade = Column(Integer, nullable=False)
    tipo_produto = Column(Integer, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento N:1
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='produtos')
    categoria_id = Column(Integer, ForeignKey('categoria.id'), nullable=False)
    categoria = relationship('Categoria', back_populates='produtos')

    # Relacionamento 1:N
    itens_retirada = relationship('ItemRetirada')
    itens_delivery = relationship('ItemDelivery')
    itens_mesa = relationship('ItemMesa')
    itens_customizacao = relationship('Customizacao', secondary='item_customizacao')
    itens_customizacao_permitida = relationship('CustomizacaoPermitida', secondary='item_customizacao_permitida', back_populates='produto')

    # Relacionamento 1:1
    customizacao_permitida = relationship('CustomizacaoPermitida', back_populates='produto', uselist=False)

    itens_combo = relationship('ItemCombo', back_populates='produto')

    combo = relationship('Combo', back_populates='produto', uselist=False)

    def to_json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "valor": self.valor,
            "sku": self.sku,
            "quantidade": self.quantidade,
            "active": self.active,
            "restaurante_id": self.restaurante_id,
            "categoria_id": self.categoria_id
        }