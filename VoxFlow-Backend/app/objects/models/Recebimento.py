from app.config.imports.create_table import *
from decimal import Decimal

class Recebimento(Base): 
    __tablename__ = 'recebimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Numeric(10, 2), nullable=False)
    data = Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    antecipacao = Column(Boolean, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamento Pagamento
    pagamento_id = Column(Integer, ForeignKey('pagamento.id'), nullable=False)
    pagamento = relationship('Pagamento', back_populates='recebimentos')
    
    def to_json(self):
        return {
            'id': self.id,
            'valor': float(self.valor) if isinstance(self.valor, Decimal) else self.valor,
            'data': self.data,
            'hora': self.hora,
            'antecipacao': self.antecipacao,
            'active': self.active,            
            'pagamento_id': self.pagamento_id
        }