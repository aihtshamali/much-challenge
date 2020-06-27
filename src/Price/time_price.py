import json


class TimePrice:
    def __init__(self,
                 has_complex_min: bool,
                 simple_min_price: float = 0.0,
                 min_duration: float = 0.0,
                 has_hour_day: float = 0.0,
                 interval: str = None,

                 ):
        self.simple_min_price = simple_min_price
        self.has_complex_min = has_complex_min
        self.min_duration = min_duration
        self.has_hour_day = has_hour_day
        self.interval = interval
        # (Minute price value for the current timeframe)
        self.timeprices = []
        # self.minute_price = minute_price
        # # (the minimum value for a timeframe to be billed)
        # self.bill_per_frame = bill_per_frame
        # self.hour_from = hour_from  # Hour from (Start of the timeframe)
        # self.hour_to = hour_to  # Hour to (End of the timeframe)

    def set_value_timeframe(self):
        pass

    def add_timePrices(
            self,
            bill_per_frame: float,
            hour_from: float,
            hour_to: float,
            minute_price: float):
        self.timeprices.append({"bill_per_frame": bill_per_frame,
                                "hour_from": hour_from,
                                "hour_to": hour_to,
                                "minute_price": minute_price})

    def get_simple(self):
        """
         returns the simple time price
        """
        return dict({"simple_min_price": self.simple_min_price,
                     "min_duration": self.min_duration,
                     "has_complex_min": self.has_complex_min})

    def get_complex(self):
        """
         returns the complex time price
        """
        return dict({"has_complex_min": self.has_complex_min,
                     "has_hour_of_day": self.has_hour_day,
                     "interval": self.interval,
                     "min_duration": self.min_duration,
                     "timeprice": self.timeprices})

    def get_timePrice(self):
        """
         returns the current (Simple or Complex) timeprice of Supplier
        """

        if self.simple_min_price:
            return self.get_simple()
        else:
            return self.get_complex()
