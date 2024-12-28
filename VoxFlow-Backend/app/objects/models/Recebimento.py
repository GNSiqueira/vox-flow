from app.config.imports.create_table import *

class Recebimento(Base): 
    __tablename__ = 'recebimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    tipo_pagamento = Column(Integer, nullable=False)
    status = Column(Boolean, default=False, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Pagamento
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'), nullable=False)
    pagamento = relationship('Pagamento', back_populates='recebimentos')
    
    def to_json(self):
        return {
            'id': self.id,
            'valor': self.valor,
            'tipo_pagamento': self.tipo_pagamento,
            'status': self.status,
            'active': self.active,
            'pagamento_id': self.pagamento_id
            }