import os 
from app.objects.models import *
from decimal import Decimal
from datetime import date, time
from app.config.connection.connection_developer import Connection 

os.system("rm -rf database.db")

conexao = Connection().conectar()

Base.metadata.create_all(conexao.engine)

session = conexao.session

#region Restaurante
restaurantes = [
    {
        "nome": "Restaurante Sabor Caseiro",
        "cnpj": "12345678000111",
        "logradouro": "Rua das Flores, 123",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01001000",
        "email": "contato@saborcaseiro.com",
        "telefone": "11987654321"
    },
    {
        "nome": "Bistrô Elegance",
        "cnpj": "22345678000111",
        "logradouro": "Avenida Paulista, 1500",
        "bairro": "Bela Vista",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01311000",
        "email": "reservas@bistroelegance.com",
        "telefone": "11976543210"
    },
    {
        "nome": "Churrascaria Gaúcha",
        "cnpj": "32345678000111",
        "logradouro": "Rua dos Pampas, 45",
        "bairro": "Moema",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "04077001",
        "email": "contato@churrascariagaucha.com",
        "telefone": "11965432109"
    },
    {
        "nome": "Pizzaria Bella Napoli",
        "cnpj": "42345678000111",
        "logradouro": "Rua Itália, 500",
        "bairro": "Vila Mariana",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "04110040",
        "email": "pedidos@bellanapoli.com",
        "telefone": "11954321098"
    },
    {
        "nome": "Restaurante Oriental",
        "cnpj": "52345678000111",
        "logradouro": "Rua Japão, 321",
        "bairro": "Liberdade",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01503000",
        "email": "contato@orientalrestaurante.com",
        "telefone": "11943210987"
    },
    {
        "nome": "Café do Centro",
        "cnpj": "62345678000111",
        "logradouro": "Praça Central, 10",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01002001",
        "email": "atendimento@cafedocentro.com",
        "telefone": "11932109876"
    },
    {
        "nome": "Hamburgueria Gourmet",
        "cnpj": "72345678000111",
        "logradouro": "Rua Burguer, 78",
        "bairro": "Pinheiros",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "05422000",
        "email": "contato@gourmethamburguer.com",
        "telefone": "11921098765"
    },
    {
        "nome": "Cantina do Chef",
        "cnpj": "82345678000111",
        "logradouro": "Rua da Cantina, 456",
        "bairro": "Santana",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "02013001",
        "email": "reservas@cantinadochef.com",
        "telefone": "11910987654"
    },
    {
        "nome": "Doceria Delícia",
        "cnpj": "92345678000111",
        "logradouro": "Rua dos Doces, 99",
        "bairro": "Aclimação",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01531001",
        "email": "contato@doceriadelicia.com",
        "telefone": "11909876543"
    },
    {
        "nome": "Bar do Zé",
        "cnpj": "10345678000111",
        "logradouro": "Avenida Principal, 200",
        "bairro": "Jardins",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "01451000",
        "email": "contato@bardoze.com",
        "telefone": "11987654320"
    }
]

for dados in restaurantes:
    restaurante = Restaurante(**dados)
    session.add(restaurante)
#endregion
#region Funcionario
funcionarios = [
    Funcionario(
        nome='Carlos Silva',
        email='carlos.silva@email.com',
        cpf='12345678901',
        telefone='11987654321',
        funcao=TipoFuncao.ADMINISTRADOR,
        login='carlos_admin',
        senha='senha123',
        restaurante_id=1
    ),
    Funcionario(
        nome='Mariana Oliveira',
        email='mariana.oliveira@email.com',
        cpf='23456789012',
        telefone='21987654321',
        funcao=TipoFuncao.CAIXA,
        login='mariana_caixa',
        senha='senha123',
        restaurante_id=1
    ),
    Funcionario(
        nome='Rafael Santos',
        email='rafael.santos@email.com',
        cpf='34567890123',
        telefone='31987654321',
        funcao=TipoFuncao.GARCOM,
        login='rafael_garcom',
        senha='senha123',
        restaurante_id=1
    ),
    Funcionario(
        nome='Ana Costa',
        email='ana.costa@email.com',
        cpf='45678901234',
        telefone='41987654321',
        funcao=TipoFuncao.ADMINISTRADOR,
        login='ana_admin',
        senha='senha123',
        restaurante_id=2
    ),
    Funcionario(
        nome='Pedro Almeida',
        email='pedro.almeida@email.com',
        cpf='56789012345',
        telefone='51987654321',
        funcao=TipoFuncao.CAIXA,
        login='pedro_caixa',
        senha='senha123',
        restaurante_id=2
    ),
    Funcionario(
        nome='Camila Rocha',
        email='camila.rocha@email.com',
        cpf='67890123456',
        telefone='61987654321',
        funcao=TipoFuncao.GARCOM,
        login='camila_garcom',
        senha='senha123',
        restaurante_id=2
    ),
    Funcionario(
        nome='Lucas Pereira',
        email='lucas.pereira@email.com',
        cpf='78901234567',
        telefone='71987654321',
        funcao=TipoFuncao.ADMINISTRADOR,
        login='lucas_admin',
        senha='senha123',
        restaurante_id=3
    ),
    Funcionario(
        nome='Fernanda Lima',
        email='fernanda.lima@email.com',
        cpf='89012345678',
        telefone='81987654321',
        funcao=TipoFuncao.CAIXA,
        login='fernanda_caixa',
        senha='senha123',
        restaurante_id=3
    ),
    Funcionario(
        nome='Thiago Mendes',
        email='thiago.mendes@email.com',
        cpf='90123456789',
        telefone='91987654321',
        funcao=TipoFuncao.GARCOM,
        login='thiago_garcom',
        senha='senha123',
        restaurante_id=3
    ),
    Funcionario(
        nome='Juliana Freitas',
        email='juliana.freitas@email.com',
        cpf='01234567890',
        telefone='21998765432',
        funcao=TipoFuncao.ADMINISTRADOR,
        login='juliana_admin',
        senha='senha123',
        restaurante_id=3
    )
]

with conexao.session as session:
    session.add_all(funcionarios)
    session.commit()
#endregion
#region Categoria


categorias = [
    Categoria(
        nome='Bebidas',
        descricao='Categoria para todas as bebidas disponíveis',
        restaurante_id=1
    ),
    Categoria(
        nome='Comidas',
        descricao='Pratos principais e refeições',
        restaurante_id=1
    ),
    Categoria(
        nome='Sobremesas',
        descricao='Doces e sobremesas variadas',
        restaurante_id=1
    ),
    Categoria(
        nome='Lanches',
        descricao='Lanches rápidos e sanduíches',
        restaurante_id=2
    ),
    Categoria(
        nome='Massas',
        descricao='Massas e molhos especiais',
        restaurante_id=2
    ),
    Categoria(
        nome='Vegetarianos',
        descricao='Pratos vegetarianos e veganos',
        restaurante_id=2
    ),
    Categoria(
        nome='Carnes',
        descricao='Pratos com carne bovina, suína e frango',
        restaurante_id=3
    ),
    Categoria(
        nome='Peixes',
        descricao='Pratos com frutos do mar e peixes',
        restaurante_id=3
    ),
    Categoria(
        nome='Especiais',
        descricao='Pratos especiais do chef',
        restaurante_id=3
    ),
    Categoria(
        nome='Saladas',
        descricao='Saladas frescas e leves',
        restaurante_id=3
    )
]

with conexao.session as session:
    session.add_all(categorias)
    session.commit()
#endregion
#region Produto
produtos = [
    Produto(
        nome='Coca-Cola Lata',
        descricao='Refrigerante Coca-Cola lata 350ml',
        valor=Decimal('5.50'),
        sku='COC001',
        quantidade=100,
        tipo_produto=TipoProduto.SIMPLES,  # Usando o Enum
        restaurante_id=1,
        categoria_id=1
    ),
    Produto(
        nome='Hambúrguer Clássico',
        descricao='Hambúrguer com carne, queijo e salada',
        valor=Decimal('15.00'),
        sku='HAM001',
        quantidade=50,
        tipo_produto=TipoProduto.COMBO,  # Usando o Enum
        restaurante_id=1,
        categoria_id=4
    ),
    Produto(
        nome='Pizza Marguerita',
        descricao='Pizza com molho de tomate, mussarela e manjericão',
        valor=Decimal('30.00'),
        sku='PIZ001',
        quantidade=20,
        tipo_produto=TipoProduto.COMBO,  # Usando o Enum
        restaurante_id=2,
        categoria_id=5
    ),
    Produto(
        nome='Sorvete de Chocolate',
        descricao='Sorvete de chocolate 500ml',
        valor=Decimal('10.00'),
        sku='SOR001',
        quantidade=30,
        tipo_produto=TipoProduto.PESSO,  # Usando o Enum
        restaurante_id=2,
        categoria_id=3
    ),
    Produto(
        nome='Salada Caesar',
        descricao='Salada com alface, frango, parmesão e croutons',
        valor=Decimal('12.50'),
        sku='SAL001',
        quantidade=40,
        tipo_produto=TipoProduto.SIMPLES,  # Usando o Enum
        restaurante_id=3,
        categoria_id=10
    ),
    Produto(
        nome='Espaguete à Bolonhesa',
        descricao='Massa com molho bolonhesa',
        valor=Decimal('18.00'),
        sku='ESP001',
        quantidade=25,
        tipo_produto=TipoProduto.COMBO,  # Usando o Enum
        restaurante_id=3,
        categoria_id=5
    ),
    Produto(
        nome='Frango Grelhado',
        descricao='Peito de frango grelhado com legumes',
        valor=Decimal('20.00'),
        sku='FRA001',
        quantidade=35,
        tipo_produto=TipoProduto.COMBO,  # Usando o Enum
        restaurante_id=1,
        categoria_id=7
    ),
    Produto(
        nome='Salmão Grelhado',
        descricao='Salmão grelhado com purê de batata',
        valor=Decimal('35.00'),
        sku='SAL002',
        quantidade=15,
        tipo_produto=TipoProduto.COMBO,  # Usando o Enum
        restaurante_id=2,
        categoria_id=8
    ),
    Produto(
        nome='Bolo de Cenoura',
        descricao='Bolo de cenoura com cobertura de chocolate',
        valor=Decimal('8.00'),
        sku='BOL001',
        quantidade=25,
        tipo_produto=TipoProduto.PESSO,  # Usando o Enum
        restaurante_id=3,
        categoria_id=3
    ),
    Produto(
        nome='Suco de Laranja',
        descricao='Suco de laranja natural 500ml',
        valor=Decimal('6.00'),
        sku='SUC001',
        quantidade=60,
        tipo_produto=TipoProduto.SIMPLES,  # Usando o Enum
        restaurante_id=1,
        categoria_id=1
    )
]

with conexao.session as session:
    session.add_all(produtos)
    session.commit()
#endregion#region Combo
#region Combo
combos = [
    {
        "produto_id": 1,
        "active": True
    },
    {
        "produto_id": 2,
        "active": True
    },
    {
        "produto_id": 3,
        "active": True
    },
    {
        "produto_id": 4,
        "active": True
    },
    {
        "produto_id": 5,
        "active": True
    },
    {
        "produto_id": 6,
        "active": False
    },
    {
        "produto_id": 7,
        "active": False
    },
    {
        "produto_id": 8,
        "active": True
    },
    {
        "produto_id": 9,
        "active": True
    },
    {
        "produto_id": 10,
        "active": False
    }
]

for dados in combos:
    combo = Combo(**dados)
    session.add(combo)
#endregion
#region ItemCombo
itens_combo = [
    {
        "produto_id": 1,
        "combo_id": 1,
        "quantidade": 2
    },
    {
        "produto_id": 2,
        "combo_id": 1,
        "quantidade": 3
    },
    {
        "produto_id": 3,
        "combo_id": 2,
        "quantidade": 1
    },
    {
        "produto_id": 4,
        "combo_id": 2,
        "quantidade": 5
    },
    {
        "produto_id": 5,
        "combo_id": 3,
        "quantidade": 4
    },
    {
        "produto_id": 6,
        "combo_id": 3,
        "quantidade": 2
    },
    {
        "produto_id": 7,
        "combo_id": 4,
        "quantidade": 6
    },
    {
        "produto_id": 8,
        "combo_id": 4,
        "quantidade": 2
    },
    {
        "produto_id": 9,
        "combo_id": 5,
        "quantidade": 3
    },
    {
        "produto_id": 10,
        "combo_id": 5,
        "quantidade": 1
    }
]

for dados in itens_combo:
    item_combo = ItemCombo(**dados)
    session.add(item_combo)
#endregion
#region CustomizacaoPermitida
customizacoes_permitidas = [
    {
        "produto_id": 1,
        "active": True
    },
    {
        "produto_id": 2,
        "active": True
    },
    {
        "produto_id": 3,
        "active": True
    },
    {
        "produto_id": 4,
        "active": False
    },
    {
        "produto_id": 5,
        "active": True
    },
    {
        "produto_id": 6,
        "active": False
    },
    {
        "produto_id": 7,
        "active": True
    },
    {
        "produto_id": 8,
        "active": True
    },
    {
        "produto_id": 9,
        "active": True
    },
    {
        "produto_id": 10,
        "active": False
    }
]

for dados in customizacoes_permitidas:
    customizacao_permitida = CustomizacaoPermitida(**dados)
    session.add(customizacao_permitida)
#endregion
#region ItemCustomizacaoPermitida
itens_customizacao_permitida = [
    {
        "customizacao_permitida_id": 1,
        "produto_id": 1
    },
    {
        "customizacao_permitida_id": 1,
        "produto_id": 2
    },
    {
        "customizacao_permitida_id": 2,
        "produto_id": 3
    },
    {
        "customizacao_permitida_id": 2,
        "produto_id": 4
    },
    {
        "customizacao_permitida_id": 3,
        "produto_id": 5
    },
    {
        "customizacao_permitida_id": 3,
        "produto_id": 6
    },
    {
        "customizacao_permitida_id": 4,
        "produto_id": 7
    },
    {
        "customizacao_permitida_id": 4,
        "produto_id": 8
    },
    {
        "customizacao_permitida_id": 5,
        "produto_id": 9
    },
    {
        "customizacao_permitida_id": 5,
        "produto_id": 10
    }
]

for dados in itens_customizacao_permitida:
    item_customizacao_permitida = ItemCustomizacaoPermitida(**dados)
    session.add(item_customizacao_permitida)
#endregion
#region Customizacao
customizacoes = [
    {
        "valor": 10.50
    },
    {
        "valor": 20.75
    },
    {
        "valor": 15.30
    },
    {
        "valor": 8.99
    },
    {
        "valor": 5.00
    },
    {
        "valor": 12.40
    },
    {
        "valor": 18.60
    },
    {
        "valor": 22.10
    },
    {
        "valor": 25.00
    },
    {
        "valor": 30.80
    }
]

for dados in customizacoes:
    customizacao = Customizacao(**dados)
    session.add(customizacao)
#endregion
#region ItemCustomizacao
itens_customizacao = [
    {
        "customizacao_id": 1,
        "produto_id": 1,
        "valor": 5
    },
    {
        "customizacao_id": 1,
        "produto_id": 2,
        "valor": 8
    },
    {
        "customizacao_id": 2,
        "produto_id": 3,
        "valor": 6
    },
    {
        "customizacao_id": 2,
        "produto_id": 4,
        "valor": 7
    },
    {
        "customizacao_id": 3,
        "produto_id": 5,
        "valor": 10
    },
    {
        "customizacao_id": 3,
        "produto_id": 6,
        "valor": 12
    },
    {
        "customizacao_id": 4,
        "produto_id": 7,
        "valor": 3
    },
    {
        "customizacao_id": 4,
        "produto_id": 8,
        "valor": 4
    },
    {
        "customizacao_id": 5,
        "produto_id": 9,
        "valor": 9
    },
    {
        "customizacao_id": 5,
        "produto_id": 10,
        "valor": 15
    }
]

for dados in itens_customizacao:
    item_customizacao = ItemCustomizacao(**dados)
    session.add(item_customizacao)
#endregion
#region Mesa
mesas = [
    {
        "nome": "Mesa 1",
        "status": StatusMesa.ABERTA,
        "active": True,
        "restaurante_id": 1
    },
    {
        "nome": "Mesa 2",
        "status": StatusMesa.PAGAMENTO_PARCIAL,
        "active": True,
        "restaurante_id": 2
    },
    {
        "nome": "Mesa 3",
        "status": StatusMesa.OCUPADA,
        "active": True,
        "restaurante_id": 3
    },
    {
        "nome": "Mesa 4",
        "status": StatusMesa.ABERTA,
        "active": True,
        "restaurante_id": 4
    },
    {
        "nome": "Mesa 5",
        "status": StatusMesa.PAGAMENTO_PARCIAL,
        "active": False,
        "restaurante_id": 5
    },
    {
        "nome": "Mesa 6",
        "status": StatusMesa.OCUPADA,
        "active": True,
        "restaurante_id": 6
    },
    {
        "nome": "Mesa 7",
        "status": StatusMesa.ABERTA,
        "active": True,
        "restaurante_id": 7
    },
    {
        "nome": "Mesa 8",
        "status": StatusMesa.PAGAMENTO_PARCIAL,
        "active": False,
        "restaurante_id": 8
    },
    {
        "nome": "Mesa 9",
        "status": StatusMesa.OCUPADA,
        "active": True,
        "restaurante_id": 9
    },
    {
        "nome": "Mesa 10",
        "status": StatusMesa.ABERTA,
        "active": True,
        "restaurante_id": 10
    }
]

for dados in mesas:
    mesa = Mesa(**dados)
    session.add(mesa)
#endregion
#region OrdemPagamento
ordens_pagamento = [
    {
        "status": False,
        "valor_total": 150.50,
        "valor_a_pagar": 120.00,
        "active": True
    },
    {
        "status": True,
        "valor_total": 200.00,
        "valor_a_pagar": 180.00,
        "active": True
    },
    {
        "status": False,
        "valor_total": 75.25,
        "valor_a_pagar": 50.00,
        "active": True
    },
    {
        "status": True,
        "valor_total": 300.00,
        "valor_a_pagar": 250.00,
        "active": True
    },
    {
        "status": False,
        "valor_total": 100.00,
        "valor_a_pagar": 90.00,
        "active": False
    },
    {
        "status": True,
        "valor_total": 450.00,
        "valor_a_pagar": 400.00,
        "active": True
    },
    {
        "status": False,
        "valor_total": 120.00,
        "valor_a_pagar": 100.00,
        "active": True
    },
    {
        "status": True,
        "valor_total": 175.50,
        "valor_a_pagar": 160.00,
        "active": True
    },
    {
        "status": False,
        "valor_total": 220.00,
        "valor_a_pagar": 200.00,
        "active": True
    },
    {
        "status": True,
        "valor_total": 350.00,
        "valor_a_pagar": 300.00,
        "active": False
    }
]

for dados in ordens_pagamento:
    ordem_pagamento = OrdemPagamento(**dados)
    session.add(ordem_pagamento)
#endregion
#region Pagamento
pagamentos = [
    {
        "valor": 100.00,
        "tipo_pagamento": TipoPagamento.PIX,
        "status": False,
        "active": True,
        "ordem_pagamento_id": 1
    },
    {
        "valor": 150.00,
        "tipo_pagamento": TipoPagamento.DINHEIRO,
        "status": True,
        "active": True,
        "ordem_pagamento_id": 2
    },
    {
        "valor": 200.00,
        "tipo_pagamento": TipoPagamento.DEBITO,
        "status": False,
        "active": True,
        "ordem_pagamento_id": 3
    },
    {
        "valor": 300.00,
        "tipo_pagamento": TipoPagamento.CREDITO,
        "status": True,
        "active": True,
        "ordem_pagamento_id": 4
    },
    {
        "valor": 50.00,
        "tipo_pagamento": TipoPagamento.PIX,
        "status": False,
        "active": True,
        "ordem_pagamento_id": 5
    },
    {
        "valor": 250.00,
        "tipo_pagamento": TipoPagamento.DINHEIRO,
        "status": True,
        "active": True,
        "ordem_pagamento_id": 6
    },
    {
        "valor": 400.00,
        "tipo_pagamento": TipoPagamento.DEBITO,
        "status": False,
        "active": True,
        "ordem_pagamento_id": 7
    },
    {
        "valor": 350.00,
        "tipo_pagamento": TipoPagamento.CREDITO,
        "status": True,
        "active": True,
        "ordem_pagamento_id": 8
    },
    {
        "valor": 180.00,
        "tipo_pagamento": TipoPagamento.PIX,
        "status": False,
        "active": True,
        "ordem_pagamento_id": 9
    },
    {
        "valor": 220.00,
        "tipo_pagamento": TipoPagamento.DINHEIRO,
        "status": True,
        "active": False,
        "ordem_pagamento_id": 10
    }
]

for dados in pagamentos:
    pagamento = Pagamento(**dados)
    session.add(pagamento)
#endregion
#region Recebimento
recebimentos = [
    {
        "valor": Decimal('100.00'),
        "data": date(2025, 1, 1),
        "hora": time(12, 30),
        "antecipacao": False,
        "active": True,
        "pagamento_id": 1
    },
    {
        "valor": Decimal('150.00'),
        "data": date(2025, 1, 2),
        "hora": time(14, 45),
        "antecipacao": True,
        "active": True,
        "pagamento_id": 2
    },
    {
        "valor": Decimal('200.00'),
        "data": date(2025, 1, 3),
        "hora": time(16, 00),
        "antecipacao": False,
        "active": True,
        "pagamento_id": 3
    },
    {
        "valor": Decimal('300.00'),
        "data": date(2025, 1, 4),
        "hora": time(10, 15),
        "antecipacao": True,
        "active": True,
        "pagamento_id": 4
    },
    {
        "valor": Decimal('50.00'),
        "data": date(2025, 1, 5),
        "hora": time(18, 30),
        "antecipacao": False,
        "active": True,
        "pagamento_id": 5
    },
    {
        "valor": Decimal('250.00'),
        "data": date(2025, 1, 6),
        "hora": time(11, 00),
        "antecipacao": True,
        "active": True,
        "pagamento_id": 6
    },
    {
        "valor": Decimal('400.00'),
        "data": date(2025, 1, 7),
        "hora": time(13, 30),
        "antecipacao": False,
        "active": True,
        "pagamento_id": 7
    },
    {
        "valor": Decimal('350.00'),
        "data": date(2025, 1, 8),
        "hora": time(9, 00),
        "antecipacao": True,
        "active": True,
        "pagamento_id": 8
    },
    {
        "valor": Decimal('180.00'),
        "data": date(2025, 1, 9),
        "hora": time(15, 00),
        "antecipacao": False,
        "active": True,
        "pagamento_id": 9
    },
    {
        "valor": Decimal('220.00'),
        "data": date(2025, 1, 10),
        "hora": time(17, 45),
        "antecipacao": True,
        "active": False,
        "pagamento_id": 10
    }
]

for dados in recebimentos:
    recebimento = Recebimento(**dados)
    session.add(recebimento)
#endregion
#region Retirada
retiradas = [
    {
        "data": date(2025, 1, 1),
        "hora": time(12, 30),
        "nome_cliente": "João Silva",
        "active": True,
        "restaurante_id": 1,
        "ordem_pagamento_id": 1
    },
    {
        "data": date(2025, 1, 2),
        "hora": time(14, 45),
        "nome_cliente": "Maria Oliveira",
        "active": True,
        "restaurante_id": 2,
        "ordem_pagamento_id": 2
    },
    {
        "data": date(2025, 1, 3),
        "hora": time(16, 00),
        "nome_cliente": "Carlos Pereira",
        "active": True,
        "restaurante_id": 3,
        "ordem_pagamento_id": 3
    },
    {
        "data": date(2025, 1, 4),
        "hora": time(10, 15),
        "nome_cliente": "Ana Costa",
        "active": True,
        "restaurante_id": 4,
        "ordem_pagamento_id": 4
    },
    {
        "data": date(2025, 1, 5),
        "hora": time(18, 30),
        "nome_cliente": "Pedro Almeida",
        "active": True,
        "restaurante_id": 5,
        "ordem_pagamento_id": 5
    },
    {
        "data": date(2025, 1, 6),
        "hora": time(11, 00),
        "nome_cliente": "Cláudia Santos",
        "active": True,
        "restaurante_id": 6,
        "ordem_pagamento_id": 6
    },
    {
        "data": date(2025, 1, 7),
        "hora": time(13, 30),
        "nome_cliente": "Lucas Lima",
        "active": True,
        "restaurante_id": 7,
        "ordem_pagamento_id": 7
    },
    {
        "data": date(2025, 1, 8),
        "hora": time(9, 00),
        "nome_cliente": "Fernanda Rocha",
        "active": True,
        "restaurante_id": 8,
        "ordem_pagamento_id": 8
    },
    {
        "data": date(2025, 1, 9),
        "hora": time(15, 00),
        "nome_cliente": "Rafael Souza",
        "active": True,
        "restaurante_id": 9,
        "ordem_pagamento_id": 9
    },
    {
        "data": date(2025, 1, 10),
        "hora": time(17, 45),
        "nome_cliente": "Mariana Silva",
        "active": False,
        "restaurante_id": 10,
        "ordem_pagamento_id": 10
    }
]

for dados in retiradas:
    retirada = Retirada(**dados)
    session.add(retirada)
#endregion
#region Delivery
deliveries = [
    {
        "data": date(2025, 1, 1),
        "hora": time(12, 30),
        "nome_cliente": "João Silva",
        "logradouro": "Rua A, 123",
        "bairro": "Centro",
        "cidade_estado": "São Paulo, SP",
        "status": StatusDelivery.EM_ANDAMENTO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 1,
        "ordem_pagamento_id": 1
    },
    {
        "data": date(2025, 1, 2),
        "hora": time(14, 45),
        "nome_cliente": "Maria Oliveira",
        "logradouro": "Avenida B, 456",
        "bairro": "Zona Sul",
        "cidade_estado": "Rio de Janeiro, RJ",
        "status": StatusDelivery.A_CAMINHO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 2,
        "ordem_pagamento_id": 2
    },
    {
        "data": date(2025, 1, 3),
        "hora": time(16, 00),
        "nome_cliente": "Carlos Pereira",
        "logradouro": "Rua C, 789",
        "bairro": "Zona Norte",
        "cidade_estado": "Belo Horizonte, MG",
        "status": StatusDelivery.EM_ANDAMENTO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 3,
        "ordem_pagamento_id": 3
    },
    {
        "data": date(2025, 1, 4),
        "hora": time(10, 15),
        "nome_cliente": "Ana Costa",
        "logradouro": "Praça D, 321",
        "bairro": "Jardim Paulista",
        "cidade_estado": "Curitiba, PR",
        "status": StatusDelivery.A_CONFIRMAR,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 4,
        "ordem_pagamento_id": 4
    },
    {
        "data": date(2025, 1, 5),
        "hora": time(18, 30),
        "nome_cliente": "Pedro Almeida",
        "logradouro": "Rua E, 654",
        "bairro": "Vila Progresso",
        "cidade_estado": "Fortaleza, CE",
        "status": StatusDelivery.REJEITADO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 5,
        "ordem_pagamento_id": 5
    },
    {
        "data": date(2025, 1, 6),
        "hora": time(11, 00),
        "nome_cliente": "Cláudia Santos",
        "logradouro": "Avenida F, 987",
        "bairro": "Centro",
        "cidade_estado": "Salvador, BA",
        "status": StatusDelivery.EM_ANDAMENTO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 6,
        "ordem_pagamento_id": 6
    },
    {
        "data": date(2025, 1, 7),
        "hora": time(13, 30),
        "nome_cliente": "Lucas Lima",
        "logradouro": "Rua G, 135",
        "bairro": "Vila Nova",
        "cidade_estado": "Recife, PE",
        "status": StatusDelivery.A_CONFIRMAR,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 7,
        "ordem_pagamento_id": 7
    },
    {
        "data": date(2025, 1, 8),
        "hora": time(9, 00),
        "nome_cliente": "Fernanda Rocha",
        "logradouro": "Rua H, 246",
        "bairro": "Bairro do Sol",
        "cidade_estado": "Porto Alegre, RS",
        "status": StatusDelivery.A_CAMINHO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 8,
        "ordem_pagamento_id": 8
    },
    {
        "data": date(2025, 1, 9),
        "hora": time(15, 00),
        "nome_cliente": "Rafael Souza",
        "logradouro": "Avenida I, 369",
        "bairro": "Parque Central",
        "cidade_estado": "Manaus, AM",
        "status": StatusDelivery.EM_ANDAMENTO,  # Alterado para usar o Enum
        "active": True,
        "restaurante_id": 9,
        "ordem_pagamento_id": 9
    },
    {
        "data": date(2025, 1, 10),
        "hora": time(17, 45),
        "nome_cliente": "Mariana Silva",
        "logradouro": "Rua J, 471",
        "bairro": "Caiçara",
        "cidade_estado": "Vitória, ES",
        "status": StatusDelivery.A_CONFIRMAR,  # Alterado para usar o Enum
        "active": False,
        "restaurante_id": 10,
        "ordem_pagamento_id": 10
    }
]

for dados in deliveries:
    delivery = Delivery(**dados)
    session.add(delivery)
#endregion
#region Ocupação
ocupacoes = [
    {
        "valor_total": Decimal("100.00"),
        "data": date(2025, 1, 1),
        "hora": time(12, 30),
        "status": True,
        "active": True,
        "mesa_id": 1,
        "ordem_pagamento_id": 1
    },
    {
        "valor_total": Decimal("150.50"),
        "data": date(2025, 1, 2),
        "hora": time(14, 45),
        "status": False,
        "active": True,
        "mesa_id": 2,
        "ordem_pagamento_id": 2
    },
    {
        "valor_total": Decimal("120.75"),
        "data": date(2025, 1, 3),
        "hora": time(16, 00),
        "status": True,
        "active": True,
        "mesa_id": 3,
        "ordem_pagamento_id": 3
    },
    {
        "valor_total": Decimal("200.00"),
        "data": date(2025, 1, 4),
        "hora": time(10, 15),
        "status": False,
        "active": True,
        "mesa_id": 4,
        "ordem_pagamento_id": 4
    },
    {
        "valor_total": Decimal("80.25"),
        "data": date(2025, 1, 5),
        "hora": time(18, 30),
        "status": True,
        "active": True,
        "mesa_id": 5,
        "ordem_pagamento_id": 5
    },
    {
        "valor_total": Decimal("90.40"),
        "data": date(2025, 1, 6),
        "hora": time(11, 00),
        "status": True,
        "active": True,
        "mesa_id": 6,
        "ordem_pagamento_id": 6
    },
    {
        "valor_total": Decimal("110.10"),
        "data": date(2025, 1, 7),
        "hora": time(13, 30),
        "status": False,
        "active": True,
        "mesa_id": 7,
        "ordem_pagamento_id": 7
    },
    {
        "valor_total": Decimal("130.30"),
        "data": date(2025, 1, 8),
        "hora": time(9, 00),
        "status": True,
        "active": True,
        "mesa_id": 8,
        "ordem_pagamento_id": 8
    },
    {
        "valor_total": Decimal("140.55"),
        "data": date(2025, 1, 9),
        "hora": time(15, 00),
        "status": True,
        "active": True,
        "mesa_id": 9,
        "ordem_pagamento_id": 9
    },
    {
        "valor_total": Decimal("160.80"),
        "data": date(2025, 1, 10),
        "hora": time(17, 45),
        "status": False,
        "active": False,
        "mesa_id": 10,
        "ordem_pagamento_id": 10
    }
]

# Inserindo as ocupações no banco
for dados in ocupacoes:
    ocupacao = Ocupacao(**dados)
    session.add(ocupacao)

#endregion
#region ItemRetirada
itens_retirada = [
    ItemRetirada(
        retirada_id=1,
        customizacao_id=1,
        funcionario_id=1,
        produto_id=1,
        valor=Decimal('5.50'),
        observacao='Produto retirado com sucesso.',
        peso=Decimal('0.35'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=2,
        customizacao_id=2,
        funcionario_id=2,
        produto_id=2,
        valor=Decimal('15.00'),
        observacao='Cliente escolheu pão com gergelim.',
        peso=Decimal('0.45'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=3,
        customizacao_id=3,
        funcionario_id=3,
        produto_id=3,
        valor=Decimal('30.00'),
        observacao='Pizza pronta, retirado pelo cliente.',
        peso=Decimal('0.8'),
        pago=False
    ),
    ItemRetirada(
        retirada_id=4,
        customizacao_id=4,
        funcionario_id=4,
        produto_id=4,
        valor=Decimal('10.00'),
        observacao='Sorvete com cobertura de chocolate.',
        peso=Decimal('0.5'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=5,
        customizacao_id=5,
        funcionario_id=5,
        produto_id=5,
        valor=Decimal('12.50'),
        observacao='Salada de frango retirada.',
        peso=Decimal('0.6'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=6,
        customizacao_id=6,
        funcionario_id=6,
        produto_id=6,
        valor=Decimal('18.00'),
        observacao='Espaguete retirado pelo cliente.',
        peso=Decimal('0.7'),
        pago=False
    ),
    ItemRetirada(
        retirada_id=7,
        customizacao_id=7,
        funcionario_id=7,
        produto_id=7,
        valor=Decimal('20.00'),
        observacao='Retirada do frango grelhado com legumes.',
        peso=Decimal('0.9'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=8,
        customizacao_id=8,
        funcionario_id=8,
        produto_id=8,
        valor=Decimal('35.00'),
        observacao='Salmão retirado.',
        peso=Decimal('1.0'),
        pago=True
    ),
    ItemRetirada(
        retirada_id=9,
        customizacao_id=9,
        funcionario_id=9,
        produto_id=9,
        valor=Decimal('8.00'),
        observacao='Bolo de cenoura retirado.',
        peso=Decimal('0.4'),
        pago=False
    ),
    ItemRetirada(
        retirada_id=10,
        customizacao_id=10,
        funcionario_id=10,
        produto_id=10,
        valor=Decimal('6.00'),
        observacao='Suco de laranja retirado.',
        peso=Decimal('0.3'),
        pago=True
    )
]

with conexao.session as session:
    session.add_all(itens_retirada)
    session.commit()
#endregion
#region ItemDelivery
itens_delivery = [
    ItemDelivery(
        delivery_id=1,
        customizacao_id=1,
        funcionario_id=1,
        produto_id=1,
        valor=Decimal('5.50'),
        observacao='Produto entregue com sucesso.',
        peso=Decimal('0.35'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=2,
        customizacao_id=2,
        funcionario_id=2,
        produto_id=2,
        valor=Decimal('15.00'),
        observacao='Hambúrguer com queijo e bacon entregue.',
        peso=Decimal('0.45'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=3,
        customizacao_id=3,
        funcionario_id=3,
        produto_id=3,
        valor=Decimal('30.00'),
        observacao='Pizza entregada com molho extra.',
        peso=Decimal('0.8'),
        pago=False
    ),
    ItemDelivery(
        delivery_id=4,
        customizacao_id=4,
        funcionario_id=4,
        produto_id=4,
        valor=Decimal('10.00'),
        observacao='Sorvete entregue com calda de morango.',
        peso=Decimal('0.5'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=5,
        customizacao_id=5,
        funcionario_id=5,
        produto_id=5,
        valor=Decimal('12.50'),
        observacao='Salada de frango entregue.',
        peso=Decimal('0.6'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=6,
        customizacao_id=6,
        funcionario_id=6,
        produto_id=6,
        valor=Decimal('18.00'),
        observacao='Espaguete à bolonhesa entregue.',
        peso=Decimal('0.7'),
        pago=False
    ),
    ItemDelivery(
        delivery_id=7,
        customizacao_id=7,
        funcionario_id=7,
        produto_id=7,
        valor=Decimal('20.00'),
        observacao='Frango grelhado entregue.',
        peso=Decimal('0.9'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=8,
        customizacao_id=8,
        funcionario_id=8,
        produto_id=8,
        valor=Decimal('35.00'),
        observacao='Salmão grelhado entregue.',
        peso=Decimal('1.0'),
        pago=True
    ),
    ItemDelivery(
        delivery_id=9,
        customizacao_id=9,
        funcionario_id=9,
        produto_id=9,
        valor=Decimal('8.00'),
        observacao='Bolo de cenoura entregue.',
        peso=Decimal('0.4'),
        pago=False
    ),
    ItemDelivery(
        delivery_id=10,
        customizacao_id=10,
        funcionario_id=10,
        produto_id=10,
        valor=Decimal('6.00'),
        observacao='Suco de laranja entregue.',
        peso=Decimal('0.3'),
        pago=True
    )
]

with conexao.session as session:
    session.add_all(itens_delivery)
    session.commit()
#endregion
#region ItemMesa
itens_mesa = [
    ItemMesa(
        ocupacao_id=1,
        customizacao_id=1,
        funcionario_id=1,
        produto_id=1,
        valor=Decimal('5.50'),
        observacao='Produto servido na mesa.',
        peso=Decimal('0.35'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=2,
        customizacao_id=2,
        funcionario_id=2,
        produto_id=2,
        valor=Decimal('15.00'),
        observacao='Hambúrguer servido com bacon.',
        peso=Decimal('0.45'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=3,
        customizacao_id=3,
        funcionario_id=3,
        produto_id=3,
        valor=Decimal('30.00'),
        observacao='Pizza com molho extra servida.',
        peso=Decimal('0.8'),
        pago=False
    ),
    ItemMesa(
        ocupacao_id=4,
        customizacao_id=4,
        funcionario_id=4,
        produto_id=4,
        valor=Decimal('10.00'),
        observacao='Sorvete servido com calda.',
        peso=Decimal('0.5'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=5,
        customizacao_id=5,
        funcionario_id=5,
        produto_id=5,
        valor=Decimal('12.50'),
        observacao='Salada de frango servida.',
        peso=Decimal('0.6'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=6,
        customizacao_id=6,
        funcionario_id=6,
        produto_id=6,
        valor=Decimal('18.00'),
        observacao='Espaguete à bolonhesa servido.',
        peso=Decimal('0.7'),
        pago=False
    ),
    ItemMesa(
        ocupacao_id=7,
        customizacao_id=7,
        funcionario_id=7,
        produto_id=7,
        valor=Decimal('20.00'),
        observacao='Frango grelhado servido.',
        peso=Decimal('0.9'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=8,
        customizacao_id=8,
        funcionario_id=8,
        produto_id=8,
        valor=Decimal('35.00'),
        observacao='Salmão grelhado servido.',
        peso=Decimal('1.0'),
        pago=True
    ),
    ItemMesa(
        ocupacao_id=9,
        customizacao_id=9,
        funcionario_id=9,
        produto_id=9,
        valor=Decimal('8.00'),
        observacao='Bolo de cenoura servido.',
        peso=Decimal('0.4'),
        pago=False
    ),
    ItemMesa(
        ocupacao_id=10,
        customizacao_id=10,
        funcionario_id=10,
        produto_id=10,
        valor=Decimal('6.00'),
        observacao='Suco de laranja servido.',
        peso=Decimal('0.3'),
        pago=True
    )
]

with conexao.session as session:
    session.add_all(itens_mesa)
    session.commit()
#endregion











