from abc import ABCMeta, abstractmethod

from CommunityPartner.CommunityPartnerDataType import DataType
from CommunityPartner.CommunityPartnerOrgType import OrgType
from CommunityPartner.CommunityPartnerRequiredLockedState import RequiredLockState


class CommunityPartnerField(object):
    """
    Abstract class to define the structure of each given Community Partner Fields.
    """
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def field_id():
        """
        e.g. 1.6.1.1
        :return: String
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def field_name():
        """
        e.g. Medicaid_ID
        :return: String
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def size():
        """
        The size of the field: e.g. 12
        :return: Int
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def required_or_locked():
        """
        Note: The "R" indicates Required fields. "L" indicates Locked fields that should not be changed by the
        ACO, MCO or CP if they have been pre-populated by MassHealth. "O" indicates optional fields that MassHealth
        intends to supply when/if possible, or that the ACO or MCO may supply.
        :return: List<RequiredLockedState>
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def data_type():
        """
        The data type of the stored value: e.g. String, Date, Int
        :return:
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def end_user():
        """
        MassHealth
        ACO/MCO
        CP
        :return: List<OrgType>
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def supplier():
        """
        MassHealth
        ACO/MCO
        :return: List<OrgType>
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def format():
        """
        Option format field when needed.  Example: Date
        :return: String
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def valid_values():
        """
        A subset of allowed values for an implemented field.  E.g.: M, F, U (unknown)
        :return: String
        """
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def description():
        """
        A text description of the implemented field type.
        :return:
        """
        raise NotImplementedError


class MedicaidID(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.1'

    @staticmethod
    def field_name():
        return 'Medicaid_ID'

    @staticmethod
    def size():
        return 12

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's MassHealth ID **Required by ACO/MCO-CP Agreement"


class MemberNameLast(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.2'

    @staticmethod
    def field_name():
        return 'Member_Name_Last'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's Last Name **Required by ACO/MCO-CP Agreement"


class MemberNameFirst(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.3'

    @staticmethod
    def field_name():
        return 'Member_Name_First'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's First Name **Required by ACO/MCO-CP Agreement"


class MemberMiddleInitial(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.4'

    @staticmethod
    def field_name():
        return 'Member_Middle_Initial'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's Middle Initial **Required by ACO/MCO-CP Agreement"


class MemberSuffix(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.5'

    @staticmethod
    def field_name():
        return 'Member_Suffix'

    @staticmethod
    def size():
        return 20

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's Suffix **Required by ACO/MCO-CP Agreement"


class MemberDateOfBirth(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.6'

    @staticmethod
    def field_name():
        return 'Member_Date_of_Birth'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.DATE

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return "YYYYMMDD"

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's Date of Birth **Required by ACO/MCO-CP Agreement"


class MemberSex(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.7'

    @staticmethod
    def field_name():
        return 'Member_Sex'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['M', 'F', 'U']

    @staticmethod
    def description():
        return "Member's Sex"


class ACOMCOName(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.8'

    @staticmethod
    def field_name():
        return 'ACO_MCO_Name'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "ACO/MCO's name as recorded in DW"


class ACOMCOPID(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.9'

    @staticmethod
    def field_name():
        return 'ACO_MCO_PID'

    @staticmethod
    def size():
        return 9

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "ACO/MCO's Provider ID"


class ACOMCOSL(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.10'

    @staticmethod
    def field_name():
        return 'ACO_MCO_SL'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "ACO/MCO's Provider Service Location"


class HealthPlanID(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.11'

    @staticmethod
    def field_name():
        return 'Health_Plan_ID'

    @staticmethod
    def size():
        return 50

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.ACOMCO

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Member's Health plan ID; ACO/MCO would have to populate this field, as MassHealth does not know this " \
               "***Requested by CP"


class MemberCPAssignmentPlan(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.12'

    @staticmethod
    def field_name():
        return 'Member_CP_Assignment_Plan'

    @staticmethod
    def size():
        return 5

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED, RequiredLockState.LOCKED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['BHCP', 'LTSS', 'ELTSS', 'ACCS1', 'PACC1', 'ACCS2', 'PACC2', 'CSA']

    @staticmethod
    def description():
        return "Member's Program  In the case of a new Enrollment populated by an ACO/MCO, it is requested that the " \
               "ACO/MCO leave this field blank, as MassHealth intends to make appropriate Assignment Plan " \
               "enrollments. Further details provided in the CP Assignment and Outreach Guidance released in May 2018. "


class CPNameDSRIP(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.13'

    @staticmethod
    def field_name():
        return 'CP_Name_DSRIP'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Name that CP is called by for DSRIP and Finance Payment Purposes. When an ACO/MCO does a referral, " \
               "they do not need to fill in this field."


class CPNameOfficial(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.14'

    @staticmethod
    def field_name():
        return 'CP_Name_Official'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Name that CP is called by in MMIS (\"MMIS Enrollment Name (DBA)\" in Section 2.2 of this " \
               "Specifications Document). When an ACO/MCO does a referral, they should utilize the official " \
               "name of the CP. MassHealth will provide a list of CP names and PID/SLs."


class CPPID(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.15'

    @staticmethod
    def field_name():
        return 'CP_PID'

    @staticmethod
    def size():
        return 9

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "CP's Provider ID that CP is called by in MMIS. When an ACO/MCO does a referral, they should utilize " \
               "the official name of the CP. MassHealth will provide a list of CP names and PID/SLs."


class CPSL(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.16'

    @staticmethod
    def field_name():
        return 'CP_SL'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "CP's Service Location that CP is called by in MMIS. When an ACO/MCO does a referral, they should " \
               "utilize the official name of the CP. MassHealth will provide a list of CP names and PID/SLs."


class EnrollmentStartDate(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.17'

    @staticmethod
    def field_name():
        return 'Enrollment_Start_Date'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.DATE

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return OrgType.MASSHEALTH

    @staticmethod
    def format():
        return "YYYYMMDD"

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Start date of member's enrollment in CP. Must be first of the month. No partial month enrollments " \
               "will be allowed."


class StartReasonDesc(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.18'

    @staticmethod
    def field_name():
        return 'Start_Reason_Desc'

    @staticmethod
    def size():
        return 105

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['MH-Identified', 'ACO Referred', 'CP Referred', 'Provider Referred',
                'Enrollee Requested Change', 'ACO/MCO Requested Change', 'DMH Referred']

    @staticmethod
    def description():
        return "How the member was identified for enrollment in CP. Further details provided in the CP Assignment " \
               "and Outreach Guidance released in May 2018."


class ResidentialAddressLineOne(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.19'

    @staticmethod
    def field_name():
        return 'Residential_Address_Line_1'

    @staticmethod
    def size():
        return 50

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class ResidentialAddressLineTwo(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.20'

    @staticmethod
    def field_name():
        return 'Residential_Address_Line_2'

    @staticmethod
    def size():
        return 50

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class ResidentialAddressCity(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.21'

    @staticmethod
    def field_name():
        return 'Residential_Address_City'

    @staticmethod
    def size():
        return 40

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class ResidentialAddressState(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.22'

    @staticmethod
    def field_name():
        return 'Residential_Address_State'

    @staticmethod
    def size():
        return 2

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class ResidentialAddressZipCodeOne(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.23'

    @staticmethod
    def field_name():
        return 'Residential_Address_ZipCode_1'

    @staticmethod
    def size():
        return 5

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Should include only first 5 digits of zipcode.  **Required by ACO/MCO-CP Agreement"


class ResidentialAddressZipCodeTwo(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.24'

    @staticmethod
    def field_name():
        return 'Residential_Address_ZipCode_2'

    @staticmethod
    def size():
        return 4

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Zipcode 4-digit extension."


class Email(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.25'

    @staticmethod
    def field_name():
        return 'Email'

    @staticmethod
    def size():
        return 60

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Requested by CPs"


class PhoneNumberCell(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.26'

    @staticmethod
    def field_name():
        return 'Phone_Number_Cell'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PhoneNumberDay(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.27'

    @staticmethod
    def field_name():
        return 'Phone_Number_Day'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PhoneNumberNight(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.28'

    @staticmethod
    def field_name():
        return 'Phone_Number_Day'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PrimaryLanguageSpokenDesc(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.29'

    @staticmethod
    def field_name():
        return 'Primary_Language_Spoken_Desc'

    @staticmethod
    def size():
        return 109

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "List of languages known by MassHealth will be provided. Should use Description, not code. " \
               "**Required by ACO/MCO-CP Agreement"


class PrimaryDiagnosis(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.30'

    @staticmethod
    def field_name():
        return 'Primary_Diagnosis'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "MassHealth cannot populate this field due to 42CFR Part 2. ACOs/MCOs may add this information in " \
               "compliance with applicable laws and regulations.  ***Requested by CPs"


class SecondaryDiagnosis(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.31'

    @staticmethod
    def field_name():
        return 'Secondary_Diagnosis'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "MassHealth cannot populate this field due to 42CFR Part 2. ACOs/MCOs may add this information in " \
               "compliance with applicable laws and regulations.  ***Requested by CPs"


class PCPNameLast(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.32'

    @staticmethod
    def field_name():
        return 'PCP_Name_Last'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPNameFirst(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.33'

    @staticmethod
    def field_name():
        return 'PCP_Name_First'

    @staticmethod
    def size():
        return 100

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPNPI(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.34'

    @staticmethod
    def field_name():
        return 'PCP_NPI'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Requested by CPs"


class PCPAddressLineOne(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.35'

    @staticmethod
    def field_name():
        return 'PCP_Address_Line_1'

    @staticmethod
    def size():
        return 30

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPAddressLineTwo(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.36'

    @staticmethod
    def field_name():
        return 'PCP_Address_Line_2'

    @staticmethod
    def size():
        return 30

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPAddressCity(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.37'

    @staticmethod
    def field_name():
        return 'PCP_Address_City'

    @staticmethod
    def size():
        return 40

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPAddressState(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.38'

    @staticmethod
    def field_name():
        return 'PCP_Address_State'

    @staticmethod
    def size():
        return 2

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class PCPAddressZipCode(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.39'

    @staticmethod
    def field_name():
        return 'PCP_Address_ZipCode'

    @staticmethod
    def size():
        return 5

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Should include only first 5 digits of zipcode. **Required by ACO/MCO-CP Agreement"


class PCPPhoneNumber(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.40'

    @staticmethod
    def field_name():
        return 'PCP_Phone_Number'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "**Required by ACO/MCO-CP Agreement"


class DMHFlag(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.41'

    @staticmethod
    def field_name():
        return 'DMH_Flag'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['Y', 'N']

    @staticmethod
    def description():
        return "Indicator that member is affiliated with Department of Mental Health ***Requested by CPs"


class DDSFlag(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.42'

    @staticmethod
    def field_name():
        return 'DDS_Flag'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['Y', 'N']

    @staticmethod
    def description():
        return "Indicator that member is affiliated with Department of Developmental Services ***Requested by CPs"


class EOEAFlag(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.43'

    @staticmethod
    def field_name():
        return 'EOEA_Flag'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['Y', 'N']

    @staticmethod
    def description():
        return "Indicator that member is affiliated with Elder Affairs ***Requested by CPs"


class EDVisits(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.44'

    @staticmethod
    def field_name():
        return 'ED_Visits'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.NUMBER

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "# of Emergency Department Visits in Identification time period ***Requested by CPs"


class SNFDischarge(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.45'

    @staticmethod
    def field_name():
        return 'SNF_Discharge'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.OPTIONAL]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['Y', 'N']

    @staticmethod
    def description():
        return "Indicator that member has been discharged from a Skilled Nursing Facility in Identification time " \
               "period ***Requested by CPs"


class IdentificationFlag(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.46'

    @staticmethod
    def field_name():
        return 'Identification_Flag'

    @staticmethod
    def size():
        return 30

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['ACCS', 'Post-CBFS', 'Identified', 'Identified Relationship']

    @staticmethod
    def description():
        return "Indicator of reason for Identification and/or Assignment to CP. MassHealth will use this field to " \
               "identify if members are enrolled in ACCS, are post-CBFS, identified or have an identified " \
               "relationship.  ***Requested by CPs, ACOs, MCOs"


class RecordStatus(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.47'

    @staticmethod
    def field_name():
        return 'Record_Status'

    @staticmethod
    def size():
        return 1

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.TEXT

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return None

    @staticmethod
    def valid_values():
        return ['A', 'I']

    @staticmethod
    def description():
        return "Should be used to indicate when changes have led to a record becoming inactive. All records should " \
               "be \"A\" (Active) when MassHealth sends the list to ACO/MCO and CP."


class RecordUpdateDate(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.48'

    @staticmethod
    def field_name():
        return 'Record_Update_Date'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.DATE

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return "YYYYMMDD"

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Indicates date on which record was updated."


class ExportDate(CommunityPartnerField):
    @staticmethod
    def field_id():
        return '1.6.1.49'

    @staticmethod
    def field_name():
        return 'Export_Date'

    @staticmethod
    def size():
        return 10

    @staticmethod
    def required_or_locked():
        return [RequiredLockState.REQUIRED]

    @staticmethod
    def data_type():
        return DataType.DATE

    @staticmethod
    def end_user():
        return [OrgType.MASSHEALTH, OrgType.ACOMCO, OrgType.CP]

    @staticmethod
    def supplier():
        return [OrgType.MASSHEALTH]

    @staticmethod
    def format():
        return "YYYYMMDD"

    @staticmethod
    def valid_values():
        return None

    @staticmethod
    def description():
        return "Indicates \"export time\" or date table was created. Used in tracking data errors."
