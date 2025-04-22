"""
This module provides a data source class for interacting with the Churn Prediction API.

Classes:
    ApiChurnDataSource: A class to handle communication with the Churn Prediction API.

Usage:
    - Instantiate the `ApiChurnDataSource` class.
    - Use the `predict_churn` method to send data to the API and retrieve churn predictions.
"""

import requests


class ApiChurnDataSource:
    """
    A data source class for interacting with the Churn Prediction API.

    Attributes:
        url (str): The endpoint URL for the Churn Prediction API.
    """

    def __init__(self):
        """
        Initializes the ApiChurnDataSource with the API endpoint URL.
        """
        self.url = "https://churn-prediction-api-ogwd.onrender.com/churn-api/v1/predict/list"

    def predict_churn(self, data):
        """
        Sends a POST request to the Churn Prediction API with the provided data and retrieves predictions.

        Args:
            data (dict): A dictionary containing the input data for churn prediction.

        Returns:
            list: A list of predictions returned by the API.

        Raises:
            Exception: If the API response status code is not 200.
            Exception: If the 'predictions' key is not found in the API response.
        """
        response = requests.post(self.url, json=data, timeout=(120, 180))

        if response.status_code != 200:
            raise Exception("Algo salió mal en la predicción de churn")

        data = response.json()

        if 'predictions' not in data:
            raise Exception("No se encontraron predicciones en la respuesta")

        return data['predictions']




