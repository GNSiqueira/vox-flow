from app.config.imports.create_table import * 

class OrdemPagamento(Base):
    __tablename__ = 'ordem_pagamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(Boolean, default=False, nullable=False)
    valor_total = Column(Numeric(10, 2), nullable=False)
    valor_a_pagar = Column(Numeric(10, 2), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Ocupamento 
    ocupacao = relationship('Ocupacao', uselist=False)

    # Relacionamento Retirada
    retirada = relationship('Retirada', uselist=False)

    # Relacionamento Delivery
    delivery = relationship('Delivery', uselist=False)

    # Relacionamento Pagamento
    pagamentos = relationship('Pagamento', back_populates='ordem_pagamento')