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

# Listas de regiões exemplo
regions = [
    "RONDONIA - RO",
    "MEDIO NORTE - MT",
    "TRIÂNGULO - MG",
    "NORDESTE SP",
    "VALE PARANAPANEMA SP",
    "SUDOESTE - PR",
    "ENTORNO DE BRASILIA",
    "NOROESTE SP",
    "NORTE PR",
    "PLANALTO MÉDIO RS",
    "ALTO DA SERRA RS",
    "SUL - MG",
    "VALE EUROPEU SC",
    "CENTRO OESTE - MG",
    "OESTE PR",
    "ZONA MATA - MG / ES",
    "VENDA INDUSTRIAL",
    "VALE DO ARAGUAIA - MT",
    "SUDOESTE - GO",
    "CAMPOS GERAIS PR",
    "SUL - MT",
    "SUL - MS",
    "C NORTE - TO/SUL PA",
    "PARAGUAY",
    "URUGUAY",
    "NORTE - PA",
    "CHAPADÕES",
    "SUDESTE - GO",
    "SUL TO",
    "SUL RS",
    "OESTE - MT",
    "ALTO PARANAIBA - MG",
    "NORTE - TO/SUL MA",
    "CENTRO - MA",
    "OESTE - BA BARREIRAS",
    "RONDONIA - MT",
    "CHAPADÃO",
    "LESTE - MA",
    "VENDAS DIRETA",
    "LEM - BA",
    "SUL PI",
    "VALE SÃO FRANSCISCO",
    "CW - ZONA MATA-MG/ES",
    "CW - MEDIO NORTE - MT",
    "CW - VL DO ARAGUAIA - MT",
    "CW - ALTO PARANAIBA - MG",
    "CW - SUDOESTE - GO",
    "CW - ENTO. DE BRASILIA",
    "CW - SUL - MG",
    "CW - PARAGUAY",
    "CW CENTRO OESTE - MG",
    "CW - SUL - MT",
    "CW - SUL - MS",
    "CW - TRIÂNGULO - MG",
    "CW - OESTE - MT",
    "CW - TO",
    "CW PARAGUAY",
    "CW - NOROESTE SP",
    "CW ALTO PARANAIBA-MG",
    "CW VL DO ARAGUAIA-MT",
    "CW - NORTE PR",
    "CW - NORDESTE SP",
    "CW - VALE EUROPEU SC",
    "VALE EUROPEU SC",
    "SUDOESTE - PR",
    "MEDIO NORTE - MT",
    "TRIÂNGULO - MG",
    "RONDONIA - MT",
    "OESTE - MT",
    "SUL - MT",
    "NORTE SP",
    "SUDESTE - GO",
    "PLANALTO MÉDIO RS",
    "ALTO DA SERRA RS",
    "URUGUAY",
    "NOROESTE SP",
    "ENTORNO DE BRASILIA",
    "NORTE PR",
    "PARAGUAY",
    "CHAPADÃO",
    "CENTRO OESTE - MG",
    "SUL RS",
    "LESTE - MA",
    "OESTE - BA BARREIRAS",
    "SUDOESTE - GO",
    "CW - CHAPADÃO",
    "CW - OESTE - MT",
    "CW - SUDOESTE - GO",
    "CW - SUDOESTE - PR",
]

# Lista de produtos exemplo
products = [
    "FLEX COMOL",
    "BIO NMT",
    "VITAL BORO POLYOL",
    "VITAL MAGNESIO",
    "VITAL MANGANES",
    "VITAL POTASSIUM",
    "ESTIMULUS AMINOMAX",
    "ESTIMULUS ROOT +",
    "RESISTANCE BAC-F",
    "BIO FIXAN GRAM",
    "RESISTANCE TM",
    "BIOSCAP LIQ",
    "ESTIMULUS EVO",
    "SPREAD MPO",
    "RESISTANCE DRILLFLY",
    "ESTIMULUS ROOT",
    "RESISTANCE GARLIC",
    "BIO TCD",
    "BIO BVB (WP)",
    "VITAL SOLO BORO",
    "VITAL SOLO CALCIO",
    "BIO SOLUB",
    "FLEX CITROLEO",
    "RESISTANCE C CITRUS",
    "BIO BAC T",
    "SPREAD COMBO",
    "RESISTANCE PROTECTOR",
    "VITAL SOLO MAGNESIO",
    "VITAL SOLO ZINCO",
    "SPREAD SIL",
    "VITAL CALCIO",
    "VITAL ZINCO",
    "VITAL SOLO MANGANES",
    "ESTIMULUS GRASS",
    "BIOISA",
    "FLEX S TOTAL",
    "BIOTHREE",
    "BIO DUO",
    "SPREAD LIMPA TANQUE",
    "FLEX MOLIBDENIO 16%",
    "FLEX AMINO",
    "BIO BAC S",
    "FLEX N MASTER 32",
    "BIOFIXA LEG",
    "SOLO BORO",
    "BIO MTZ",
    "BIOFIXAN GRAM (T)",
    "VITAL COBRE",
    "RESIST STOOT",
    "ESTIMULUS IMMUNE",
    "SPREAD WEET ADJUVANTE",
    "SPREAD ALVO - COADYUVANTE - PY",
    "BIO PHAKO",
    "ESTIMULUS AMINOMAX D",
    "RESISTANCE BAC F",
    "CALDO BACTERIANO PARA PRODUCAO RALBIT",
    "CW RESIST INDUCTOR",
    "CW RESIST STOOT",
    "CW ECOBALS",
    "CW ECOTETRAN",
    "CW ECOAZOTO GRAM (T)",
    "CW FORCE RAIZ",
    "CW RESIST PROTECTOR",
    "CW TOP MULT ADJUVANTE",
    "CW TOP CERIUM ADJUVANTE",
    "CW FOLIUM BORO POLYOL",
    "CW FOLIUM POTASSIUM FERTILIZANTE MINERAL",
    "CW FORCE GRAIN",
    "CW FORCE RAIZ+",
    "CW FORCE BETAG",
    "CW RESIST DUAL",
    "CW SOLO CALCIO",
    "CW SOLO MAGNESIO",
    "CW ECO NEMA",
    "CW SOLO BORO",
    "CW FLEX N MASTER 32",
    "CW RESIST STRATT",
    "CW ECO TCH",
    "CW ECOBACI T",
    "CW ECO TRI",
    "CW ECO RAZTO",
    "CW FOLIUM ZINCO",
    "CW FLEX COMOL",
    "CW ECO TTRN",
    "CW FLEX CITROLEO",
    "CW FLEX MOLIBDENIO 16%",
    "CW ECO DUE",
    "CW FOLIUM MANGANES",
    "CW TOP SIL",
    "CW ECOCORDY",
    "CW TOP MULT",
    "CW TOP CERIUM",
    "CW FORCE AMINO",
    "CW FOLIUM POTASSIUM",
    "CW ECO CLAVY",
    "CW SOLO ZINCO",
    "CW TOP SIL",
    "CW TOP CERIUM",
    "CW RESIST INDUCT",
    "CW FORCE GRAIN",
    "CW SOLO MANGANES",
    "CW TOP ROOF ADJUVANTE",
    "CW FOLIUM CALCIO",
    "CW FLEX AMINO",
    "CW FOLIUM CÁLCIO",
    "CW FOLIUM BORO",
    "BIO PHAKO 6X2",
    "SPREAD COMBO ADJUVANTE",
    "SPREAD SIL ADJUVANTE",
    "ESTIMULUS ROOT + UY FERTILIZANTE MINERAL",
    "ESTIMULUS GRASS UY FERTILIZANTE MINERAL",
    "ESTIMU MAX-AMI UY D FERTILIZANTE MINERAL",
    "VITAL ZINC - UY FERTILIZANTE MINERAL",
    "VITAL BORO POLYO UY FERTILIZANTE MINERAL",
    "BIO BAC T 12 X 1",
    "BIO BAC T 4 X 5",
    "SPREAD MPO ADJUVANTE",
    "BIO AMILOFACIENS 12X1",
    "SPREAD COMBO - COADYUVANTE - PY",
    "RESIST. DRILLFLY-PY FERTILIZANTE MINERAL",
    "VITAL BORO POLYO PY FERTILIZANTE MINERAL",
    "VITAL POTASSIUM-PY FERTILIZANTE MINERAL",
    "VITAL SOLO BORO PY FERTILIZANTE MINERAL",
    "ROOT + PY FERTILIZANTE MINERAL",
    "BIO AMILOFACIENS 4X5",
    "BIO TRICO 12X1",
    "BIO TRICO 4X5",
    "CW ECO VASTAX 6X2",
    "CW ECO NEMAXY 12X1",
    "CW ECO TRICO 12X1",
    "CW ECO NEMAXY 4X5",
    "CW ECO TRICO 4X5",
    "BIO MTZ 12 X 1",
    "RESISTANCE BAC-F UY FERTILIZANTE MINERAL",
    "SPREAD LIMPA TANQUE ADJUVANTE",
    "ESTIMULUS IMMUNE PY FERTILIZANTE MINERAL",
    "RESISTANCE BAC-F PY FERTILIZANTE MINERAL",
    "FLEX COMOL - PY FERTILIZANTE MINERAL",
    "RESISTANCE TM - UY FERTILIZANTE MINERAL",
    "BIO PHAKO",
    "BIO BAC T",
    "BIO TRICO",
    "BIO AMILOFACIENS",
    "BIO MTZ",
    "CW ECO NEMAXY",
    "CW ECO TRICO",
    "CW ECO VASTAX",
    "CW TOP SIL ADJUVANTE",
    "BIO AMILOFACIENS",
    "CW ECO NEMAXY",
    "ISACONTROL",
    "SPREAD OIL PLUS",
    "BIOBVB - INSECTICIDA MICROBIOLOGICO - PY",
]

# Lista de especialidades exemplo
specialities = ["SIM", "NÃO"]

# Lista de embalagens exemplo
packages = ["12 X 1", "4 X 5", "BB 20", "10 X 1", "12X1"]


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
    especialidades: str
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
        quantidade = randint(1, 1000)
        valor_unitario = round(uniform(5.0, 500.0), 2)
        valor_item = round(quantidade * valor_unitario, 2)

        business = {
            "filial": choice(filiais),
            "data_negociacao": data_negociacao,
            "nf": fake.numerify(text="######"),
            "data_vencimento": data_vencimento,
            "razao_social_parceiro": fake.company(),
            "regiao_parceiro": choice(regions),
            "coordenacao": fake.job(),
            "cidade": fake.city(),
            "uf": fake.state_abbr(),
            "descricao_produto": choice(products),
            "especialidades": choice(specialities),
            "biologico": fake.boolean(chance_of_getting_true=50),
            "embalagem": choice(packages),
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
