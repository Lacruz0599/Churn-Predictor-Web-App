

from datasource.api_churn_datasource import ApiChurnDataSource


class ApiChurnRepository():

    def __init__(self):
        self.data_source = ApiChurnDataSource()

    def predict_churn(self, list_clients):
        """
        Predict churn using the API.
        """
        # Convert the list of clients to a format that the API can understand
        list_mapped_clients = [ client.map_entity() for client in list_clients ]

        body = {
            "clients": list_mapped_clients,
        }
        # Call the data source to get the prediction
        try:
            predictions = self.data_source.predict_churn(body)

            # Map the predictions to the clients

            for i, client in enumerate(list_clients):
                client.probability = predictions[i]['probability']
                client.churn = predictions[i]['prediction']

        except Exception as e:
            raise Exception(e)
        