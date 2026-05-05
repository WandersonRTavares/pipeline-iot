# 📊 Pipeline de Dados com IoT e Docker

## 🚀 Descrição do Projeto
Este projeto implementa um pipeline de dados utilizando dispositivos IoT para coleta de temperatura, com processamento em Python, armazenamento em PostgreSQL via Docker e visualização com Streamlit.

---

## 🛠 Tecnologias Utilizadas
- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker
- Streamlit
- Plotly

---

## 📁 Estrutura do Projeto

pipeline-iot/
│
├── data/ # Arquivo CSV (Kaggle)
├── src/
│ ├── etl.py # Script de processamento
│ ├── dashboard.py # Dashboard Streamlit
│
├── requirements.txt
└── README.md


---

## ⚙️ Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/SEU_USUARIO/pipeline-iot.git
cd pipeline-iot
```

### 2. Criar e ativar ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Subir o PostgreSQL com Docker

Se for a primeira vez:

```bash
docker run --name postgres-iot \
-e POSTGRES_PASSWORD=1234 \
-e POSTGRES_DB=iot_db \
-p 5432:5432 \
-d postgres
```

Se o container já existir:

```bash
docker start postgres-iot
```

### 5. Executar o ETL (inserir dados)

```bash
python src/etl.py
```

### 6. Rodar o Dashboard

```bash
streamlit run src/dashboard.py
```

### 7. Acessar no navegador

```
http://localhost:8501

```
## 📊 Dashboard

### Média de Temperatura por Dispositivo
![Média](docs/images/media_temp.jpg)

### Leituras por Hora
![Leituras](docs/images/leituras_hora.jpg)

### Temperatura Máxima e Mínima por Dia
![Temp](docs/images/temp_max_min.jpg)

🔥 Ajuste EXTRA

Verificar dados no banco
docker exec -it postgres-iot psql -U postgres -d iot_db

E dentro do psql:
SELECT COUNT(*) FROM temperature_readings;


📊 Views SQL Criadas

-- Média por dispositivo
CREATE VIEW avg_temp_por_dispositivo AS
SELECT "room_id/id" AS device, AVG(temp) AS avg_temp
FROM temperature_readings
GROUP BY "room_id/id";

-- Leituras por hora
CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS hora,
       COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- Máx e mín por dia
CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(TO_TIMESTAMP(noted_date, 'DD-MM-YYYY HH24:MI')) AS data,
       MAX(temp) AS temp_max,
       MIN(temp) AS temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;
📈 Insights

A temperatura média varia conforme o ambiente (interno/externo)
Horários específicos apresentam maior volume de leitura
Há variações térmicas significativas ao longo dos dias


📦 Fonte dos Dados

Kaggle - Temperature Readings IoT Devices


---

Depois:

```bash
git add README.md
git commit -m "README profissional"
git push


