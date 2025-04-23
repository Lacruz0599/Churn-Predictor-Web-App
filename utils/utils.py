"""
This module provides utility functions for managing client data and creating DataFrames.

Functions:
    add_client(client, clients_list): Adds a client to the list of clients.
    update_current_client(user, date=None, is_month_to_month=None, internet=None, is_optical_fiber=None, is_electronic_check=None):
        Updates the attributes of an existing client.
    delete_last_client(list_clients): Removes the last client from the list of clients.
    calculate_days(date): Calculates the number of days between the given date and today.
    create_df(list_clients, include_prob_churn=True): Creates a pandas DataFrame from a list of clients.

Dependencies:
    - datetime: For working with dates.
    - pandas: For creating and managing DataFrames.
"""

import datetime
import pandas as pd


def add_client(client, clients_list):
    """
    Adds a client to the list of clients.

    Args:
        client (object): The client object to add.
        clients_list (list): The list of client objects.

    Returns:
        None
    """
    clients_list.append(client)


def update_current_client(user, date=None, is_month_to_month=None, internet=None, is_optical_fiber=None, is_electronic_check=None):
    """
    Updates the attributes of an existing client.

    Args:
        user (object): The client object to update.
        date (datetime.date, optional): The new date for the client.
        is_month_to_month (str, optional): Indicates if the client is on a month-to-month plan ('Si' or 'No').
        internet (str, optional): Indicates if the client has internet service ('Si' or 'No').
        is_optical_fiber (str, optional): Indicates if the client has optical fiber internet ('Si' or 'No').
        is_electronic_check (str, optional): Indicates if the client pays with an electronic check ('Si' or 'No').

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


def delete_last_client(list_clients):
    """
    Removes the last client from the list of clients.

    Args:
        list_clients (list): The list of client objects.

    Returns:
        None
    """
    if len(list_clients) == 0:
        return
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


def create_df(list_clients, include_prob_churn=True):
    """
    Creates a pandas DataFrame from a list of clients.

    Args:
        list_clients (list): A list of client objects.
        include_prob_churn (bool, optional): Whether to include churn probability and prediction in the DataFrame. Defaults to True.

    Returns:
        pd.DataFrame: A DataFrame containing client data.
    """
    dict_to_df = {
        "Fecha": [],
        "Facturación mensual": [],
        "internet": [],
        "Tiene fibra óptica": [],
        "Paga con cheque electronico": []
    }

    if include_prob_churn:
        dict_to_df["Probabilidad"] = []
        dict_to_df["churn"] = []

    for client in list_clients:
        dict_to_df["Fecha"].append(client.date)
        dict_to_df["Facturación mensual"].append(client.is_month_to_month)
        dict_to_df["internet"].append(client.internet)
        dict_to_df["Tiene fibra óptica"].append(client.is_optical_fiber)
        dict_to_df["Paga con cheque electronico"].append(client.is_electronic_check)

        if include_prob_churn:
            dict_to_df["Probabilidad"].append(client.probability)
            dict_to_df["churn"].append('Abandona' if client.churn else 'No Abandona')

    main_df = pd.DataFrame(dict_to_df)
    return main_df