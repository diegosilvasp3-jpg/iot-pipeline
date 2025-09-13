# Pipeline de Dados IoT com Docker

## Descrição
Projeto que processa leituras de temperatura de dispositivos IoT e exibe um dashboard interativo usando Streamlit. O pipeline utiliza Docker para o PostgreSQL e pgAdmin.

## Estrutura do Projeto
- `data/temperature_readings.csv`: CSV com leituras de temperatura.
- `src/ingest.py`: Script para ler CSV e gravar no PostgreSQL.
- `src/dashboard.py`: Dashboard interativo com Streamlit.
- `docker-compose.yml`: Configuração dos containers PostgreSQL e pgAdmin.

## Pré-requisitos
- Python 3.9+  
- Docker  
- Git  

## Como Rodar

1. Ativar o ambiente virtual:
```powershell
.\.venv\Scripts\activate
Instalar dependências:

powershell
Copiar código
pip install -r requirements.txt
Rodar containers Docker:

powershell
Copiar código
docker compose up -d
Processar dados e inserir no PostgreSQL:

powershell
Copiar código
python src\ingest.py
Executar o dashboard:

powershell
Copiar código
streamlit run src\dashboard.py

2. Instalar dependências: 
poweshel pip install -r requirements.txt

3. Rodar containers Docker:
docker compose up -d

4. Processar dados e inserir no PostgreSQL:
python src\ingest.py

5. Executar dashboard: streamlit run src\dashboard.py

Views SQL Criadas

No PostgreSQL, foram criadas as seguintes views:

Média de temperatura por dispositivo

CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) AS avg_temp
FROM temperature_readings
GROUP BY device_id;


Contagem de leituras por hora

CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM reading_ts::timestamp) AS hora,
       COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;


Temperaturas máximas e mínimas por dia

CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(reading_ts) AS data,
       MAX(temperature) AS temp_max,
       MIN(temperature) AS temp_min
FROM temperature_readings
GROUP BY DATE(reading_ts)
ORDER BY data;