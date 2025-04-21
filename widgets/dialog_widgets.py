
import streamlit as st

from utils.utils import df_predictions

@st.dialog('Resultados de las predicciones', width='large')
def show_results( list_clients):
    df_results = df_predictions(list_clients)

    st.download_button(label='Descargar resultados', 
                       data=df_results.to_csv(index=False).encode('utf-8'), 
                       file_name='predicciones.csv', 
                       mime='text/csv')

    st.table(df_results)


@st.dialog('Hubo un error...', width='small')
def show_error( error_message):
    st.write(error_message)