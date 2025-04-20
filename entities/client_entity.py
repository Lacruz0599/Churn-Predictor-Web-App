
import datetime
# from numpy import nan

from utils.utils import calculate_days


class Client():
    def __init__(self, 
                 date = datetime.date.today(), 
                 is_month_to_month = 'Si', 
                 internet = 'Si', 
                 is_optical_fiber = 'Si', 
                 is_electronic_check = 'Si',
                 probability=None, 
                 churn = None
                ):
        self.date = date
        self.days = calculate_days(date)
        self.is_month_to_month = is_month_to_month
        self.internet = internet
        self.is_optical_fiber = is_optical_fiber
        self.is_electronic_check = is_electronic_check
        self.probability = probability
        self.churn = churn
    
    def to_dict(self, include_prob_churn=False):

        if include_prob_churn:
            return {
                'Fecha de ingreso': self.date,
                'Facturación mensual': self.is_month_to_month,
                'Internet': self.internet,
                'Fibra óptica': self.is_optical_fiber,
                'Cheque electrónico': self.is_electronic_check,
                'Probabilidad de abandono': self.probability,
                'Abandono': self.churn
            }
        
        return {
            'Fecha de ingreso': self.date,
            'Facturación mensual': self.is_month_to_month,
            'Internet': self.internet,
            'Fibra óptica': self.is_optical_fiber,
            'Cheque electrónico': self.is_electronic_check,
        }
    
    
    def map_entity(self):
        return {
            'days': self.days,
            'is_month_to_month': self.one_cero_nan(self.is_month_to_month),
            'is_fiber_optic': self.one_cero_nan(self.is_optical_fiber),
            'is_electronic_check': self.one_cero_nan(self.is_electronic_check),
            'internet': self.one_cero_nan(self.internet)
        }
    
    def one_cero_nan(self, value):
        if value == 'Si':
            return 1
        elif value == 'No':
            return 0
        else:
            return None
        


        