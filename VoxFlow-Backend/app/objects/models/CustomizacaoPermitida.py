from app.config.imports.create_table import *

class CustomizacaoPermitida(Base):
    __tablename__ = 'customizacao_permitida'
    id = Column(Integer, primary_key=True, autoincrement=True)

    produto_id = Column(Integer, ForeignKey('produto.id'), nullable=False)
    produto = relationship('Produto', back_populates='customizacao_permitida')

    itens_customizacao_permitida = relationship('ItemCustomizacaoPermitida', secondary='item_customizacao_permitida')
