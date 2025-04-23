

import streamlit as st

from entities.client_entity import Client
from repository.api_churn_repository import ApiChurnRepository
from utils.utils import add_client, delete_last_client


def buttons_widget():

    container_buttons = st.container(border=True)

    repository = ApiChurnRepository()
    
    with container_buttons:

        columns = st.columns(4, vertical_alignment='center')


        columns[0].button('Predecir abandonos', 
                    use_container_width=True,
                    disabled= st.session_state.load_prediction,
                    on_click= toggle_load_prediction)
        
        
        columns[2].button('Eliminar', 
                        use_container_width=True,
                        disabled= st.session_state.load_prediction,
                        on_click=delete_last_client,
                        kwargs={'list_clients': st.session_state.clients_list})
        
        
        with columns[3]:
            st.button('Añadir', 
                use_container_width=True,
                disabled= st.session_state.load_prediction,
                on_click=add_client,
                args=(st.session_state.current_client, 
                      st.session_state.clients_list))
            st.session_state.current_client = Client()
        

        if not st.session_state.load_prediction:
            return
        
        
        with columns[1]:
            with st.spinner('Cargando predicciones...'):
                try:
                    repository.predict_churn(
                        st.session_state.clients_list
                        )        
                    st.session_state.ready_to_show = True   
                except Exception as e:
                    st.session_state.error_occurred = True
                    st.session_state.error_message = str(e)
                    
                finally:
                    toggle_load_prediction()
                    st.rerun()
        


def toggle_load_prediction():
    """
    Function to toggle the load prediction button.
    """
    if st.session_state.load_prediction:
        st.session_state.load_prediction = False
    else:
        st.session_state.load_prediction = True