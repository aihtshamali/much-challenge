from typing import Tuple, Type
from src.Price.kwh_price import kWhPrice
from src.Price.time_price import TimePrice

class SupplierPrice:
    def __init__(
            self,
            id: str = None,
            company_name: str = None,
            currency: Tuple = None,
            transaction: Type[Transaction]= None,
            fee: Type[Fee] = None,
            timeprice: Type[TimePrice] = None,
            kWhprice: Type[kWHPrice] = None,
            ):

        self.id = id
        self.company_name = company_name
        self.currency = currency
        
        # No need to check for if both presents or not as
        # we should store the data whatever company provides us
        self.transaction = transaction
        self.fee = fee
        self.timeprice = timeprice
        self.kWhprice = kWhprice
