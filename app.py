
import streamlit as st
import pandas as pd
import datetime

from entities.client_entity import Client
from repository.api_churn_repository import ApiChurnRepository
from utils.utils import add_client, delete_last_user, df_predictions, update_user


if 'first_time' not in st.session_state:
    st.session_state.first_time = False

    st.session_state.df_to_predict = pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual', 'Internet', 'Fibra óptica'])
    st.session_state.current_client = Client()
    st.session_state.clients_list = []

    st.session_state.predictions_ready = False


st.title("El cliente abadona?")

columns = st.columns(4)

date = columns[0].date_input( 'Fecha',
                      value=datetime.date.today(), 
                      min_value=datetime.date(2017, 1, 1), 
                      max_value=datetime.date.today(), )

is_month_to_month = columns[1].selectbox( 'Campo 1',
                      options=['Si', 'No', 'No lo sé'], 
                      key='is_month_to_month',
                      index=0)

internet = columns[2].selectbox( 'Campo 2',
                      options=['Si', 'No', 'No lo sé'], 
                      key='internet',
                      index=0)

is_optical_fiber = columns[3].selectbox( 'Campo 3',
                      options=['Si', 'No', 'No lo sé'], 
                      key='optical_fiber',
                      index=0)


update_user(st.session_state.current_client, date, is_month_to_month, internet, is_optical_fiber)


container = st.container(border=True)

with container:
    columns = st.columns(5, vertical_alignment='center')
    columns[1].button('Eliminar', 
                      use_container_width=True,
                      on_click=delete_last_user,
                      args=(st.session_state.df_to_predict,
                            st.session_state.clients_list))
    
    columns[3].button('Añadir', 
                      use_container_width=True,
                      on_click=add_client,
                      args=(st.session_state.current_client, 
                            st.session_state.df_to_predict,
                            st.session_state.clients_list))


st.table( st.session_state.df_to_predict )

columns = st.columns(3, vertical_alignment='center')

repository = ApiChurnRepository()

columns[1].button('Predecir abandonos', 
                  use_container_width=True,
                  on_click= repository.predict_churn,
                  kwargs ={
                      'list_clients': st.session_state.clients_list
                  })


# st.table( df_predictions(st.session_state.clients_list) )