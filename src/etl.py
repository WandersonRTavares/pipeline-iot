import pandas as pd
from sqlalchemy import create_engine

# conexão com banco
engine = create_engine('postgresql://postgres:1234@127.0.0.1:5432/iot_db')

# carregar CSV
df = pd.read_csv('data/IOT-temp.csv')

# padronizar colunas
df.columns = df.columns.str.lower()

# salvar no banco
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("Dados inseridos com sucesso!")
