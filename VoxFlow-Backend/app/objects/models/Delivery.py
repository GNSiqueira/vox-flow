from app.config.imports.create_table import *
from app.objects.enums.StatusDelivery import StatusDelivery

class Delivery(Base):
    __tablename__ = 'delivery'

    enums = {
        'status' : StatusDelivery
    }

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    nome_cliente = Column(String(170), nullable=False)
    logradouro = Column(String(150), nullable=False)
    bairro = Column(String(100), nullable=False)
    cidade_estado = Column(String(100), nullable=False)
    status = Column(Integer, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Restaurante
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='deliveries')

    # relacionamento Ordem de pagamento
    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagamento.id'), nullable=False)
    ordem_pagamento = relationship('OrdemPagamento', back_populates='delivery')

    # Relacionamento item delivery
    itens_delivery = relationship('ItemDelivery')

    def to_json(self):
        return {
            'id': self.id,
            'data': self.data,
            'hora': self.hora,
            'nome_cliente': self.nome_cliente,
            'logradouro': self.logradouro,
            'bairro': self.bairro,
            'cidade_estado': self.cidade_estado,
            'status': self.status,
            'active': self.active,
            'restaurante_id': self.restaurante_id,
            'ordem_pagamento_id': self.ordem_pagamento_id
            }