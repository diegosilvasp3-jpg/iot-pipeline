import os
import pandas as pd
import streamlit as st
import plotly.express as px
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB = os.getenv("POSTGRES_DB")
USER = os.getenv("POSTGRES_USER")
PWD = os.getenv("POSTGRES_PASSWORD")
HOST = os.getenv("POSTGRES_HOST")
PORT = os.getenv("POSTGRES_PORT")

engine = create_engine(f"postgresql+psycopg2://{USER}:{PWD}@{HOST}:{PORT}/{DB}")

st.title("📊 Dashboard de Temperaturas IoT")

@st.cache_data
def load_view(view_name):
    return pd.read_sql(f"SELECT * FROM {view_name}", con=engine)

try:
    # 1️⃣ Gráfico: Média de temperatura por sensor
    st.header("Média de Temperatura por Dispositivo")
    df_avg_temp = load_view("avg_temp_por_dispositivo")
    fig1 = px.bar(df_avg_temp, x="device_id", y="avg_temp", labels={"avg_temp": "Temperatura Média (°C)"})
    st.plotly_chart(fig1)

    # 2️⃣ Gráfico: Leituras por hora do dia
    st.header("Leituras por Hora do Dia")
    df_leituras_hora = load_view("leituras_por_hora")
    fig2 = px.line(df_leituras_hora, x="hora", y="contagem", markers=True)
    st.plotly_chart(fig2)

    # 3️⃣ Gráfico: Temperaturas máxima e mínima por dia
    st.header("Temperaturas Máximas e Mínimas por Dia")
    df_temp_max_min = load_view("temp_max_min_por_dia")
    fig3 = px.line(df_temp_max_min, x="data", y=["temp_max", "temp_min"])
    st.plotly_chart(fig3)

except Exception as e:
    st.error(f"Erro ao conectar ou carregar dados: {e}")
