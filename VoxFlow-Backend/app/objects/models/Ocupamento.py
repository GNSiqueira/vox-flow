from app.config.imports.create_table import *

class Ocupacao(Base): 
    __tablename__ = 'ocupacao'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor_total = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    status = Column(Boolean, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamentos
    mesa_id = Column(Integer, ForeignKey('mesa.id'), nullable=False)
    mesa = relationship('Mesa', back_populates='ocupacoes')

    itens_mesa = relationship('ItemMesa', back_populates='ocupacao')

    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagameto.id'), nullable=False)