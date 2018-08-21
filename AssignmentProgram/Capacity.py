import logging


class Capacity(object):
    """
    Basic helper class that maps the capacities from the excel workbook into Capacity objects.  The capacity objects
    are typically referenced through a CapacityManager class instance.
    """
    def __init__(self, ap, capacity):
        self.ap = ap
        self.capacity_available = capacity
        self.capacity = capacity

    def decrement_capacity(self):
        self.capacity -= 1

    def available_capacity_percentage(self):
        return (self.capacity / self.capacity_available) * 100


class CapacityManager(object):
    """
    Class used to manage one or more Capacity objects and offer helper functions for interacting with capacities.
    """
    def __init__(self, all_capacities):
        self.capacities = all_capacities
        self.logger = logging.getLogger(__name__)

    def get_capacity_size_of_affiliate(self, affiliate):
        for capacity in self.capacities:
            if capacity.ap == affiliate:
                return capacity.capacity

    def does_affiliate_have_capacity(self, affiliate_name):
        capacity_obj = self.get_capacity_by_affiliate(affiliate_name)
        if capacity_obj:
            return capacity_obj.capacity > 0
        return False

    def get_capacity_by_affiliate(self, affiliate):
        for capacity in self.capacities:
            if capacity.ap == affiliate:
                return capacity

    def get_highest_capacity_by_affiliates(self, affiliates):
        capacities = []
        for ap in affiliates:
            capacities.append(self.get_capacity_by_affiliate(ap))
        highest_capacities = sorted(capacities, key=lambda x: x.capacity, reverse=True)
        if highest_capacities:
            return highest_capacities[0]
        return None

    def get_highest_capacity_percentage_by_affiliates(self, affiliates):
        capacities = []
        for ap in affiliates:
            capacities.append(self.get_capacity_by_affiliate(ap))

        for cap in capacities:
            self.logger.debug("Capacity of {0} is {1}.".format(cap.ap, cap.available_capacity_percentage()))
        highest_capacities = sorted(capacities, key=lambda x: x.available_capacity_percentage(), reverse=True)
        if highest_capacities:
            self.logger.debug("Returning the highest capacity ap: {0}".format(highest_capacities[0].ap))
            return highest_capacities[0]
        return None

    def decrement_capacity_from_affiliate(self, affiliate):
        capacity_obj = self.get_capacity_by_affiliate(affiliate)
        if capacity_obj:
            capacity_obj.decrement_capacity()
