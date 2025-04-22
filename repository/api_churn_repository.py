"""
This module provides a repository class for managing interactions with the Churn Prediction API.

Classes:
    ApiChurnRepository: A repository class that acts as an intermediary between the application and the Churn Prediction API.

Usage:
    - Instantiate the `ApiChurnRepository` class.
    - Use the `predict_churn` method to send client data to the API and handle the predictions.

Dependencies:
    - datasource.api_churn_datasource.ApiChurnDataSource: The data source class used to communicate with the API.
"""

import time
from datasource.api_churn_datasource import ApiChurnDataSource


class ApiChurnRepository:
    """
    A repository class for managing interactions with the Churn Prediction API.

    Attributes:
        data_source (ApiChurnDataSource): An instance of the data source class for API communication.
    """

    def __init__(self):
        """
        Initializes the ApiChurnRepository with an instance of the ApiChurnDataSource.
        """
        self.data_source = ApiChurnDataSource()

    def predict_churn(self, list_clients, show_results, show_error):
        """
        Sends client data to the Churn Prediction API, retrieves predictions, and updates the client objects.

        Args:
            list_clients (list): A list of client objects to be sent to the API for prediction.
            show_results (function): A callback function to display the results after predictions are retrieved.
            show_error (function): A callback function to display an error message if an exception occurs.

        Returns:
            None

        Raises:
            Exception: If the list of clients is empty or if an error occurs during the API call.
        """
        try:
            if len(list_clients) == 0:
                raise Exception("No hay clientes para predecir")
        
            # Convert the list of clients to a format that the API can understand
            list_mapped_clients = [client.map_entity() for client in list_clients]

            body = {
                "clients": list_mapped_clients,
            }

            # Call the data source to get the prediction
            predictions = self.data_source.predict_churn(body)

            # Map the predictions to the clients
            for i, client in enumerate(list_clients):
                client.probability = predictions[i]['probability']
                client.churn = predictions[i]['prediction']
            
            time.sleep(1)  # Prevents excesive calls
            show_results(list_clients)

        except Exception as e:
            show_error(str(e))