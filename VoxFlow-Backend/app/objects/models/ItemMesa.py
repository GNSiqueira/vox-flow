from decimal import Decimal
from app.config.imports.create_table import *

class ItemMesa(Base):
    __tablename__= 'item_mesa'
    
    ocupacao_id = Column(Integer, ForeignKey('ocupacao.id'), nullable=False, primary_key=True)
    customizacao_id = Column(Integer, ForeignKey('customizacao.id'), primary_key=True)
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)
    
    valor = Column(Numeric(10, 2), nullable=False)
    observacao = Column(Text)
    peso = Column(Numeric(10, 2))
    pago = Column(Boolean, default=False, nullable=False)

    def to_json(self):
        return {
            'valor': float(self.valor) if isinstance(self.valor, Decimal) else self.valor,
            'observacao': self.observacao,
            'peso': float(self.peso) if isinstance(self.peso, Decimal) else self.peso,
            'pago': self.pago,
            'ocupacao_id': self.ocupacao_id,
            'customizacao_id': self.customizacao_id,
            'funcionario_id': self.funcionario_id,
            'produto_id': self.produto_id
            }