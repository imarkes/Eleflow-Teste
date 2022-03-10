# BigData Airlines - Test

A Empresa irá atender um novo cliente, a _BigData Airlines_, e você será o engenheiro de dados responsável por fazer a
ingestão de dados e preparar algumas tabelas para os cientistas de dados e analistas de dados.

#### Desenvolvimento:
- O arquivo `main.py` executará o ETL dos dados. Atráves dele será executado os objetivos 1, 2 e 3.
- O Arquivo `database.py` persite os dados em banco de dados SQLite3.
- A DAG será utilizada execução programada da tarefa.
#### Ferramentas para desenvolvimento:
- Python 
- Docker
- Airflow
- Sqlite3

#### Rodando o projeto localmente:
- Se for rodar localmente, cria a variavel: `python -m venv venv`
- Ative a variavel de ambiente: `cd venv\scripts\activate.bat`
- Instale as dependencias: `pip install -r requirements.txt`
- Execute o comando: `python main.py`
#### Rodando o projeto via docker:
- Para rodar via docker: `docker build -t nome_da_imagem`
- Execute a imagem docker `docker run --name nome_container -p 8080:8080 nome_imagem`

### Objetivos:

#### 1- Carregar os dados de VRA
    - Normalizar o cabeçalho para snake case
    - Salvar estes dados

#### 2- Carregar dos dados de AIR_CIA
    - Normalizar o cabeçalho para snake case
    - Separar a coluna 'ICAO IATA' em duas colunas, seu conteúdo está separado por espaço e pode não conter o código
      IATA, caso não contenha o código IATA, deixe o valor nulo.
    - Salvar estes dados
#### 3- Criar nova tabela aerodromos
    - Através da API [https://rapidapi.com/Active-api/api/airport-info/]() trazer os aeródramos através do código ICAO
      presente nos dados de VRA.
    - Salvar estes dados
#### 4 -Criar as seguintes views (Priorize o uso de SQL para esta parte):
    - Para cada companhia aérea trazer a rota mais utilizada com as seguintes informações:
        - Razão social da companhia aérea
        - Nome Aeroporto de Origem
        - ICAO do aeroporto de origem
        - Estado/UF do aeroporto de origem
        - Nome do Aeroporto de Destino
        - ICAO do Aeroporto de destino
        - Estado/UF do aeroporto de destino
    - Para cada aeroporto trazer a companhia aérea com maior atuação no ano com as seguintes informações:
        - Nome do Aeroporto
        - ICAO do Aeroporto
        - Razão social da Companhia Aérea
        - Quantidade de Rotas à partir daquele aeroporto
        - Quantidade de Rotas com destino àquele aeroporto
        - Quantidade total de pousos e decolagens naquele aeroporto

### Info Desenvolvedor :
- Ivan Marques
- email: i.markes@hotmail.com

