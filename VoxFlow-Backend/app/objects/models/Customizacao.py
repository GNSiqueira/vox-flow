from app.config.imports.create_table import *

class Customizacao(Base):
    __tablename__ = 'customizacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    
    # Relacionamento Itens Customizacao
    itens_customizacao = relationship('ItemCustomizacao', secondary='item_customizacao')

    # Relacionamento Item Mesa
    item_mesa = relationship('ItemMesa', uselist=False)

    item_delivery = relationship('ItemDelivery', uselist=False)

    item_retirada = relationship('ItemRetirada', uselist=False)