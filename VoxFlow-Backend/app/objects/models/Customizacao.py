from decimal import Decimal
from app.config.imports.create_table import *

class Customizacao(Base):
    __tablename__ = 'customizacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    
    # Relacionamento Itens Customizacao
    itens_customizacao = relationship('Produto', secondary='item_customizacao')

    item_mesa = relationship('ItemMesa', uselist=False)

    item_delivery = relationship('ItemDelivery', uselist=False)

    item_retirada = relationship('ItemRetirada', uselist=False)

    def to_json(self):
        return {
            'id': self.id,
            'valor': float(self.valor) if isinstance(self.valor, Decimal) else self.valor
            }