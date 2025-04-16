

from datasource.api_churn_datasource import ApiChurnDataSource


class ApiChurnRepository():

    def __init__(self):
        self.data_source = ApiChurnDataSource()

    def predict_churn(self, data):
        """
        Predict churn using the API.
        """
        try:
            prediction = self.data_source.predict_churn(data)
            return prediction
        except Exception as e:
            raise Exception(e)
        