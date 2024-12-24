from app.config.imports.create_table import *

class ItemCombo(Base): 
    __tablename__ = 'item_combo'

    quantidade = Column(Integer, nullable=False)

    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)
    combo_id = Column(Integer, ForeignKey('combo.id'), primary_key=True, nullable=False)
    produto = relationship('Produto', back_populates='itens_combo')
    combo = relationship('Combo', back_populates='itens_combo')
