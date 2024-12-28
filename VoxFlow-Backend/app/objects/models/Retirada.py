from app.config.imports.create_table import *

class Retirada(Base):
    __tablename__ = 'retirada'

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    nome_cliente = Column(String(170), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Restaurante
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='retiradas')

    # Relacionamento Ordem de Pagamento
    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagamento.id'), nullable=False)

    # Relacionamento item retirada
    itens_retirada = relationship('ItemRetirada')

    def to_json(self):
        return {
            "id": self.id,
            "data": self.data,
            "hora": self.hora,
            "nome_cliente": self.nome_cliente,
            "active": self.active,
            "restaurante_id": self.restaurante_id,
            "ordem_pagamento_id": self.ordem_pagamento_id
        }