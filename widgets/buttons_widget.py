"""
This module defines the `buttons_widget` function, which creates a Streamlit widget for managing client actions 
such as adding, deleting, and predicting churn.

Functions:
    buttons_widget(): Creates a widget with buttons for client management and churn prediction.
    toggle_load_prediction(): Toggles the state of the load prediction button.

Dependencies:
    - streamlit: For creating the Streamlit UI components.
    - entities.client_entity.Client: The Client class for managing client data.
    - repository.api_churn_repository.ApiChurnRepository: The repository class for interacting with the Churn Prediction API.
    - utils.utils.add_client: A utility function to add a client to the list.
    - utils.utils.delete_last_client: A utility function to delete the last client from the list.

Usage:
    - Call `buttons_widget()` to render the widget in a Streamlit app.
"""

import streamlit as st
from entities.client_entity import Client
from repository.api_churn_repository import ApiChurnRepository
from utils.utils import add_client, delete_last_client


def buttons_widget():
    """
    Creates a Streamlit widget with buttons for managing clients and predicting churn.

    The widget includes:
        - A button to predict churn for the current list of clients.
        - A button to delete the last client from the list.
        - A button to add a new client to the list.

    The function also handles the logic for interacting with the Churn Prediction API and updating the application state.

    Returns:
        None
    """
    container_buttons = st.container(border=True)

    repository = ApiChurnRepository()
    
    with container_buttons:

        columns = st.columns(4, vertical_alignment='center')

        # Button to predict churn
        columns[0].button('Predecir abandonos', 
                           use_container_width=True,
                           disabled=st.session_state.load_prediction,
                           help='Predecir cuales clientes abandonarán',
                           on_click=toggle_load_prediction)

        # Button to delete the last client
        columns[2].button('Eliminar', 
                           use_container_width=True,
                           disabled=st.session_state.load_prediction,
                           help='Eliminar el último cliente añadido a la lista',
                           on_click=delete_last_client,
                           kwargs={'list_clients': st.session_state.clients_list})

        # Button to add a new client
        with columns[3]:
            st.button('Añadir', 
                      use_container_width=True,
                      disabled=st.session_state.load_prediction,
                      help= 'Añade un nuevo cliente a la lista',
                      on_click=add_client,
                      args=(st.session_state.current_client, 
                            st.session_state.clients_list))
            st.session_state.current_client = Client()

        # Handle churn prediction logic
        if not st.session_state.load_prediction:
            return

        with columns[1]:
            with st.spinner('Cargando predicciones...'):
                try:
                    repository.predict_churn(st.session_state.clients_list)
                    st.session_state.ready_to_show = True
                except Exception as e:
                    st.session_state.error_occurred = True
                    st.session_state.error_message = str(e)
                finally:
                    toggle_load_prediction()
                    st.rerun()


def toggle_load_prediction():
    """
    Toggles the state of the `load_prediction` flag in the Streamlit session state.

    This function is used to enable or disable the prediction button.

    Returns:
        None
    """
    st.session_state.load_prediction = not st.session_state.load_prediction