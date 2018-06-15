class Member(object):
    def __init__(self, medicaid_id, last_name, first_name, middle_initial, date_of_birth):
        self.affiliates = []
        self.medicaid_id = medicaid_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.date_of_birth = date_of_birth

    def add_affiliate(self, affiliate):
        self.affiliates.append(affiliate)


class Affiliate(object):
    def __init__(self, affiliate_name):
        self.affiliate_name = affiliate_name
        self.is_accs = False
        self.is_pcp = False
        self.is_cbfs = False
        self.is_pact = False
        self.is_respite_or_css = False
        self.is_out_patient = False
        self.is_day_treatment = False
        self.is_csp = False
        self.is_emergency_svs = False
        self.is_ltss = False
        self.assigned_to = None
