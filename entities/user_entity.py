class User():
    def __init__(self, days, is_month_to_month, internet, is_optical_fiber, probability=None, churn = None):
        self.days = days
        self.is_month_to_month = is_month_to_month
        self.internet = internet
        self.is_optical_fiber = is_optical_fiber
        self.probability = probability
        self.churn = churn