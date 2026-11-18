import pandas as pd
import streamlit as st
import plotly as pl
import openpyxl



df = pd.read_excel("saeb_aprendizado_territorios-7-2023-EM.xlsx",sheet_name="estados", engine="openpyxl")


st.set_page_config(page_title="Oi janaina",page_icon="😊", layout="wide", initial_sidebar_state="expanded")


st.sidebar.title("Visualizar Dados")

Tipo = ["Tabela", "Graficos"]
visualizacao= st.sidebar.multiselect ("Tipo", Tipo, default=Tipo,help="")

st.title("Oi janaina")
st.text("eu sei que vc queria que eu fizesse a prova namoral, mas me deu um branco e como eu já passei na sua materia, eu vou usar isso aq pra escrever um texto de agradecimento. esse ano foi muito legal e você foi a minha primeira professora preferida, muito obrigado por tudo, foi muito especial e vc faz parte disso")


# deploy