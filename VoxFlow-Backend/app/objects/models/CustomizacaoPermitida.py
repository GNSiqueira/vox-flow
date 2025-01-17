from app.config.imports.create_table import *

class CustomizacaoPermitida(Base):
    __tablename__ = 'customizacao_permitida'
    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, default=True, nullable=False)

    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto = relationship('Produto', back_populates='customizacao_permitida')

    itens_customizacao_permitida = relationship('Produto', secondary='item_customizacao_permitida')

    def to_json(self):
        return {
            'id': self.id,
            'produto_id': self.produto_id
            }