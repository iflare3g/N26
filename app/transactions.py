import time
from functools import reduce

class Transaction:
    def __init__(self):
        self.transaction = []
        
    def create_body(self,amount,timestamp):
        self.body = {
            'amount':amount,
            'timestamp':timestamp
        }
        return self.body
        
    def get_transactions(self,transaction):
        all_transactions = list(map(lambda trans:trans,transaction))
        all_trans_last_sixty = list(filter(lambda item:self.check_time(item.get('timestamp')),all_transactions))
        all_amounts_last_sixty = list(map(lambda trans:float(trans.get('amount')),all_trans_last_sixty))
        statistics = {}
        all_trans_last_sixty_length = len(all_trans_last_sixty)
        try:
            
            statistics = {
                'sum':sum(map(lambda trans:float(trans.get('amount')),all_trans_last_sixty)),
                'max':max(map(lambda trans:float(trans.get('amount')),all_trans_last_sixty),default=0),
                'min':min(map(lambda trans:float(trans.get('amount')),all_trans_last_sixty),default=0),
                'count':len(all_trans_last_sixty),
                'avg': reduce(lambda x,y:x + y,all_amounts_last_sixty,0)/all_trans_last_sixty_length if all_trans_last_sixty_length > 0 else 0
            }
        
        except ZeroDivisionError:
            print("Divison by 0 is not possible")
        
        return statistics
        
    def check_time(self,timestamp):
        if time.time() - float(timestamp) < 59:
            return True
        else:
            print("One minute passed!")
            return False
        
    
        
    
        