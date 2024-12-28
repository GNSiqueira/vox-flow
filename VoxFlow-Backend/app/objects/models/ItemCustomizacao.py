from app.config.imports.create_table import * 

class ItemCustomizacao(Base): 
    __tablename__ = 'item_customizacao'

    customizacao_id = Column(Integer, ForeignKey('customizacao.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)
    valor = Column(Integer)

    def to_json(self):
        return {
            'customizacao_id': self.customizacao_id,
            'produto_id': self.produto_id,
            'valor': self.valor
            }