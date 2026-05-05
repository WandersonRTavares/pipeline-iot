import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# 🔹 Conexão com o banco
engine = create_engine('postgresql://postgres:1234@localhost:5432/iot_db')

# 🔹 Função para carregar dados
def load_data(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", engine)

# 🔹 Título
st.title('📊 Dashboard de Temperaturas IoT')

# 🔹 SIDEBAR (filtro simples)
st.sidebar.title("Filtros")

# ==============================
# 🔥 MÉTRICA PRINCIPAL
# ==============================
df1 = load_data('avg_temp_por_dispositivo')

st.header('🌡️ Temperatura Média')

st.metric(
    label="Temperatura Média Geral",
    value=f"{df1['avg_temp'].mean():.2f} °C"
)

# ==============================
# 📊 GRÁFICO 1
# ==============================
st.header('Média de Temperatura por Dispositivo')

fig1 = px.bar(
    df1,
    x='device',
    y='avg_temp',
    text_auto=True,
    color='avg_temp'
)

st.plotly_chart(fig1)

# ==============================
# 📈 GRÁFICO 2
# ==============================
st.header('Leituras por Hora')

df2 = load_data('leituras_por_hora')

fig2 = px.line(
    df2,
    x='hora',
    y='contagem'
)

st.plotly_chart(fig2)

# ==============================
# 📉 GRÁFICO 3
# ==============================
st.header('Temp Max e Min por Dia')

df3 = load_data('temp_max_min_por_dia')

fig3 = px.line(
    df3,
    x='data',
    y=['temp_max', 'temp_min']
)

st.plotly_chart(fig3)
