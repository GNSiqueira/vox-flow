from app.config.imports.create_table import *

class ItemCustomizacaoPermitida(Base):
    __tablename__ = 'item_customizacao_permitida'

    customizacao_permitida_id = Column(Integer, ForeignKey('customizacao_permitida.id'), primary_key=True, nullable=False)
    produto_id = Column(Integer, ForeignKey('produto.id'), primary_key=True, nullable=False)