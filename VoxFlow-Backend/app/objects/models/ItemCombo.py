from app.config.imports.create_table import *

class ItemCombo(Base): 
    # Table name
    __tablename__ = 'item_combo'

    # Atributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer, nullable=False)

    # Relacioanmento N:1
    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto = relationship('Produto', back_populates='itens_combo')
    produto_base_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto_base = relationship('Produto', back_populates='itens_combo_base')