from app.config.imports.create_table import *

class Combo(Base): 
    __tablename__ = 'combo'

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True, nullable=False)

    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto = relationship('Produto', back_populates='combo', uselist=False)

    itens_combo = relationship('ItemCombo', back_populates='combo')
