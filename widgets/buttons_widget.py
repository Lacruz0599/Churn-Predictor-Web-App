

import streamlit as st

from repository.api_churn_repository import ApiChurnRepository
from utils.utils import add_client_df, delete_last_client
from widgets.dialog_widgets import show_results, show_error


def buttons_widget():

    container_buttons = st.container(border=True)

    repository = ApiChurnRepository()
    
    with container_buttons:

        columns = st.columns(4, vertical_alignment='center')

        # if st.session_state.load_prediction:
        #     with st.spinner('Cargando predicciones...'):
        #         time.sleep(10)
        #         columns[0].empty()
        #         repository.predict_churn(
        #             st.session_state.clients_list,
        #             show_results,
        #             show_error
        #         )
        #         toggle_load_prediction()
        # else:
        #     columns[0].button('Predecir abandonos', 
        #                 use_container_width=True,
        #                 on_click= toggle_load_prediction)

        columns[0].button('Predecir abandonos', 
                    use_container_width=True,
                    disabled= st.session_state.load_prediction,
                    on_click= toggle_load_prediction)
        
        
        columns[2].button('Eliminar', 
                        use_container_width=True,
                        disabled= st.session_state.load_prediction,
                        on_click=delete_last_client,
                        args=(st.session_state.df_to_predict,
                                st.session_state.clients_list))
        
        
        columns[3].button('Añadir', 
                        use_container_width=True,
                        disabled= st.session_state.load_prediction,
                        on_click=add_client_df,
                        args=(st.session_state.current_client, 
                                st.session_state.df_to_predict,
                                st.session_state.clients_list))
        

        if not st.session_state.load_prediction:
            return
        
        with columns[1]:
            with st.spinner('Cargando predicciones...'):
                repository.predict_churn(
                    st.session_state.clients_list,
                    show_results,
                    show_error
                    )
            toggle_load_prediction()
        


def toggle_load_prediction():
    """
    Function to toggle the load prediction button.
    """
    if st.session_state.load_prediction:
        st.session_state.load_prediction = False
    else:
        st.session_state.load_prediction = True