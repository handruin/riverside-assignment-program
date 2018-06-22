from openpyxl import load_workbook

from AssignmentProgram.Member import Member, Affiliate

# Temporary way to obscure name of file being read in for privacy concerns.
with open('parse_file_name.txt') as f:
    file_name = f.read()
masshealth_wb = load_workbook(file_name)

active_sheet = masshealth_wb.active
obj_members = []
members = {}

member_attributes = {
    "medicaid_id": "A",
    "member_last_name": "B",
    "member_first_name": "C",
    "member_middle_initial": "D",
    "member_date_of_birth": "F",
    "residential_address_zipcode_1": "W",
    "identification_flag": "AT",
    "affiliate": "AX",
    "accs": "AY",
    "pcp": "AZ",
    "cbfs": "BA",
    "pact": "BB",
    "respite_or_ccs": "BC",
    "out_patient": "BD",
    "day_treatment": "BE",
    "csp": "BF",
    "emergency_svs": "BG",
    "ltts": "BH",
    "assigned_to": "BI",
}


def member_exists(all_members, new_member):
    for member in all_members:
        if member.medicaid_id == new_member.medicaid_id \
                and member.last_name == new_member.last_name \
                and member.first_name == new_member.first_name \
                and member.middle_initial == new_member.middle_initial \
                and member.date_of_birth == new_member.date_of_birth:
            return True
    return False


def get_existing_member(all_members, new_member):
    for member in all_members:
        if member.medicaid_id == new_member.medicaid_id \
                and member.last_name == new_member.last_name \
                and member.first_name == new_member.first_name \
                and member.middle_initial == new_member.middle_initial \
                and member.date_of_birth == new_member.date_of_birth:
            return member
    return None


def get_record(row, column, active_sheet):
    cell_name = "{}{}".format(column, row)
    if active_sheet[cell_name].value:
        if not isinstance(active_sheet[cell_name].value, int):
            val = active_sheet[cell_name].value.lower()
        else:
            val = active_sheet[cell_name].value
        return val


def is_empty_member(member):
    if member.medicaid_id is None \
            and member.last_name is None \
            and member.first_name is None \
            and member.middle_initial is None \
            and member.date_of_birth is None \
            and member.identification_flag is None:

        for affiliate in member.affiliates:
            if is_affiliate_empty(affiliate):
                return True
    return False


def is_affiliate_empty(affiliate):
    if affiliate.affiliate_name is None \
            and affiliate.is_accs is False \
            and affiliate.is_pcp is False \
            and affiliate.is_cbfs is False \
            and affiliate.is_pact is False \
            and affiliate.is_respite_or_css is False \
            and affiliate.is_out_patient is False \
            and affiliate.is_day_treatment is False \
            and affiliate.is_csp is False \
            and affiliate.is_emergency_svs is False \
            and affiliate.is_ltss is False \
            and affiliate.assigned_to is None:
        return True
    return False


def update_member_affiliates(all_members, new_member):
    member = get_existing_member(all_members, new_member)
    for affiliate in new_member.affiliates:
        member.add_affiliate(affiliate)


def process_members():
    for row in range(2, active_sheet.max_row + 1):
        new_obj_member = Member(get_record(row, member_attributes['medicaid_id'], active_sheet),
                                get_record(row, member_attributes['member_last_name'], active_sheet),
                                get_record(row, member_attributes['member_first_name'], active_sheet),
                                get_record(row, member_attributes['member_middle_initial'], active_sheet),
                                get_record(row, member_attributes['member_date_of_birth'], active_sheet),
                                get_record(row, member_attributes['residential_address_zipcode_1'], active_sheet),
                                get_record(row, member_attributes['identification_flag'], active_sheet))

        new_obj_affiliate = Affiliate(get_record(row, member_attributes['affiliate'], active_sheet))
        new_obj_affiliate.is_accs = bool(int(get_record(row, member_attributes['accs'], active_sheet) or 0))
        new_obj_affiliate.is_pcp = bool(int(get_record(row, member_attributes['pcp'], active_sheet) or 0))

        new_obj_affiliate.is_cbfs = bool(int(get_record(row, member_attributes['cbfs'], active_sheet) or 0))
        new_obj_affiliate.is_pact = bool(int(get_record(row, member_attributes['pact'], active_sheet) or 0))
        new_obj_affiliate.is_respite_or_ccs = bool(
            int(get_record(row, member_attributes['respite_or_ccs'], active_sheet) or 0))
        new_obj_affiliate.is_out_patient = bool(
            int(get_record(row, member_attributes['out_patient'], active_sheet) or 0))
        new_obj_affiliate.is_day_treatment = bool(
            int(get_record(row, member_attributes['day_treatment'], active_sheet) or 0))
        new_obj_affiliate.is_csp = bool(int(get_record(row, member_attributes['csp'], active_sheet) or 0))
        new_obj_affiliate.is_emergency_svs = bool(
            int(get_record(row, member_attributes['emergency_svs'], active_sheet) or 0))
        new_obj_affiliate.is_ltts = bool(int(get_record(row, member_attributes['ltts'], active_sheet) or 0))
        new_obj_affiliate.assigned_to = get_record(row, member_attributes['assigned_to'], active_sheet)

        new_obj_member.add_affiliate(new_obj_affiliate)

        if not is_empty_member(new_obj_member):
            if member_exists(obj_members, new_obj_member):
                update_member_affiliates(obj_members, new_obj_member)
            else:
                obj_members.append(new_obj_member)


# print(len(obj_members))


def process_rules(member):
    rule_set_accs(member)


def rule_set_accs(member):
    for affiliate in member.affiliates:
        if affiliate.is_accs is False \
                and affiliate.affiliate_name is None \
                and affiliate.is_cbfs is True:
            if mem.identification_flag.lower() == "accs":
                # TODO - change to logger instead of printing to stdout
                print("Rule met and set accs to True for {0}".format(member.first_name))
                affiliate.is_accs = True


process_members()


for mem in obj_members:
    process_rules(mem)
    for affiliate in mem.affiliates:
        print("{0} - affiliate name: {1}, is_accs: {2}, zipcode: {3}".format(mem.first_name, affiliate.affiliate_name, affiliate.is_accs, mem.residential_address_zipcode_1))

exit(0)

# Rules:
# if accs is None and affiliate is None and cbfs is not None:
# if identification_flag.lower() == "ACCS".lower()
#   set accs = 1
