"""
The Assignment Program will use the following cascading criteria for assignment.  For each criterion listed, general
logic will include:
•	Does the referral <criteria>?
•	If NO, go to next selection criteria.
•	If YES, check AP’s capacity.  If YES capacity then assign to that AP and decrement that AP’s Capacity by one.
    Next record.
•	If capacity is NO then go to next selection criteria.

Assignment Criteria, in order of importance:
1.	Is Referral’s zip code within AP service area zip codes?
2.	Is Referral a current ACCS client at the AP organization?
3.	Is the Referral been a current PCP patient at the AP organization?
4.	Was the Referral a former CBFS client who did not transition to ACCS?
5.	Was the Referral a client of any Behavioral Health service program at the AP organization?
    a.	PACT
    b.	Respite, CCS, and other short term residential
    c.	Outpatient
    d.	Day Treatment
    e.	CSP
    f.	Emergency Services
6.	Was the Referral a client of any LTSS program at the AP organization?
7.	If a referral has no previous history with Riverside or the APs, then assignment will be based on Zip code, and
assigned to the program that matches the Zip code and which has the highest percentage of current capacity.
"""


class Rule(object):
    """
    Base class used for generic Rule management.
    """
    def __init__(self):
        self.rule_priority_base_multiplier = 100
        self.rule_priority = None
        self._member = None
        self._capacity_manager = None
        self._zipcode_manager = None
        self._member_affiliate_name = None
        self.rule_match = False
        self._rule_exceptions = []

    def process_rule(self):
        raise NotImplementedError("Error: This method should be implemented in child class!")

    def is_rule_met(self):
        return self.rule_match

    def does_ap_have_capacity(self):
        return self.capacity_manager.does_affiliate_have_capacity(self.assigned_member_affiliate_name)

    def assign_member(self, affiliate):
        self.member.assign_first_affiliate(affiliate)

    @property
    def assigned_member_affiliate_name(self):
        return self._member_affiliate_name

    @assigned_member_affiliate_name.setter
    def assigned_member_affiliate_name(self, affiliate_name):
        self._member_affiliate_name = affiliate_name

    @property
    def member(self):
        return self._member

    @member.setter
    def member(self, val):
        self._member = val

    @property
    def capacity_manager(self):
        return self._capacity_manager

    @capacity_manager.setter
    def capacity_manager(self, val):
        self._capacity_manager = val

    @property
    def zipcode_manager(self):
        return self._zipcode_manager

    @zipcode_manager.setter
    def zipcode_manager(self, val):
        self._zipcode_manager = val

    def register_rule_exception(self, member_rule_exception):
        self._rule_exceptions.append(member_rule_exception)

    def get_all_rule_exceptions(self):
        return self._rule_exceptions

    def process_match_and_capacity(self, affiliate):
        self.assigned_member_affiliate_name = affiliate.affiliate_name
        if self.does_ap_have_capacity():
            self.member.assign_first_affiliate(affiliate.affiliate_name)
            self.capacity_manager.decrement_capacity_from_affiliate(affiliate.affiliate_name)
            self.rule_match = True
        else:
            message = "The assigned affiliate: {0} does not have capacity.".format(affiliate.affiliate_name)
            self.register_rule_exception(MemberRuleException(self.member,
                                                             NoCapacityAssignmentError(message),
                                                             rule=self))


class ClientZipcodeInAPServiceAreaRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    1.	Is Referral’s zip code within AP service area zip codes?
    """

    def __init__(self, priority=1):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        member_zipcode = self.member.residential_address_zipcode_1
        if member_zipcode:
            affiliates_in_zipcode = self._zipcode_manager.get_affiliates_from_zipcode(member_zipcode)
            if not affiliates_in_zipcode:
                message = "The member zipcode: {0} does not have any matching affiliates.".format(member_zipcode)
                self.register_rule_exception(MemberRuleException(self.member,
                                                                 NoMatchingAffiliateAssignmentError(message),
                                                                 rule=self))

            for ap in affiliates_in_zipcode:
                if self.member.has_affiliate_relationship(ap):
                    self.assigned_member_affiliate_name = ap
                    if self.does_ap_have_capacity():
                        self.member.assign_first_affiliate(ap)
                        self.capacity_manager.decrement_capacity_from_affiliate(ap)
                        self.rule_match = True
                    else:
                        message = "The assigned affiliate: {0} does not have capacity.".format(ap)
                        self.register_rule_exception(MemberRuleException(self.member,
                                                                         NoCapacityAssignmentError(message),
                                                                         rule=self))


class CurrentACCSclientAPorganizationRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    2.	Is Referral a current ACCS client at the AP organization?
    ================= Question
    Is this checking Column (AY) for a value of "1"?
    YES
    """
    def __init__(self, priority=2):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        # look for ACCS field in Affiliates
        for affiliate in self.member.affiliates:
            if affiliate.is_accs:
                self.process_match_and_capacity(affiliate)


class SetACCSRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    """
    def __init__(self, priority=250):
        super().__init__()
        self.rule_priority = priority

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.is_accs is False \
                    and affiliate.affiliate_name is None \
                    and affiliate.is_cbfs is True:
                if self.member.identification_flag.lower() == "accs":
                    # TODO - change to logger instead of printing to stdout
                    # print("Rule met and set accs to True for {0}".format(self.member.first_name))
                    affiliate.is_accs = True


class CurrentPCPClientAPOrganizationRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    3.	Is the Referral been a current PCP patient at the AP organization?
    """
    def __init__(self, priority=3):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.is_pcp:
                self.process_match_and_capacity(affiliate)


class FormerCBFSWithoutTransitionACCSRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    4.    Was the Referral a former CBFS client who did not transition to ACCS?
    ================= Question
    Is this checking column "BA" for a value of "1" and column "AY" for no value?  How else can I detect a transition
    from CBFS to ACCS within all entries for a given person?
    YES – 1 in BA and AY is blank.
    """
    def __init__(self, priority=4):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.is_cbfs and not affiliate.is_accs:
                self.process_match_and_capacity(affiliate)


class ClientOfBehavioralServiceAPRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    5.	Was the Referral a client of any Behavioral Health service program at the AP organization?
        a.	PACT
        b.	Respite, CCS, and other short term residential
        c.	Outpatient
        d.	Day Treatment
        e.	CSP
        f.	Emergency Services
    """
    def __init__(self, priority=5):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.is_pact \
                    or affiliate.is_respite_or_css \
                    or affiliate.is_out_patient \
                    or affiliate.is_day_treatment \
                    or affiliate.is_csp \
                    or affiliate.is_emergency_svs:
                self.process_match_and_capacity(affiliate)


class ClientOfLTSSatAPRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    6.	Was the Referral a client of any LTSS program at the AP organization?
    """
    def __init__(self, priority=6):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.is_ltss:
                self.process_match_and_capacity(affiliate)


class ClientNoPriorHistoryZipcodeCapacityMatchRule(Rule):
    """
    Rule used for handling the assignments of members based on numerous conditions and priorities outlined below:
    7.	If a referral has no previous history with Riverside or the APs, then assignment will be based on Zip code, and
    assigned to the program that matches the Zip code and which has the highest percentage of current capacity.
    """
    def __init__(self, priority=7):
        super().__init__()
        self.rule_priority = priority * self.rule_priority_base_multiplier
        self._affiliate_partner_list = ["riverside", "lynn", "nsmha", "edinburg", "uphams", "dimock", "brookline"]

    def process_rule(self):
        for affiliate in self.member.affiliates:
            if affiliate.affiliate_name not in self._affiliate_partner_list:
                # Match zipcode then find AP with highest current capacity
                member_zipcode = self.member.residential_address_zipcode_1
                if member_zipcode:
                    affiliates_in_zipcode = self._zipcode_manager.get_affiliates_from_zipcode(member_zipcode)
                    if not affiliates_in_zipcode:
                        message = "The member zipcode: {0} does not have any matching affiliates."\
                            .format(member_zipcode)
                        self.register_rule_exception(MemberRuleException(self.member,
                                                                         NoMatchingAffiliateAssignmentError(message),
                                                                         rule=self))
                    highest_capacity_ap = self.capacity_manager.get_highest_capacity_by_affiliates(affiliates_in_zipcode)
                    if highest_capacity_ap:
                        self.member.assign_first_affiliate(highest_capacity_ap.ap)
                        self.capacity_manager.decrement_capacity_from_affiliate(highest_capacity_ap.ap)
                        self.rule_match = True
                    else:
                        message = "No capacity found for affiliate: {0}.".format(affiliates_in_zipcode)
                        self.register_rule_exception(MemberRuleException(self.member,
                                                                         NoCapacityAssignmentError(message),
                                                                         rule=self))


class FailedAssignmentRule(Rule):
    """
    This is a catch rule used to handle all members that are not captured by all previous rules.  This rule is set
    to be prioritized last when rules are assigned.  Do not adjust the priority unless you understand the implications
    of moving this rule into an earlier priority.  This rule will always return as the rule being met because it's a
    failure.  The importance of this rule is that it registers a rule exception to be managed after the assignment
    program is run.
    """
    def __init__(self, priority=999999999):
        super().__init__()
        self.rule_priority = priority

    def process_rule(self):
        message = "Warning: Failed member assignment.  Unable to process member after using all registered rules."
        self.register_rule_exception(MemberRuleException(self.member, AssignmentError(message), rule=self))
        self.rule_match = False

    def is_rule_met(self):
        """
        Override from parent to ensure this always returns true for errors.
        :return: Boolean
        """
        return True


class MemberRuleException(object):
    """
    Class used to manage internal exception handling to be collated and managed after the assignment program completes.
    """
    def __init__(self, member, assignment_error_type, rule=None):
        self.member = member
        self.assignment_error_type = assignment_error_type
        self.exception_message = self.assignment_error_type.message
        self.rule = rule


class RuleProcessing(object):
    """
    The core of managing and processing all assigned rule objects of type Rule.  All Rule objects are iterated through
    and call the process_rule method through polymorphism so that all rules are executed the same.

    Also managed the rule exceptions that are generated through processing and can be called to process after rules
    are run.  This class holds handles to the member, capacity manager, and zipcode manager.
    """
    def __init__(self, member, capacity_manager, zipcode_manager):
        self._rules = []
        self.member = member
        self.capacity_manager = capacity_manager
        self.zipcode_manager = zipcode_manager
        self._member_rule_exceptions = []

    def assign_rule(self, rule):
        rule.member = self.member
        rule.zipcode_manager = self.zipcode_manager
        rule.capacity_manager = self.capacity_manager
        self.check_rule_have_priority_conflict(rule)
        self._rules.append(rule)

    def check_rule_have_priority_conflict(self, new_rule):
        for rule in self._rules:
            if rule.rule_priority == new_rule.rule_priority:
                raise Exception("Multiple rules {0} and {1} conflict with the same priority.".format(rule, new_rule))

    def get_rules_prioritized(self):
        self._rules.sort(key=lambda x: x.rule_priority, reverse=False)
        return self._rules

    @property
    def member_rule_exceptions(self):
        return self._member_rule_exceptions

    @member_rule_exceptions.setter
    def member_rule_exceptions(self, member):
        self._member_rule_exceptions.extend(member)

    def has_rule_exception(self):
        return len(self.member_rule_exceptions) > 0

    def process(self):
        if not self.member.is_assigned:
            for rule in self.get_rules_prioritized():
                rule.process_rule()
                self.member_rule_exceptions = rule.get_all_rule_exceptions()
                if rule.is_rule_met():
                    return


class AssignmentError(object):
    """
    Basic parent error type to be extended to manage errors by class type
    """
    def __init__(self, message):
        self.message = message


class NoMatchingAffiliateAssignmentError(AssignmentError):
    """
    Basic error type when no matching affiliates can be found.
    """
    def __init__(self, message):
        super().__init__(message)


class NoCapacityAssignmentError(AssignmentError):
    """
    Basic error type when there is no capacity for a given affiliate program.
    """
    def __init__(self, message):
        super().__init__(message)
