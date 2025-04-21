

from datasource.api_churn_datasource import ApiChurnDataSource


class ApiChurnRepository():

    def __init__(self):
        self.data_source = ApiChurnDataSource()

    def predict_churn(self, list_clients, show_results, show_error):

        try:

            if len(list_clients) == 0:
                raise Exception("No hay clientes para predecir")
        
            # Convert the list of clients to a format that the API can understand
            list_mapped_clients = [ client.map_entity() for client in list_clients ]

            body = {
                "clients": list_mapped_clients,
            }
            # Call the data source to get the prediction
            predictions = self.data_source.predict_churn(body)

            # Map the predictions to the clients

            for i, client in enumerate(list_clients):
                client.probability = predictions[i]['probability']
                client.churn = predictions[i]['prediction']
            
            show_results(list_clients)

        except Exception as e:
            show_error(str(e))