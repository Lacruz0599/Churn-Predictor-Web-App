"""
This module defines the `form_widget` function, which creates a Streamlit form widget for collecting client data.

Functions:
    form_widget(): Creates a form widget for inputting client attributes such as date of joining, billing type, 
                   internet service, optical fiber, and payment method.

Dependencies:
    - datetime: For working with dates.
    - streamlit: For creating the Streamlit UI components.

Usage:
    - Call `form_widget()` to render the form in a Streamlit app and collect client data.
"""

import datetime
import streamlit as st


def form_widget():
    """
    Creates a Streamlit form widget for collecting client data.

    The form includes:
        - A date input for the client's joining date.
        - Dropdowns for selecting whether the client pays monthly, has internet, uses optical fiber, 
          and pays with an electronic check.

    Returns:
        tuple: A tuple containing the following client attributes:
            - date (datetime.date): The date the client joined.
            - is_month_to_month (str): Indicates if the client is on a month-to-month plan ('Si', 'No', or 'No lo sé').
            - internet (str): Indicates if the client has internet service ('Si', 'No', or 'No lo sé').
            - is_optical_fiber (str): Indicates if the client has optical fiber internet ('Si', 'No', or 'No lo sé').
            - is_electronic_check (str): Indicates if the client pays with an electronic check ('Si', 'No', or 'No lo sé').
    """
    main_container = st.container(border=True)

    with main_container:

        # First section of the form
        container_form_1 = st.container()

        with container_form_1:

            columns_form_1 = st.columns(3, vertical_alignment='center')

            # Date input for the client's joining date
            date = columns_form_1[0].date_input(
                'Fecha de ingreso',
                disabled=st.session_state.load_prediction,
                value=datetime.date.today(),
                min_value=datetime.date(2017, 1, 1),
                max_value=datetime.date.today(),
                help='Fecha de ingreso del cliente',
            )

            # Dropdown for monthly billing
            is_month_to_month = columns_form_1[1].selectbox(
                '¿Paga facturación mensual?',
                disabled=st.session_state.load_prediction,
                options=['Si', 'No', 'No lo sé'],
                key='is_month_to_month',
                index=0,
                help='¿El cliente paga mensualmente su servicio?',
            )

            # Dropdown for internet service
            internet = columns_form_1[2].selectbox(
                '¿Tiene internet?',
                disabled=st.session_state.load_prediction,
                options=['Si', 'No', 'No lo sé'],
                key='internet',
                index=0,
                help='¿El cliente tiene servicio de internet?',
            )

        # Second section of the form
        container_form_2 = st.container()

        with container_form_2:

            columns_form_2 = st.columns(3, vertical_alignment='center')

            # Dropdown for optical fiber
            is_optical_fiber = columns_form_2[0].selectbox(
                '¿Tiene fibra óptica?',
                disabled=st.session_state.load_prediction,
                options=['Si', 'No', 'No lo sé'],
                key='optical_fiber',
                index=0,
                help='¿El cliente tiene fibra óptica en su servicio?',
            )

            # Dropdown for electronic check payment
            is_electronic_check = columns_form_2[2].selectbox(
                '¿Paga con cheque electrónico?',
                disabled=st.session_state.load_prediction,
                options=['Si', 'No', 'No lo sé'],
                key='is_electronic_check',
                index=0,
                help='¿El cliente paga con cheque electrónico?',
            )

    return date, is_month_to_month, internet, is_optical_fiber, is_electronic_check
