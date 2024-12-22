from app.config.imports.create_table import *

class Mesa(Base): 
    __tablename__ = 'mesa'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable=False)
    status = Column(Integer, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    # Relacionamentos
    restaurante_id = Column(Integer, ForeignKey('restaurante.id'), nullable=False)
    restaurante = relationship('Restaurante', back_populates='mesas')

    ocupacoes = relationship('Ocupacao', back_populates='mesa')
