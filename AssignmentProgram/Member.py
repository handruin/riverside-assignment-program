class Member(object):
    """
    Base class to manage members as extracted from the MassHealth excel workbook.  Each member will have one or more
    Affiliate objects to represent that data.  This is used to condense the multiple duplicated rows for a given member
    and put the data that differs as new Affiliate objects associated to any given instance of a member object.
    """
    def __init__(self, medicaid_id, last_name, first_name, middle_initial, date_of_birth, residential_address_zipcode_1,
                 identification_flag):
        self.affiliates = []
        self.medicaid_id = medicaid_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.date_of_birth = date_of_birth
        self.residential_address_zipcode_1 = str(residential_address_zipcode_1).zfill(5)
        self.identification_flag = identification_flag
        self.is_assigned = False
        self.assignment_written = False

    def add_affiliate(self, affiliate):
        self.affiliates.append(affiliate)

    def has_affiliate_relationship(self, affiliate_name):
        for affiliate in self.affiliates:
            if affiliate.affiliate_name == affiliate_name:
                return True
        return False

    def assign_first_affiliate(self, affiliate_name):
        self.affiliates[0].assigned_to = affiliate_name
        self.is_assigned = True

    def get_affiliate_by_name(self, affiliate_name):
        for affiliate in self.affiliates:
            if affiliate.affiliate_name == affiliate_name:
                return affiliate

    def get_assigned_affiliate(self):
        for affiliate in self.affiliates:
            if affiliate.assigned_to:
                return affiliate.assigned_to
        return None

    def remove_all_affiliate_assignments(self):
        for affiliate in self.affiliates:
            affiliate.assigned_to = None
        self.is_assigned = False


class Affiliate(object):
    """
    A composition class associated with members as a way to condense and manage a member with multiple rows in the
    workbook.
    """
    def __init__(self, affiliate_name):
        self._affiliate_name = None
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

    @property
    def affiliate_name(self):
        return self._affiliate_name

    @affiliate_name.setter
    def affiliate_name(self, val):
        if val:
            self._affiliate_name = val.strip().lower()
