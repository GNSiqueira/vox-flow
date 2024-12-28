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

    itens_mesa = relationship('ItemMesa')

    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagamento.id'), nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'valor_total': self.valor_total,
            'data': self.data,
            'hora': self.hora,
            'status': self.status,
            'active': self.active,
            'mesa_id': self.mesa_id,
            'ordem_pagamento_id': self.ordem_pagamento_id
            }