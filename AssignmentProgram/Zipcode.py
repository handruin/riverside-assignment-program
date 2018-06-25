class Zipcode(object):
    """
    Class used to represent Zipcodes defined in the Excel workbook.  An instance of a Zipcode will have helper method
    properties to act on the data defined within a Zipcode object.  A ZipcodeManager class instance is typically
    used for managing one or more Zipcode object throughout the processing.
    """
    def __init__(self, city_town, zipcode):
        self.city_town = city_town
        self._zipcode = None
        self.zipcode = str(zipcode).zfill(5)
        self._ap_lynn = None
        self._ap_nsmha = None
        self._ap_edinburg = None
        self._ap_riverside = None
        self._ap_uphams = None
        self._ap_dimock = None
        self._ap_brookline = None
        self._ap_priority = None
        self._all_available_aps = []

    @property
    def ap_priority(self):
        return self._ap_priority

    @ap_priority.setter
    def ap_priority(self, ap):
        self._ap_priority = ap

    @property
    def all_available_aps(self):
        # Moving the ap marked as priority to the first in the list
        if self._ap_priority:
            self._all_available_aps.insert(0, self._all_available_aps.pop(
                self._all_available_aps.index(self._ap_priority)))
        return self._all_available_aps

    @property
    def zipcode(self):
        return self._zipcode

    @zipcode.setter
    def zipcode(self, val):
        self._zipcode = val

    @property
    def ap_lynn(self):
        return self._ap_lynn

    @ap_lynn.setter
    def ap_lynn(self, val):
        k, v = val['record']
        self._ap_lynn = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_nsmha(self):
        return self._ap_nsmha

    @ap_nsmha.setter
    def ap_nsmha(self, val):
        k, v = val['record']
        self._ap_nsmha = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_edinburg(self):
        return self._ap_edinburg

    @ap_edinburg.setter
    def ap_edinburg(self, val):
        k, v = val['record']
        self._ap_edinburg = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_riverside(self):
        return self._ap_riverside

    @ap_riverside.setter
    def ap_riverside(self, val):
        k, v = val['record']
        self._ap_riverside = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_uphams(self):
        return self._ap_uphams

    @ap_uphams.setter
    def ap_uphams(self, val):
        k, v = val['record']
        self._ap_uphams = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_dimock(self):
        return self._ap_dimock

    @ap_dimock.setter
    def ap_dimock(self, val):
        k, v = val['record']
        self._ap_dimock = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k

    @property
    def ap_brookline(self):
        return self._ap_brookline

    @ap_brookline.setter
    def ap_brookline(self, val):
        k, v = val['record']
        self._ap_brookline = k
        if k:
            self._all_available_aps.append(k)
        if v:
            self.ap_priority = k


class ZipcodeManager(object):
    """
    Helper class used to manage one or more Zipcode objects.
    """
    def __init__(self, zipcodes):
        self._all_zipcodes = zipcodes

    def contains_zipcode(self, requested_zipcode):
        for zipcode in self._all_zipcodes:
            if zipcode.zipcode == requested_zipcode:
                return True
        return False

    def get_zipcode(self, requested_zipcode):
        for zipcode in self._all_zipcodes:
            if zipcode.zipcode == requested_zipcode:
                return zipcode
        return None

    def get_affiliates_from_zipcode(self, requested_zipcode):
        zipcode = self.get_zipcode(requested_zipcode)
        if zipcode:
            return zipcode.all_available_aps
        return []
