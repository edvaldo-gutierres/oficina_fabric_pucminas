_Projeto desenvolvido para fins de treinamento e simulação de integração de APIs._

# Simulação de API de Negócios

Esta API simula dados de negócios para um cenário de integração e análise de dados. A API é desenvolvida com **FastAPI** e utiliza **Faker** para gerar dados falsos como regiões, produtos, especialidades e embalagens.

## Requisitos

Antes de começar, certifique-se de que seu sistema atende aos seguintes requisitos:

- **Windows Subsystem for Linux (WSL)**: Este projeto foi desenvolvido e testado utilizando o WSL, permitindo um ambiente Linux dentro do Windows.
  - [Guia de Instalação do WSL](https://docs.microsoft.com/pt-br/windows/wsl/install)

- **Python 3.11.5 ou superior**: O projeto requer o Python 3.11.5 ou uma versão superior para funcionar corretamente. Certifique-se de que essa versão do Python está instalada e ativa no seu ambiente.
  - [Download Python](https://www.python.org/downloads/)

- **Poetry**: Para gerenciamento de dependências e ambientes virtuais.
  - [Guia de Instalação do Poetry](https://python-poetry.org/docs/#installation)

- **Git**: Para clonar o repositório do projeto.
  - [Guia de Instalação do Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)


## Instalação

### 1. Clone o repositório

Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/edvaldo-gutierres/oficina_fabric_pucminas
```

### 2. Navegue até a pasta do projeto

```bash
cd oficina_fabric_pucminas
```

### 3. Ative o ambiente virtual do Poetry

O **Poetry** já gerencia o ambiente virtual para você. Para ativar o ambiente virtual e iniciar a interação com o projeto, execute o comando abaixo:

```bash
poetry shell
```

### 4. Instale as dependências com Poetry

Com o **Poetry** instalado, basta rodar o seguinte comando para instalar todas as dependências do projeto:

```bash
poetry install
```

## Executando a API

Após instalar as dependências, você pode rodar a API localmente usando o **Uvicorn**.

Execute o seguinte comando dentro do ambiente virtual:

```bash
uvicorn api.gera_dados_venda:app --reload
```

Caso a porta 8000 já esteve sendo utilizado, para setar outra porta execute o comando:

```bash
uvicorn api.gera_dados_venda:app --reload --port 8080
```

Este comando irá iniciar um servidor de desenvolvimento que será automaticamente atualizado sempre que você modificar o código.

### Acessando a API

Com o servidor rodando, acesse a API em um navegador ou ferramenta como o **Postman** através do seguinte endereço:

- **Endpoint de Negócios**: `http://127.0.0.1:8080/business`

Esse endpoint irá retornar uma lista de 10 negócios com dados simulados, incluindo:

- Filial
- Data de Negociação
- Nota Fiscal
- Data de Vencimento
- Parceiro (Razão Social)
- Região do Parceiro
- Coordenação
- Cidade, UF
- Produto
- Especialidades
- Biológico
- Embalagem
- Quantidade
- Valor Unitário
- Valor Total do Item

## Personalizando a Geração de Dados

Você pode personalizar o número de registros retornados alterando o valor passado na função `generate_fake_business_data` no arquivo `main.py`.

Exemplo:

```python
return generate_fake_business_data(20)  # Gera 20 registros falsos
```

## Encerrando a API

Para parar a execução da API, pressione `Ctrl + C` no terminal onde ela está sendo executada.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

---

