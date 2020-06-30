# imports start
import requests
from typing import Dict, AnyStr
from datetime import datetime
from src.Price.kwh_price import kWhPrice
from src.Price.time_price import TimePrice
from src.charges import Charges
from src.fee import Fee
from src.utility.helpers import *
# imports end

"""
Parse Data Class,  Parse the Data
and store them in appropriate Data Types

"""


class ParseData:
    def __init__(self):
        self.transactions = list()
        self.supplier_prices = list()

    def readFromUrl(self, url: str, uname: str, pwd: str) -> Dict:
        """ Read from a specific URL
            \nParameters:
                \n\turl: string
                \n\tname: string
                \n\tpwd: string
            \n@return JSON
        """

        data = requests.get(
            url=url,
            auth=(uname, pwd))

        return data.json()

    def parseData(self, url: str, uname: str, pwd: str):
        """ Parse data and stores it into appropriate Objects
        """
        try:
            # fetching the raw data
            raw_data = self.readFromUrl(url, uname, pwd)

            # Calling two seperate functions to explode the data
            self.parseTransactions(raw_data["transactions"])
            self.parseSupplier(raw_data["supplier_prices"])
            
        except Exception as e:
            print("An Exception occured @ -> parseData() ", e)

    def parseSupplier(self, supplier_data: Dict) -> Dict:
        """
        parse the Supplier data
        """
        try:
            for supplier in supplier_data:
                updatedSupplier = self.typeCastSupplier(supplier)
                # Adding into transactions
                self.transactions.append(updatedSupplier)
        except Exception as e:
            print(
                "Exception occured while parsing Transactions/Charges @ -> parseSupplier",
                e)

    def parseTransactions(self, transactions: Dict) -> Dict:
        try:
            for transaction in transactions:

                updatedTransaction = self.typeCastTransaction(transaction)
                charge = Charges()
                charge.setTransaction(updatedTransaction)
                # print(charge.evse_id)
                self.transactions.append(charge)
        except Exception as e:
            print(
                "Exception occured while parsing Transactions/Charges @ -> parseTransactions",
                e)

    def typeCastTransaction(self, transaction: Dict) -> Dict:
        try:
            updatedTransaction = {}
            # Type casting and storing them in updatedTrans Dict

            updatedTransaction.update({"charging_start": datetime.strptime(
                transaction["Charging start"], '%Y-%m-%dT%H:%M:%S').strftime('%d %m %Y %H:%m:%S')})
            updatedTransaction.update({"charging_end": datetime.strptime(
                transaction["Charging end"], '%Y-%m-%dT%H:%M:%S').strftime('%d %m %Y %H:%m:%S')})
            updatedTransaction.update(
                {"meterV_start": float(
                    transaction["Meter value start"].replace(",", ""))})
            updatedTransaction.update(
                {"meterV_end": float(
                    transaction["Meter value end"].replace(",", ""))})
            updatedTransaction.update({"session_start": datetime.strptime(
                transaction["Session start"], '%Y-%m-%dT%H:%M:%S').strftime('%d %m %Y %H:%m:%S')})
            updatedTransaction.update({"session_end": datetime.strptime(
                transaction["Session end"], '%Y-%m-%dT%H:%M:%S').strftime('%d %m %Y %H:%m:%S')})
            updatedTransaction.update({
                "country_code": str(
                    transaction["CountryCode"])})
            updatedTransaction.update({
                "evse_id": checkandConvertToStr(transaction,"EVSEID")})
# //                    transaction["EVSEID"] if transaction["EVSEID"] else None)})
            updatedTransaction.update({"partner_prod_id": str(
                transaction["Partner product ID"] if transaction["Partner product ID"] else None)})
            updatedTransaction.update({
                "metering_sign": str(
                    transaction["Metering signature"])})
            updatedTransaction.update({
                "provider_id": str(
                    transaction["Proveider ID"])})
            updatedTransaction.update({
                "session_id": str(
                    transaction["Session ID"])})
            updatedTransaction.update({
                "uid": str(
                    transaction["UID"])})

        except Exception as e:
            print(
                "Exception occured while parsing single Transaction @ -> typeCastTransaction",
                e)
        finally:
            return updatedTransaction

    def typeCastSupplier(self, supplier: Dict) -> Dict:
        """
            Type Cast the Supplier Object into Python Data Types
        """
        try:
            updatedSupplier = {}

            # Type casting and storing them in updatedTrans Dict
            updatedSupplier.update(
                {"company_name": str(supplier["Company name"])})
            # storing curreny in tuple
            updatedSupplier.update({
                "currency":
                (supplier["Currency"][0],
                    supplier["Currency"][1])})
            updatedSupplier.update(
                {"evse_id": checkandConvertToStr(supplier, "EVSE ID")})
            updatedSupplier.update(
                {"uid": checkandConvertToStr(supplier, "Identifier")})

            updatedSupplier.update(
                {"partner_prod_id": checkandConvertToStr(supplier, "Product ID")})

            # checking if its fee type or else
            # if supplier["max_session fee"] != "False":
            # covert string into python native dataTypes
            fee = Fee(
                has_min_billing_thresh=checkandConvertToBool(
                    supplier, "has minimum billing threshold"), has_max_session_fee=checkandConvertToBool(
                    supplier, "has max session Fee"), has_session_fee=checkandConvertToBool(
                    supplier, "has session fee"), session_fee=checkandConvertToFloat(
                    supplier, "session Fee"), max_session_fee=checkandConvertToFloat(
                        supplier, "max_session fee"))
            #  Storing the Fee object in Supplier list
            updatedSupplier.update({"fee": Fee})

            # Check if key exists and has the complex minute price
            # if "has complex minute price" in supplier and supplier["has complex minute price"]:
            # print(supplier)
            time = TimePrice(
                has_complex_min=checkandConvertToBool(
                    supplier, "has complex minute price"), simple_min_price=checkandConvertToFloat(
                    supplier, "simple minute price"), min_duration=checkandConvertToFloat(
                    supplier, "min_duration"))

            # Check if its complex then add else return the above one
            if checkandConvertToBool(supplier, "has complex minute price"):
                time.has_hour_day = checkandConvertToBool(
                    supplier, "has hour day")
                time.interval = checkandConvertToStr(supplier, "interval")
                time.min_duration = checkandConvertToFloat(
                    supplier, "min duration")

                # if it has hour of day then add timeprice attributes
                if "has hour day" in supplier:
                    for timeprice in supplier["time_price"]:
                        time.add_timePrices(
                            checkandConvertToFloat(
                                supplier, "billing_each_timeframe"), checkandConvertToFloat(
                                supplier, "hour from"), checkandConvertToFloat(
                                supplier, "hour to"), checkandConvertToFloat(
                                supplier, "minute price"))

            # Adding the complex/simple time
            updatedSupplier.update({"time": time.get_timePrice()})

            # for KWH
            kwh = kWhPrice(
                has_kWh_price=checkandConvertToBool(
                    supplier, "has time based kwh"), kWh_price=checkandConvertToFloat(
                    supplier, "kwh Price"), min_consumption=checkandConvertToFloat(
                    supplier, "min cosumed energy"))
            # Complex
            if checkandConvertToBool(supplier, "has time based kwh"):
                kwh.has_time_based = checkandConvertToBool(
                    supplier, "has time based kwh")
                kwh.min_consumption = checkandConvertToFloat(
                    supplier, "min consumption")
                kwh.has_hour_day = checkandConvertToBool(
                    supplier, "has hour day")

                for timeprice in supplier["time_price"]:
                    kwh.add_timePrices(
                        kWh_price=checkandConvertToFloat(
                            supplier["time_price"], "kwh price"), hour_from=checkandConvertToFloat(
                            supplier["time_price"], "hour from"), hour_to=checkandConvertToFloat(
                            supplier["time_price"], "hour to"))
            # Add kwhObject in Supplier
            updatedSupplier.update({"kwh": kwh})
        except Exception as e:
            print("Exception occured @ -> typeCastSupplier", e)
        finally:
            return updatedSupplier

    def searchOneChargeByEVSEID(self,evseId: str) -> Dict:
        for ele in self.transactions:
            print(ele.evse_id)
        # print([transaction for transaction in self.transactions if transaction.evse_id == evseId])
        # return {}

    