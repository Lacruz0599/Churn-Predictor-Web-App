"""
This module defines the `Client` entity class, which represents a client and their attributes.

Classes:
    Client: A class that encapsulates client details, provides methods to convert the client object to a dictionary, 
            and maps the entity to a format suitable for API communication.

Usage:
    - Instantiate the `Client` class to create a client object.
    - Use the `to_dict` method to convert the client object to a dictionary.
    - Use the `map_entity` method to map the client object to a format suitable for API communication.

Dependencies:
    - utils.utils.calculate_days: A utility function to calculate the number of days between a given date and today.
"""

import datetime
from utils.utils import calculate_days


class Client:
    """
    Represents a client and their attributes.

    Attributes:
        date (datetime.date): The date the client joined.
        days (int): The number of days since the client joined.
        is_month_to_month (str): Indicates if the client is on a month-to-month plan ('Si' or 'No').
        internet (str): Indicates if the client has internet service ('Si' or 'No').
        is_optical_fiber (str): Indicates if the client has optical fiber internet ('Si' or 'No').
        is_electronic_check (str): Indicates if the client pays with an electronic check ('Si' or 'No').
        probability (float, optional): The predicted probability of churn.
        churn (int, optional): Indicates if the client is predicted to churn (1 for churn, 0 for no churn).
    """

    def __init__(self, 
                 date=datetime.date.today(), 
                 is_month_to_month='Si', 
                 internet='Si', 
                 is_optical_fiber='Si', 
                 is_electronic_check='Si',
                 probability=None, 
                 churn=None):
        """
        Initializes a Client object with the provided attributes.

        Args:
            date (datetime.date, optional): The date the client joined. Defaults to today's date.
            is_month_to_month (str, optional): Indicates if the client is on a month-to-month plan. Defaults to 'Si'.
            internet (str, optional): Indicates if the client has internet service. Defaults to 'Si'.
            is_optical_fiber (str, optional): Indicates if the client has optical fiber internet. Defaults to 'Si'.
            is_electronic_check (str, optional): Indicates if the client pays with an electronic check. Defaults to 'Si'.
            probability (float, optional): The predicted probability of churn. Defaults to None.
            churn (int, optional): Indicates if the client is predicted to churn. Defaults to None.
        """
        self.date = date
        self.days = calculate_days(date)
        self.is_month_to_month = is_month_to_month
        self.internet = internet
        self.is_optical_fiber = is_optical_fiber
        self.is_electronic_check = is_electronic_check
        self.probability = probability
        self.churn = churn

    def to_dict(self, include_prob_churn=False):
        """
        Converts the client object to a dictionary.

        Args:
            include_prob_churn (bool, optional): Whether to include churn probability and prediction in the dictionary. Defaults to False.

        Returns:
            dict: A dictionary representation of the client object.
        """
        if include_prob_churn:
            return {
                'Fecha de ingreso': self.date,
                'Facturación mensual': self.is_month_to_month,
                'Internet': self.internet,
                'Fibra óptica': self.is_optical_fiber,
                'Cheque electrónico': self.is_electronic_check,
                'Probabilidad de abandono': self.probability,
                'Abandono': 'No abandona' if self.churn == 0 else 'Abandona'
            }
        
        return {
            'Fecha de ingreso': self.date,
            'Facturación mensual': self.is_month_to_month,
            'Internet': self.internet,
            'Fibra óptica': self.is_optical_fiber,
            'Cheque electrónico': self.is_electronic_check,
        }

    def map_entity(self):
        """
        Maps the client object to a format suitable for API communication.

        Returns:
            dict: A dictionary containing the mapped client attributes.
        """
        return {
            'days': self.days,
            'is_month_to_month': self.one_cero_nan(self.is_month_to_month),
            'is_fiber_optic': self.one_cero_nan(self.is_optical_fiber),
            'is_electronic_check': self.one_cero_nan(self.is_electronic_check),
            'internet': self.one_cero_nan(self.internet)
        }

    def one_cero_nan(self, value):
        """
        Converts a value to 1, 0, or None based on its content.

        Args:
            value (str): The value to convert ('Si', 'No', or other).

        Returns:
            int or None: 1 if the value is 'Si', 0 if the value is 'No', and None otherwise.
        """
        if value == 'Si':
            return 1
        elif value == 'No':
            return 0
        else:
            return None



