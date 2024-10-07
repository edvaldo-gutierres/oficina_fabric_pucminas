from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from faker import Faker
from random import choice, randint, uniform
from datetime import date, timedelta

# Inicializa o Faker
fake = Faker("pt_BR")

# Inicializa o FastAPI
app = FastAPI()

# Lista de filiais exemplo
filiais = ["Filial01", "Filial02", "Filial03", "Filial04"]

# Mapeamento de clientes para regiões
cliente_regiao = {
    "Agroverde Comércio de Insumos Ltda.": "Amazônia Ocidental",
    "Grãos do Cerrado S.A.": "Centro-Oeste Soja",
    "Fazenda Vale do Sol Agropecuária Ltda.": "Vale do Paraíba",
    "Cooperativa Agropecuária Central": "Planalto Central",
    "Terra Fértil Insumos Agrícolas Ltda.": "Mato Grosso Agro",
    "Plantio Forte Agroindústria S.A.": "Chapada Diamantina",
    "Grupo AgroAliança Ltda.": "Sertão Nordestino",
    "Campo Belo Agronegócios Ltda.": "Região do Cariri",
    "Cereais do Brasil Comercial Ltda.": "Campos Gerais",
    "Produtores Unidos do Norte S.A.": "Costa Verde",
    "AgroTech Soluções Agrícolas Ltda.": "Pampa Gaúcho",
    "Nutrisoja Agronegócios S.A.": "Serra Gaúcha",
    "AgroLíder Distribuidora Ltda.": "Pantanal Mato-Grossense",
    "Colheita Farta Agro Ltda.": "Chapada dos Veadeiros",
    "Plantações Estrela do Sul S.A.": "Vale do São Francisco",
}

# Lista de produtos exemplo
products = [
    "Ureia",
    "Superfosfato Simples",
    "Superfosfato Triplo",
    "Cloreto de Potássio",
    "Sulfato de Amônio",
    "Nitrato de Amônio",
    "MAP (Fosfato Monoamônico)",
    "DAP (Fosfato Diamônico)",
    "Fosfato Natural",
    "Calcário Dolomítico",
    "Gesso Agrícola",
    "Sulfo-Magnesiano",
    "Sulfato de Zinco",
    "Sulfato de Cobre",
    "Boro Granulado",
]

# Lista de produtos por coordenação de vendas
produto_coordenacao = {
    "Ureia": "Vendas de Fertilizantes",
    "Superfosfato Simples": "Vendas de Fertilizantes",
    "Superfosfato Triplo": "Vendas de Fertilizantes",
    "Cloreto de Potássio": "Vendas de Fertilizantes",
    "Sulfato de Amônio": "Vendas de Fertilizantes",
    "Nitrato de Amônio": "Vendas de Fertilizantes",
    "MAP (Fosfato Monoamônico)": "Vendas de Fertilizantes",
    "DAP (Fosfato Diamônico)": "Vendas de Fertilizantes",
    "Fosfato Natural": "Vendas de Fertilizantes",
    "Sulfato de Zinco": "Vendas de Fertilizantes",
    "Sulfato de Cobre": "Vendas de Fertilizantes",
    "Boro Granulado": "Vendas de Fertilizantes",
    "Calcário Dolomítico": "Vendas Agropecuária",
    "Gesso Agrícola": "Vendas Agropecuária",
    "Sulfo-Magnesiano": "Vendas Agropecuária",
    "Adubo Orgânico": "Vendas Agropecuária",
    "Calcário Agrícola": "Vendas Agropecuária",
    "Sementes de Milho": "Vendas Agropecuária",
    "Sementes de Soja": "Vendas Agropecuária",
    "Sementes de Trigo": "Vendas Agropecuária",
    "Ração Animal": "Vendas Agropecuária",
    "Silagem de Milho": "Vendas Agropecuária",
    "Sorgo Forrageiro": "Vendas Agropecuária",
    "Farelo de Soja": "Vendas Agropecuária",
    "Farelo de Trigo": "Vendas Agropecuária",
    "Inoculante para Pastagem": "Vendas Agropecuária",
}

# Mapeamento de produtos para embalagens
produto_embalagem = {
    "Ureia": ["Saco de 50 kg", "Big Bag de 500 kg", "Big Bag de 1.000 kg"],
    "Superfosfato Simples": ["Saco de 50 kg", "Big Bag de 500 kg"],
    "Superfosfato Triplo": ["Saco de 50 kg", "Big Bag de 1.000 kg"],
    "Cloreto de Potássio": ["Saco de 25 kg", "Saco de 50 kg", "Big Bag de 1.500 kg"],
    "Sulfato de Amônio": ["Saco de 50 kg", "Big Bag de 1.000 kg"],
    "Nitrato de Amônio": ["Saco de 25 kg", "Saco de 50 kg"],
    "MAP (Fosfato Monoamônico)": ["Saco de 50 kg", "Big Bag de 1.500 kg"],
    "DAP (Fosfato Diamônico)": ["Saco de 50 kg", "Big Bag de 1.000 kg"],
    "Fosfato Natural": ["Saco de 50 kg", "Big Bag de 500 kg"],
    "Calcário Dolomítico": ["Big Bag de 1.000 kg", "Big Bag de 1.500 kg"],
    "Gesso Agrícola": ["Saco de 50 kg", "Big Bag de 1.000 kg"],
    "Sulfo-Magnesiano": ["Saco de 25 kg", "Balde de 10 kg"],
    "Sulfato de Zinco": ["Saco de 25 kg", "Saco de 50 kg"],
    "Sulfato de Cobre": ["Saco de 25 kg", "Saco de 50 kg"],
    "Boro Granulado": ["Saco de 25 kg", "Galão de 5 litros"],
}

# Lista de embalagens exemplo
packages = [
    "Saco de 25 kg",
    "Saco de 50 kg",
    "Big Bag de 500 kg",
    "Big Bag de 1.000 kg",
    "Big Bag de 1.500 kg",
    "Tambor de 200 litros",
    "Galão de 20 litros",
    "Galão de 5 litros",
    "Balde de 10 kg",
]

# Mapeamento de regiões para cidades
regiao_cidade = {
    "Amazônia Ocidental": ["Manaus", "Porto Velho", "Rio Branco"],
    "Centro-Oeste Soja": ["Goiânia", "Sorriso", "Rio Verde"],
    "Vale do Paraíba": ["São José dos Campos", "Taubaté", "Resende"],
    "Planalto Central": ["Brasília", "Anápolis", "Luziânia"],
    "Mato Grosso Agro": ["Cuiabá", "Rondonópolis", "Lucas do Rio Verde"],
    "Chapada Diamantina": ["Lençóis", "Seabra", "Palmeiras"],
    "Sertão Nordestino": ["Petrolina", "Juazeiro", "Picos"],
    "Região do Cariri": ["Juazeiro do Norte", "Crato", "Barbalha"],
    "Campos Gerais": ["Ponta Grossa", "Castro", "Palmeira"],
    "Costa Verde": ["Angra dos Reis", "Paraty", "Mangaratiba"],
    "Pampa Gaúcho": ["Bagé", "Santana do Livramento", "Dom Pedrito"],
    "Serra Gaúcha": ["Bento Gonçalves", "Caxias do Sul", "Garibaldi"],
    "Pantanal Mato-Grossense": ["Corumbá", "Cáceres", "Poconé"],
    "Chapada dos Veadeiros": ["Alto Paraíso de Goiás", "Cavalcante", "Colinas do Sul"],
    "Vale do São Francisco": ["Petrolina", "Juazeiro", "Sobradinho"],
}

# Mapeamento de regiões para cidades e seus respectivos estados (UF)
regiao_cidade_uf = {
    "Amazônia Ocidental": [
        ("Manaus", "AM"),
        ("Porto Velho", "RO"),
        ("Rio Branco", "AC"),
    ],
    "Centro-Oeste Soja": [("Goiânia", "GO"), ("Sorriso", "MT"), ("Rio Verde", "GO")],
    "Vale do Paraíba": [
        ("São José dos Campos", "SP"),
        ("Taubaté", "SP"),
        ("Resende", "RJ"),
    ],
    "Planalto Central": [("Brasília", "DF"), ("Anápolis", "GO"), ("Luziânia", "GO")],
    "Mato Grosso Agro": [
        ("Cuiabá", "MT"),
        ("Rondonópolis", "MT"),
        ("Lucas do Rio Verde", "MT"),
    ],
    "Chapada Diamantina": [("Lençóis", "BA"), ("Seabra", "BA"), ("Palmeiras", "BA")],
    "Sertão Nordestino": [("Petrolina", "PE"), ("Juazeiro", "BA"), ("Picos", "PI")],
    "Região do Cariri": [
        ("Juazeiro do Norte", "CE"),
        ("Crato", "CE"),
        ("Barbalha", "CE"),
    ],
    "Campos Gerais": [("Ponta Grossa", "PR"), ("Castro", "PR"), ("Palmeira", "PR")],
    "Costa Verde": [("Angra dos Reis", "RJ"), ("Paraty", "RJ"), ("Mangaratiba", "RJ")],
    "Pampa Gaúcho": [
        ("Bagé", "RS"),
        ("Santana do Livramento", "RS"),
        ("Dom Pedrito", "RS"),
    ],
    "Serra Gaúcha": [
        ("Bento Gonçalves", "RS"),
        ("Caxias do Sul", "RS"),
        ("Garibaldi", "RS"),
    ],
    "Pantanal Mato-Grossense": [("Corumbá", "MS"), ("Cáceres", "MT"), ("Poconé", "MT")],
    "Chapada dos Veadeiros": [
        ("Alto Paraíso de Goiás", "GO"),
        ("Cavalcante", "GO"),
        ("Colinas do Sul", "GO"),
    ],
    "Vale do São Francisco": [
        ("Petrolina", "PE"),
        ("Juazeiro", "BA"),
        ("Sobradinho", "BA"),
    ],
}


# Modelo de dados para o negócio
class BusinessData(BaseModel):
    filial: str
    data_negociacao: date
    nf: str
    data_vencimento: date
    razao_social_parceiro: str
    regiao_parceiro: str
    coordenacao: str
    cidade: str
    uf: str
    descricao_produto: str
    biologico: bool
    embalagem: str
    quantidade: int
    valor_unitario: float
    valor_item: float


# Função para gerar dados falsos de negócios
def generate_fake_business_data(num_records: int):
    business_data = []

    for _ in range(num_records):
        data_negociacao = fake.date_this_year()
        data_vencimento = data_negociacao + timedelta(days=randint(30, 60))
        descricao_produto = choice(products)
        coordenacao = produto_coordenacao.get(
            descricao_produto, "Vendas Gerais"
        )  # Associa produto à coordenação
        embalagem = choice(produto_embalagem.get(descricao_produto, ["Saco de 50 kg"]))
        cliente = choice(list(cliente_regiao.keys()))  # Escolhe um cliente
        regiao = cliente_regiao[cliente]  # Associa a região correspondente ao cliente

        # Seleciona cidade e UF juntos para garantir correspondência correta
        cidade, uf = choice(regiao_cidade_uf[regiao])

        quantidade = randint(1, 1000)
        valor_unitario = round(uniform(5.0, 500.0), 2)
        valor_item = round(quantidade * valor_unitario, 2)

        business = {
            "filial": choice(filiais),
            "data_negociacao": data_negociacao,
            "nf": fake.numerify(text="######"),
            "data_vencimento": data_vencimento,
            "razao_social_parceiro": cliente,
            "regiao_parceiro": regiao,
            "coordenacao": coordenacao,
            "cidade": cidade,
            "uf": uf,
            "descricao_produto": descricao_produto,
            "biologico": fake.boolean(chance_of_getting_true=50),
            "embalagem": embalagem,
            "quantidade": quantidade,
            "valor_unitario": valor_unitario,
            "valor_item": valor_item,
        }

        business_data.append(business)

    return business_data


# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "API de vendas rodando!"}


# Endpoint para retornar dados de negócios falsos
@app.get("/business", response_model=List[BusinessData])
def get_business_data():
    return generate_fake_business_data(100)  # Gera 100 registros falsos
