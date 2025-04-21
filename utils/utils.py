import datetime

import pandas as pd
# import streamlit as st


def add_client_df(client, df, clients_list):
    """
    Adds a new client to the DataFrame and the clients list.

    Args:
        client (object): The client object containing client details.
        df (pd.DataFrame): The DataFrame where the client data will be added.
        clients_list (list): The list of client objects to which the client will be appended.

    Returns:
        None
    """
    df.loc[len(df)] = client.to_dict()
    df.reset_index(drop=True, inplace=True)
    clients_list.append(client)


def update_current_client(user, date=None, is_month_to_month=None, internet=None, is_optical_fiber=None, is_electronic_check=None):
    """
    Updates the attributes of the current client object.

    Args:
        user (object): The client object to be updated.
        date (datetime.date, optional): The date to update the client's subscription.
        is_month_to_month (int, optional): Whether the client is on a month-to-month plan.
        internet (int, optional): Whether the client has internet service.
        is_optical_fiber (int, optional): Whether the client has optical fiber internet.
        is_electronic_check (int, optional): Whether the client pays with an electronic check.

    Returns:
        None
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
    """
    Deletes the last client from the DataFrame and the clients list.

    Args:
        df (pd.DataFrame): The DataFrame from which the last row will be removed.
        list_clients (list): The list of client objects from which the last client will be removed.

    Returns:
        None
    """
    if len(df) == 0:
        return
    
    df.drop(df.index[-1], inplace=True)
    df.reset_index(drop=True, inplace=True)
    list_clients.pop(-1)


def calculate_days(date):
    """
    Calculates the number of days between the given date and today.

    Args:
        date (datetime.date): The date to calculate the difference from.

    Returns:
        int: The number of days between the given date and today.
    """
    today = datetime.date.today()
    return (today - date).days


def df_predictions(list_clients):
    """
    Creates a DataFrame containing predictions and client details.

    Args:
        list_clients (list): A list of client objects containing prediction and client details.

    Returns:
        pd.DataFrame: A DataFrame with the following columns:
            - "Fecha": The date of the client's subscription.
            - "Facturación mensual": Whether the client is on a month-to-month plan.
            - "internet": Whether the client has internet service.
            - "Tiene fibra óptica": Whether the client has optical fiber internet.
            - "Paga con cheque electronico": Whether the client pays with an electronic check.
            - "Probabilidad": The predicted probability of churn.
            - "churn": Whether the client is predicted to churn.
    """
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