"""
This module defines Streamlit dialog widgets for displaying results and handling errors in the application.

Functions:
    show_results(list_clients): Displays a dialog with the prediction results in a table and provides a download button for the results.
    show_error(error_message): Displays a dialog with an error message.

Dependencies:
    - streamlit: For creating the Streamlit UI components.
    - utils.utils.create_df: A utility function to create a DataFrame from a list of clients.

Usage:
    - Call `show_results(list_clients)` to display the prediction results.
    - Call `show_error(error_message)` to display an error message.
"""

import streamlit as st
from utils.utils import create_df


@st.dialog('Resultados de las predicciones', width='large')
def show_results(list_clients):
    """
    Displays a dialog with the prediction results in a table and provides a download button for the results.

    Args:
        list_clients (list): A list of client objects containing prediction results.

    Returns:
        None
    """
    df_results = create_df(list_clients)

    st.download_button(label='Descargar resultados', 
                       data=df_results.to_csv(index=False).encode('utf-8'), 
                       file_name='predicciones.csv', 
                       mime='text/csv')

    st.table(df_results)


@st.dialog('Hubo un error...', width='small')
def show_error(error_message):
    """
    Displays a dialog with an error message.

    Args:
        error_message (str): The error message to display.

    Returns:
        None
    """
    st.write(error_message)