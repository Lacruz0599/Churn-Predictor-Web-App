
import requests


class ApiChurnDataSource():

    def __init__(self, ):
        self.url = "http://127.0.0.1:8000/churn-api/v1/predict/list"
    
    def predict_churn(self, data):
        """
        Predict churn using the API.
        """
        response = requests.post(self.url, json=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Algo salió mal en la predicción de churn")
        

