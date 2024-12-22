from app.config.imports.create_table import *

class Delivery(Base):
    __tablename__ = 'delivery'
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
    restaurante_id = Column(Integer, ForeignKey('restaurate.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='deliveries')

    # relacionamento Ordem de pagamento
    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagamento.id'), nullable=False)

    # Relacionamento item delivery
    itens_delivery = relationship('ItemDelivery', back_populates='delivery')

