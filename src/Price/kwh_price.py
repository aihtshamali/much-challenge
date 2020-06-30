from typing import Dict
import json
import datetime


class kWhPrice:
    def __init__(self,
                 has_kWh_price: bool = False,
                 kWh_price: float = 0.0,
                 min_consumption: float = 0.0,
                 has_hour_day: bool = False,
                 has_time_based: bool = False,
                 ):

        self.has_kWh_price = has_kWh_price
        self.kWh_price = kWh_price
        self.min_consumption = min_consumption
        self.has_hour_day = has_hour_day
        self.has_time_based = has_time_based

        self.time_prices = list()
        # self.hour_from = hour_from
        # self.hour_to = hour_to
    

    def add_timePrices(self,
            kWh_price: float,
            hour_from: float,
            hour_to: float,
            ):
        self.time_prices.append({"time_price": {
                                "hour_from": hour_from,
                                "hour_to": hour_to,
                                "kWh_price": kWh_price}})

    def getSimple(self) -> Dict:
        """
            Get Simple kWh Price
        """

        return dict({"has_kWh_price": self.has_kWh_price,
                           "kWh_price": self.kWh_price,
                           "min_consumption": self.min_consumption})

    def getComplex(self) -> Dict:
        """
            Get Complex kWh Price
        """

        data = self.getSimple()
        data.update(self.time_prices)
        return data

    def getkWhPrice(self) -> Dict:
        """
        Get Current kWh Price
        \n "Complex"  if it time prices length > 0 
        \n  else  "Simple" 
        """
        return self.getComplex() if len(self.time_prices) else self.getSimple()
