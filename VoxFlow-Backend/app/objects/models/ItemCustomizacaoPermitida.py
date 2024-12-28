from app.config.imports.create_table import *

class ItemCustomizacaoPermitida(Base):
    __tablename__ = 'item_customizacao_permitida'

    customizacao_permitida_id = Column(Integer, ForeignKey('customizacao_permitida.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)

    def to_json(self):
        return {
            'customizacao_permitida_id': self.customizacao_permitida_id,
            'produto_id': self.produto_id
            }