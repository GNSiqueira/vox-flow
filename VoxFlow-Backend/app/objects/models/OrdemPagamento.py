from decimal import Decimal
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

    def to_json(self):
        return {
            'id': self.id,
            'status': self.status,
            'valor_total': float(self.valor_total) if isinstance(self.valor_total, Decimal) else self.valor_total,
            'valor_a_pagar': float(self.valor_a_pagar) if isinstance(self.valor_a_pagar, Decimal) else self.valor_a_pagar,
            'active': self.active
            }