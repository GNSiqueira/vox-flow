from app.config.imports.create_table import *

class ItemRetirada(Base):
    __tablename__= 'item_retirada'

    valor = Column(Numeric(10, 2), nullable=False)
    observacao = Column(Text)
    peso = Column(Numeric(10, 2))
    pago = Column(Boolean, default=False, nullable=False)
    
    retirada_id = Column(Integer, ForeignKey('retirada.id'), primary_key=True, nullable=False)
    customizacao_id = Column(Integer, ForeignKey('customizacao.id'), primary_key=True)
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)