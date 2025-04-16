import streamlit as st
import pandas as pd
import datetime

from entities.user_entity import User

def print_test():

    st.write("This is a test function.")

st.title("El cliente abadona?")

data = pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual', 'Internet', 'Fibra óptica'])

columns = st.columns(4)

date = columns[0].date_input( 'Fecha',
                      value=datetime.date.today(), 
                      min_value=datetime.date(2019, 1, 1), 
                      max_value=datetime.date.today(),
                      on_change= print_test)

is_month_to_month = columns[1].selectbox( 'X',
                      options=['Si', 'No', 'No lo sé'], 
                      index=0)

internet = columns[2].selectbox( 'Y',
                      options=['Si', 'No', 'No lo sé'], 
                      index=0)

is_optical_fiber = columns[3].selectbox( 'Z',
                      options=['Si', 'No', 'No lo sé'], 
                      index=0)


container = st.container(border=True)

with container:
    columns = st.columns(5, vertical_alignment='center')
    columns[1].button('Eliminar', use_container_width=True)
    columns[3].button('Añadir', use_container_width=True)


st.table( pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual', 'Internet', 'Fibra óptica']))

columns = st.columns(3, vertical_alignment='center')
columns[1].button('Predecir abandonos', use_container_width=True)

st.table( pd.DataFrame(columns=['Fecha de ingreso', 'Facturación mensual', 'Internet', 'Fibra óptica', 'Probabilidades de abandonar']))