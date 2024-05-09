# Com uma visão mensal
#faturamento por unidade… 
# tipo de produto mais vendido, contribuição por filial,
#Desempenho das forma de pagamento…
#Como estão as avaliações das filiais?

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

dados = pd.read_csv("Power_BI\\21_PowerBI_com_Python\\supermarket_sales.csv", sep=";")
dados["Date"] = pd.to_datetime(dados["Date"])
dados = dados.sort_values("Date")

dados["Month"] = dados["Date"].dt.strftime('%Y-%m')
month = st.sidebar.selectbox("Mês", dados["Month"].unique())

df_filtered = dados[dados["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Date", y="Product line", 
                  color="City", title="Faturamento por tipo de produto",
                  orientation="h")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total",
                   title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)
