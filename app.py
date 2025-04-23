"""
This is the main application file for the Churn Prediction Web App.

The app allows users to input client data, manage a list of clients, and predict whether a client will churn using a machine learning model.

Features:
    - Input client data through a form.
    - Manage a list of clients (add, delete, and reset).
    - Predict churn for the list of clients.
    - Display prediction results in a table with an option to download the results.
    - Handle and display error messages.

Dependencies:
    - streamlit: For creating the web application interface.
    - entities.client_entity.Client: The Client class for managing client data.
    - utils.utils: Utility functions for updating client data and creating DataFrames.
    - widgets.buttons_widget: A widget for managing client actions (add, delete, predict).
    - widgets.dialog_widgets: Widgets for displaying results and error messages.
    - widgets.form_widget: A form widget for collecting client data.

Usage:
    - Run this file using Streamlit to launch the web application.
    - Use the form to input client data and manage the client list.
    - Click the "Predecir abandonos" button to predict churn for the clients in the list.
"""

import streamlit as st

from entities.client_entity import Client
from utils.utils import create_df, update_current_client
from widgets.buttons_widget import buttons_widget
from widgets.dialog_widgets import show_error, show_results
from widgets.form_widget import form_widget


# Initialize session state variables
if 'first_time' not in st.session_state:
    st.session_state.first_time = False

    st.session_state.current_client = Client()
    st.session_state.clients_list = []

    st.session_state.load_prediction = False
    st.session_state.ready_to_show = False

    st.session_state.error_message = None
    st.session_state.error_occurred = False


# App title
st.title("¿El cliente abandonará el servicio?")


# Display prediction results if ready
if (len(st.session_state.clients_list) > 0) and (not st.session_state.load_prediction) and (st.session_state.ready_to_show):
    show_results(st.session_state.clients_list)
    st.session_state.ready_to_show = False
    st.session_state.clients_list = []

# Display error message if an error occurred
elif st.session_state.error_occurred:
    st.session_state.error_occurred = False
    show_error(st.session_state.error_message)
    st.session_state.error_message = None


# Render the form widget to collect client data
date, is_month_to_month, internet, is_optical_fiber, is_electronic_check = form_widget()

# Update the current client object with the form data
update_current_client(st.session_state.current_client, date, is_month_to_month, internet, is_optical_fiber, is_electronic_check)

# Render the buttons widget for managing client actions
buttons_widget()

# Display the current list of clients in a table
st.table(create_df(st.session_state.clients_list, include_prob_churn=False))






