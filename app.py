import streamlit as st
import pandas as pd

from entities.client_entity import Client
from utils.utils import update_current_client
from widgets.buttons_widget import buttons_widget
from widgets.form_widget import form_widget



if 'first_time' not in st.session_state:
    st.session_state.first_time = False

    st.session_state.df_to_predict = pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual','Cheque electrónico', 'Internet', 'Fibra óptica'])
    st.session_state.current_client = Client()
    st.session_state.clients_list = []
    st.session_state.load_prediction = False


st.title("¿El cliente abandonará el servicio?")


date, is_month_to_month, internet, is_optical_fiber, is_electronic_check = form_widget()


update_current_client(st.session_state.current_client, date, is_month_to_month, internet, is_optical_fiber, is_electronic_check)


buttons_widget()


st.table( st.session_state.df_to_predict )






