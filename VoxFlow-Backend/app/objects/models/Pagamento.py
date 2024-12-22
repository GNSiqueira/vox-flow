from app.config.imports.create_table import *

class Pagamento(Base): 
    __tablename__ = 'pagamento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    tipo_pagamento = Column(Integer, nullable=False)
    status = Column(Boolean, default=False, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Ordem Pagamento
    ordem_pagamento_id = Column(Integer, ForeignKey('ordem_pagamento.id'), nullable=False)
    ordem_pagamento = relationship('OrdemPagamento', back_populates='pagamentos')

    # Relacionamento Recebimento
    recebimentos = relationship('Recebimento', back_populates='pagamento')