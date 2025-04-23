
import streamlit as st

from entities.client_entity import Client
from utils.utils import create_df, update_current_client
from widgets.buttons_widget import buttons_widget
from widgets.dialog_widgets import show_error, show_results
from widgets.form_widget import form_widget



if 'first_time' not in st.session_state:
    st.session_state.first_time = False

    st.session_state.current_client = Client()
    st.session_state.clients_list = []

    st.session_state.load_prediction = False
    st.session_state.ready_to_show = False

    st.session_state.error_message = None
    st.session_state.error_occurred = False


st.title("¿El cliente abandonará el servicio?")


if (len(st.session_state.clients_list) > 0) and (not st.session_state.load_prediction) and (st.session_state.ready_to_show):
    show_results(st.session_state.clients_list)
    st.session_state.ready_to_show = False
    st.session_state.clients_list = []

elif st.session_state.error_occurred:
    st.session_state.error_occurred = False
    show_error(st.session_state.error_message)
    st.session_state.error_message = None


date, is_month_to_month, internet, is_optical_fiber, is_electronic_check = form_widget()

update_current_client(st.session_state.current_client, date, is_month_to_month, internet, is_optical_fiber, is_electronic_check)


buttons_widget()


st.table( create_df(st.session_state.clients_list, include_prob_churn=False) )






