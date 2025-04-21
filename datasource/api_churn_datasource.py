
import requests


class ApiChurnDataSource():

    def __init__(self, ):
        self.url = "https://churn-prediction-api-ogwd.onrender.com/churn-api/v1/predict/list"
    
    def predict_churn(self, data):
        """
        Predict churn using the API.
        """
        response = requests.post(self.url, json=data)

        if response.status_code != 200:
            raise Exception("Algo salió mal en la predicción de churn")
        # todo: implementar el time out
        data = response.json()

        if 'predictions' not in data:
            raise Exception("No se encontraron predicciones en la respuesta")
        
        return data['predictions']
            

        

