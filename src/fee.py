
class Fee:
    def __init__(self,
                 has_min_billing_thresh: bool,
                 has_session_fee: bool,
                 has_max_session_fee: bool,
                 session_fee: float,
                 max_session_fee: float
                ):
        self.has_min_billing_thresh = has_min_billing_thresh
        self.has_session_fee = has_session_fee
        self.has_max_session_fee = has_max_session_fee
        self.session_fee = session_fee
        self.max_session_fee = max_session_fee