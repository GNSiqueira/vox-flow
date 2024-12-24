from app.config.imports.create_table import *

class ItemMesa(Base):
    __tablename__= 'item_mesa'

    valor = Column(Numeric(10, 2), nullable=False)
    observacao = Column(Text)
    peso = Column(Numeric(10, 2))
    pago = Column(Boolean, default=False, nullable=False)
    
    ocupacao_id = Column(Integer, ForeignKey('ocupacao.id'), primary_key=True, nullable=False)
    customizacao_id = Column(Integer, ForeignKey('customizacao.id'), primary_key=True)
    funcionario_id = Column(Integer, ForeignKey('funcionario.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)
    
    ocupacao = relationship('Ocupacao', back_populates='itens_mesa')
    customizacao = relationship('Customizacao', back_populates='itens_mesa')
    funcionario = relationship('Funcionario', back_populates='itens_mesa')
    produto = relationship('Produto', back_populates='itens_mesa')