
import datetime
import pandas as pd

# from entities.client_entity import Client


def add_client( client, df, clients_list ):
    """
    Adds a user to the dataframe.
    
    Parameters:
    - date: Date of the user
    - is_month_to_month: If the user is month to month
    - internet: If the user has internet
    - is_optical_fiber: If the user has optical fiber
    """
    df.loc[len(df)] = client.to_dict()
    df.reset_index(drop=True, inplace=True)
    clients_list.append(client)


def update_user(user, date = None, is_month_to_month = None, internet = None, is_optical_fiber = None ):

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


def delete_last_user(df, list_clients):
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

