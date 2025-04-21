
import datetime

import pandas as pd
import streamlit as st


def add_client_df( client, df, clients_list ):
    """
    Adds a user to the dataframe.
    
    Parameters:
    - date: Date of the user
    - is_month_to_month: If the user is month to month
    - internet: If the user has internet
    - is_optical_fiber: If the user has optical fiber
    """
    # df.loc[len(df)] = client.to_dict()
    df.loc[len(df)] = st.session_state.current_client.to_dict()
    df.reset_index(drop=True, inplace=True)
    clients_list.append(client)


def update_current_client(user, date = None, is_month_to_month = None, internet = None, is_optical_fiber = None, is_electronic_check = None):

    """
    Updates a user in the dataframe.
    
    Parameters:
    - user: User to update
    - date: Date of the user
    - is_month_to_month: If the user is month to month
    - internet: If the user has internet
    - is_optical_fiber: If the user has optical fiber
    """
    if date:
        user.days = calculate_days(date)
        user.date = date
    if is_month_to_month:
        user.is_month_to_month = is_month_to_month
    if internet:
        user.internet = internet
    if is_optical_fiber:
        user.is_optical_fiber = is_optical_fiber
    if is_electronic_check:
        user.is_electronic_check = is_electronic_check


def delete_last_client(df, list_clients):
    """"
    Deletes the last user in the dataframe.
    
    Parameters:
    - df: Dataframe to delete the user from
    """
    if len(df) > 0:
        df.drop(df.index[-1], inplace=True)
        df.reset_index(drop=True, inplace=True)
        list_clients.pop(-1)


def calculate_days( date ):
    """
    Calculate the number of days since the user joined.
    
    Parameters:
    - date: Date of the user
    
    Returns:
    - Number of days since the user joined
    """
    today = datetime.date.today()
    return (today - date).days


def df_predictions( list_clients ):

    dates = []
    is_month_to_month = []
    internet = []
    is_optical_fiber = []
    is_electronic_check = []
    prob = []
    churn = []  

    for client in list_clients:
        dates.append(client.date)
        is_month_to_month.append(client.is_month_to_month)
        internet.append(client.internet)
        is_optical_fiber.append(client.is_optical_fiber)
        is_electronic_check.append(client.is_electronic_check)
        prob.append(client.probability)
        churn.append(client.churn)


    main_df = pd.DataFrame(
        {
            "Fecha": dates,
            "Facturación mensual": is_month_to_month,
            "internet": internet,
            "Tiene fibra óptica": is_optical_fiber,
            "Paga con cheque electronico": is_electronic_check,
            "Probabilidad": prob,
            "churn": churn
        }
    )
    
    return main_df