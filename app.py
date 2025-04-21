import streamlit as st
import pandas as pd
import datetime

from entities.client_entity import Client
from repository.api_churn_repository import ApiChurnRepository
from utils.utils import add_client_df, delete_last_user, df_predictions, update_user


@st.dialog('Resultados de las predicciones', width='large')
def show_results( list_clients):
    df_results = df_predictions(list_clients)
    st.table(df_results)
    st.download_button(label='Descargar resultados', 
                       data=df_results.to_csv(index=False).encode('utf-8'), 
                       file_name='predicciones.csv', 
                       mime='text/csv')


@st.dialog('Hubo un error...', width='small')
def show_error( error_message):
    st.write(error_message)


if 'first_time' not in st.session_state:
    st.session_state.first_time = False

    st.session_state.df_to_predict = pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual','Cheque electrónico', 'Internet', 'Fibra óptica'])
    st.session_state.current_client = Client()
    st.session_state.clients_list = []

    st.session_state.predictions_ready = False


st.title("¿El cliente abadonaá el servicio?")

main_container = st.container( border=True)

with main_container:

    container_form_1 = st.container()

    with container_form_1:

        columns_form_1 = st.columns(3 , vertical_alignment='center')

        date = columns_form_1[0].date_input( 'Fecha de ingreso',
                        value=datetime.date.today(), 
                        min_value=datetime.date(2017, 1, 1), 
                        max_value=datetime.date.today(), )

        is_month_to_month = columns_form_1[1].selectbox( '¿Paga facturación mensual?',
                            options=['Si', 'No', 'No lo sé'], 
                            key='is_month_to_month',
                            index=0)

        internet = columns_form_1[2].selectbox( '¿Tiene internet?',
                            options=['Si', 'No', 'No lo sé'], 
                            key='internet',
                            index=0)


    container_form_2 = st.container()

    with container_form_2:

        columns_form_2 = st.columns(3, vertical_alignment='center')
        
        is_optical_fiber = columns_form_2[0].selectbox( '¿Tiene fibra óptica?',
                            options=['Si', 'No', 'No lo sé'], 
                            key='optical_fiber',
                            index=0)

        is_electronic_check = columns_form_2[2].selectbox( '¿Paga con cheque electrónico?',
                            options=['Si', 'No', 'No lo sé'], 
                            key='is_electronic_check',
                            index=0)


update_user(st.session_state.current_client, date, is_month_to_month, internet, is_optical_fiber, is_electronic_check)


container_buttons = st.container(border=True)

with container_buttons:
    columns = st.columns(5, vertical_alignment='center')
    columns[1].button('Eliminar', 
                      use_container_width=True,
                      on_click=delete_last_user,
                      args=(st.session_state.df_to_predict,
                            st.session_state.clients_list))
    
    columns[3].button('Añadir', 
                      use_container_width=True,
                      on_click=add_client_df,
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
                      'list_clients': st.session_state.clients_list,
                      'show_results': show_results,
                      'show_error': show_error,
                  })





