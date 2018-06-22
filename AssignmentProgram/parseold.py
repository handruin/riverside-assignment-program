# def member_exists(all_members, new_member):
#     for _, member in all_members.items():
#         if member['member']['medicaid_id'] == new_member['member']['medicaid_id'] \
#                 and member['member']['member_last_name'] == new_member['member']['member_last_name'] \
#                 and member['member']['member_first_name'] == new_member['member']['member_first_name'] \
#                 and member['member']['member_middle_initial'] == new_member['member']['member_middle_initial'] \
#                 and member['member']['member_date_of_birth'] == new_member['member']['member_date_of_birth']:
#             return True
#     return False


#    print(vars(new_obj_member).values())

# if not all((value is None for value in vars(new_obj_member).values())):
#     print("all found")
# print(vars(new_obj_member))
# print(vars(new_obj_affiliate))
# exit(0)
# if not all((value is None for value in new_member['member'].values())
#            and (value is None for value in new_member['member']['affiliates'].values())):


# for row in range(2, active_sheet.max_row+1):
#     # Temp dictionary to get data from the spreadsheet.  This will be converted to a class structure Member/Affiliate.
#     new_member = {
#         "member": {
#             "medicaid_id": get_record(row, member_attributes['medicaid_id'], active_sheet),
#             "member_last_name": get_record(row, member_attributes['member_last_name'], active_sheet),
#             "member_first_name": get_record(row, member_attributes['member_first_name'], active_sheet),
#             "member_middle_initial": get_record(row, member_attributes['member_middle_initial'], active_sheet),
#             "member_date_of_birth": get_record(row, member_attributes['member_date_of_birth'], active_sheet),
#             "identification_flag": get_record(row, member_attributes['identification_flag'], active_sheet),
#             "affiliates": {
#                 "affiliate": get_record(row, member_attributes['affiliate'], active_sheet),
#                 "accs": get_record(row, member_attributes['accs'], active_sheet),
#                 "pcp": get_record(row, member_attributes['pcp'], active_sheet),
#                 "cbfs": get_record(row, member_attributes['cbfs'], active_sheet),
#                 "pact": get_record(row, member_attributes['pact'], active_sheet),
#                 "respite_or_ccs": get_record(row, member_attributes['respite_or_ccs'], active_sheet),
#                 "out_patient": get_record(row, member_attributes['out_patient'], active_sheet),
#                 "day_treatment": get_record(row, member_attributes['day_treatment'], active_sheet),
#                 "csp": get_record(row, member_attributes['csp'], active_sheet),
#                 "emergency_svs": get_record(row, member_attributes['emergency_svs'], active_sheet),
#                 "ltts": get_record(row, member_attributes['ltts'], active_sheet),
#                 "assigned_to": get_record(row, member_attributes['assigned_to'], active_sheet)
#             }
#         }
#     }
#     new_obj_member = Member(get_record(row, member_attributes['medicaid_id'], active_sheet),
#                             get_record(row, member_attributes['member_last_name'], active_sheet),
#                             get_record(row, member_attributes['member_first_name'], active_sheet),
#                             get_record(row, member_attributes['member_middle_initial'], active_sheet),
#                             get_record(row, member_attributes['member_date_of_birth'], active_sheet),
#                             get_record(row, member_attributes['identification_flag'], active_sheet))
#
#     new_obj_affiliate = Affiliate(get_record(row, member_attributes['affiliate'], active_sheet))
#     new_obj_affiliate.is_accs = bool(int(get_record(row, member_attributes['accs'], active_sheet) or 0))
#     new_obj_affiliate.is_pcp = bool(int(get_record(row, member_attributes['pcp'], active_sheet) or 0))
#
#     new_obj_affiliate.is_cbfs = bool(int(get_record(row, member_attributes['cbfs'], active_sheet) or 0))
#     new_obj_affiliate.is_pact = bool(int(get_record(row, member_attributes['pact'], active_sheet) or 0))
#     new_obj_affiliate.is_respite_or_ccs = bool(int(get_record(row, member_attributes['respite_or_ccs'], active_sheet) or 0))
#     new_obj_affiliate.is_out_patient = bool(int(get_record(row, member_attributes['out_patient'], active_sheet) or 0))
#     new_obj_affiliate.is_day_treatment = bool(int(get_record(row, member_attributes['day_treatment'], active_sheet) or 0))
#     new_obj_affiliate.is_csp = bool(int(get_record(row, member_attributes['csp'], active_sheet) or 0))
#     new_obj_affiliate.is_emergency_svs = bool(int(get_record(row, member_attributes['emergency_svs'], active_sheet) or 0))
#     new_obj_affiliate.is_ltts = bool(int(get_record(row, member_attributes['ltts'], active_sheet) or 0))
#     new_obj_affiliate.assigned_to = get_record(row, member_attributes['assigned_to'], active_sheet)
#
#     new_obj_member.add_affiliate(new_obj_affiliate)
#
#     # TODO - figure out how to look for empty rows now that we are using class objects.
#     # Check to make sure all values in a dictionary (row) are not None...meaning empty rows found in the xlsx
#     if not all((value is None for value in new_member['member'].values())
#                and (value is None for value in new_member['member']['affiliates'].values())):
#         members[row] = new_member
#         # if member_exists(members, new_member):
#         #     pass
#         #     # print('Exists')
#         #     # We found the same member in the dictionary, so let's update them.
#         #     # print('Fetching member medicaid_id: {0}'.format(members[row]['member']['medicaid_id'].get(new_member['member']['medicaid_id'])))
#         # else:
#         #     members[row] = new_member


# Now we have all members including any duplicates that need to be processed.
# for k, v in members.items():
#     print('{} - {}'.format(k, v))
