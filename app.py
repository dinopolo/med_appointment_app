# Importando as bibliotecas
import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

st.set_page_config(page_title="Comparecimento em consultas", page_icon = ":hospital:", layout="centered", initial_sidebar_state="expanded")

### Barra Lateral / Sidebar ###

st.sidebar.markdown("**Sobre o Aplicativo Web:**")
st.sidebar.markdown("Este aplicativo web serve para verificar se um paciente vai comparecer à consulta médica ou não, para isso basta preencher todos os campos e clicar em **Verificar** que vai exibir o resultado.")
st.sidebar.markdown("")
st.sidebar.markdown("**Repositório GitHub do Aplicativo Web:**")
st.sidebar.markdown("[Clique Aqui](https://github.com/dinopolo/med_appointment_app)")
###############################

### Aplicativo Web / Web App ###

image = Image.open('consulta.jpg')
st.image(image)

st.title("Comparecimento em consultas médicas")

st.write("### **Preencha os campos abaixo:**")


col1, col2 = st.beta_columns(2)

# Idade
with col1:
    idade = st.slider("Idade do paciente:", 0, 110, 1)

# Dias de antecedência
with col2:
    dias_ate_consulta = st.slider("Dias de antecedência que a consulta foi agendada?", 0, 180, 1)


col3, col4, col5, col6 = st.beta_columns(4)

# Gênero
with col3:
    genero = st.radio("Gênero:", ("Feminino", "Masculino"))
    
    if genero == 'Feminino':
        genero = 0
    else:
        genero = 1

# Auxílio governamental
with col4:
    auxilio_governamental = st.radio("Recebe auxílio?", ("Não", "Sim"))

    if auxilio_governamental == 'Não':
        auxilio_governamental = 0
    else:
        auxilio_governamental = 1

# Hipertensão
with col5:
    hipertensao = st.radio("Tem hipertensão?", ("Não", "Sim"))

    if hipertensao == 'Não':
        hipertensao = 0
    else:
        hipertensao = 1

# Diabetes
with col6:
    diabetes = st.radio("Tem diabetes?", ("Não", "Sim"))

    if diabetes == 'Não':
        diabetes = 0
    else:
        diabetes = 1


col7, col8, col9, col10 = st.beta_columns(4)

# Alcoolismo
with col7:
    alcoolismo = st.radio("É alcoólatra?", ("Não", "Sim"))

    if alcoolismo == 'Não':
        alcoolismo = 0
    else:
        alcoolismo = 1

# PCD
with col8:
    pcd = st.radio("É PCD?", ("Não", "Sim"))

    if pcd == 'Não':
        pcd = 0
    else:
        pcd = 1

# SMS Recebido
with col9:
    sms_recebido = st.radio("SMS foi enviado?", ("Não", "Sim"))

    if sms_recebido == 'Não':
        sms_recebido = 1
    else:
        sms_recebido = 0

# Coluna apenas para alinhamento visual
with col10:
    ""

dados = {"genero": genero, "idade": idade, "auxilio_governamental": auxilio_governamental, "hipertensao": hipertensao, 
         "diabetes": diabetes, "alcoolismo": alcoolismo, "pcd": pcd, "sms_recebido": sms_recebido, "dias_ate_consulta": dias_ate_consulta}

features = pd.DataFrame(dados, index=[0])

# Carregando o modelo para fazer a previsão
xgb_model = pickle.load(open("xgbclassifier.pkl", "rb"))

if st.button("Verificar"):
    pred = xgb_model.predict(features)[0]
    if pred == 0:
        st.markdown("O paciente, provavelmente, **IRÁ** comparecer à consulta.")
    else:
        st.markdown("O paciente, provavelmente, **NÃO IRÁ** comparecer à consulta.")
    
################################