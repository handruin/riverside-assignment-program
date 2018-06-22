class Zipcode(object):
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

    @property
    def ap_priority(self):
        return self._ap_priority

    @ap_priority.setter
    def ap_priority(self, ap):
        self._ap_priority = ap

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
        if v:
            self.ap_priority = k

    @property
    def ap_nsmha(self):
        return self._ap_nsmha

    @ap_nsmha.setter
    def ap_nsmha(self, val):
        k, v = val['record']
        self._ap_nsmha = k
        if v:
            self.ap_priority = k

    @property
    def ap_edinburg(self):
        return self._ap_edinburg

    @ap_edinburg.setter
    def ap_edinburg(self, val):
        k, v = val['record']
        self._ap_edinburg = k
        if v:
            self.ap_priority = k

    @property
    def ap_riverside(self):
        return self._ap_riverside

    @ap_riverside.setter
    def ap_riverside(self, val):
        k, v = val['record']
        self._ap_riverside = k
        if v:
            self.ap_priority = k

    @property
    def ap_uphams(self):
        return self._ap_uphams

    @ap_uphams.setter
    def ap_uphams(self, val):
        k, v = val['record']
        self._ap_uphams = k
        if v:
            self.ap_priority = k

    @property
    def ap_dimock(self):
        return self._ap_dimock

    @ap_dimock.setter
    def ap_dimock(self, val):
        k, v = val['record']
        self._ap_dimock = k
        if v:
            self.ap_priority = k

    @property
    def ap_brookline(self):
        return self._ap_brookline

    @ap_brookline.setter
    def ap_brookline(self, val):
        k, v = val['record']
        self._ap_brookline = k
        if v:
            self.ap_priority = k
