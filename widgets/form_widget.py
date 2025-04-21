
import datetime
import streamlit as st


def form_widget():

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
            
    return date, is_month_to_month, internet, is_optical_fiber, is_electronic_check
