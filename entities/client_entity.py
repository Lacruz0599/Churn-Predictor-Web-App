
import datetime
from numpy import nan

from utils.utils import calculate_days


class Client():
    def __init__(self, 
                 date = datetime.date.today(), 
                 is_month_to_month = 'Si', 
                 internet = 'Si', 
                 is_optical_fiber = 'Si', 
                 probability=None, 
                 churn = None
                ):
        self.date = date
        self.days = calculate_days(date)
        self.is_month_to_month = is_month_to_month
        self.internet = internet
        self.is_optical_fiber = is_optical_fiber
        self.probability = probability
        self.churn = churn
    
    def to_dict(self):
        return {
            'Fecha de ingreso': self.date,
            'Facturación mensual': self.is_month_to_month,
            'Internet': self.internet,
            'Fibra óptica': self.is_optical_fiber
        }
    
    def map_entity(self):
        return {
            'days': self.days,
            'is_month_to_month': self.one_cero_nan(self.is_month_to_month),
            'internet': self.one_cero_nan(self.internet),
            'is_optical_fiber': self.one_cero_nan(self.is_optical_fiber),
        }
    
    def one_cero_nan(self, value):
        if value == 'Si':
            return 1
        elif value == 'No':
            return 0
        else:
            return nan
        