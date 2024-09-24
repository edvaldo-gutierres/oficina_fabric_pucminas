import requests

# URL da API que será consumida
api_url = "http://127.0.0.1:8080/business"

# Fazendo uma requisição GET para o endpoint da API
response = requests.get(api_url)

# Verificando se a requisição foi bem-sucedida (código 200)
if response.status_code == 200:
    # Convertendo a resposta para JSON
    business_data = response.json()

    # Exibindo os dados de negócios retornados pela API
    print("Dados de Negócios obtidos da API:")
    for business in business_data:
        print(f"Filial: {business['filial']}")
        print(f"Data Negociação: {business['data_negociacao']}")
        print(f"N.F.: {business['nf']}")
        print(f"Data Vencimento: {business['data_vencimento']}")
        print(f"Razão Social: {business['razao_social_parceiro']}")
        print(f"Região: {business['regiao_parceiro']}")
        print(f"Coordenação: {business['coordenacao']}")
        print(f"Cidade: {business['cidade']}, {business['uf']}")
        print(f"Produto: {business['descricao_produto']}")
        print(f"Especialidades: {business['especialidades']}")
        print(f"Biológico: {'Sim' if business['biologico'] else 'Não'}")
        print(f"Embalagem: {business['embalagem']}")
        print(f"Quantidade: {business['quantidade']}")
        print(f"Valor Unitário: {business['valor_unitario']}")
        print(f"Valor Total: {business['valor_item']}")
        print("-" * 40)
else:
    print(f"Erro ao acessar a API. Status Code: {response.status_code}")
