from typing import Type,Dict
from datetime import datetime

"""
 Class of Transaction
 which holds all the transactions functionalities
"""


class Charges:
    def __init__(
            self,
            session_id: str = None,
            provider_id: str = None,
            evse_id: str = None,
            partner_prod_id: str = None,
            uid: str = None,
            metering_sign: str = None,
            charging_start: Type[datetime] = None,
            charging_end: Type[datetime] = None,
            session_start: Type[datetime] = None,
            session_end: Type[datetime] = None,
            meterV_start: Type[datetime] = None,
            meterV_end: Type[datetime] = None,
            country_code: str = None):

        self.session_id = session_id
        self.provider_id = provider_id
        self.evse_id = evse_id
        self.partner_prod_id = partner_prod_id
        self.uid = uid
        self.metering_sign = metering_sign
        self.charging_start = charging_start
        self.charging_end = charging_end
        self.session_start = session_start
        self.session_end = session_end
        self.meterV_start = meterV_start
        self.meterV_end = meterV_end
        self.country_code = country_code

    
    def setTransaction(self, transaction: Dict):
        """
            Set values from a transaction dictionary
        """
        self.session_id = transaction["session_id"]
        self.provide_id = transaction["provider_id"]
        self.evse_id = transaction["evse_id"]
        self.partner_prod_id = transaction["partner_prod_id"]
        self.uid = transaction["uid"]
        self.metering_sign = transaction["metering_sign"]
        self.charging_start = transaction["charging_start"]
        self.charging_end = transaction["charging_end"]
        self.session_start = transaction["session_start"]
        self.session_end = transaction["session_end"]
        self.meterV_start = transaction["meterV_start"]
        self.meterV_end = transaction["meterV_end"]
        self.country_code = transaction["country_code"]

