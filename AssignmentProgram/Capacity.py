class Capacity(object):
    """
    Basic helper class that maps the capacities from the excel workbook into Capacity objects.  The capacity objects
    are typically referenced through a CapacityManager class instance.
    """
    def __init__(self, ap, capacity):
        self.ap = ap
        self.capacity = capacity

    def decrement_capacity(self):
        self.capacity -= 1


class CapacityManager(object):
    """
    Class used to manage one or more Capacity objects and offer helper functions for interacting with capacities.
    """
    def __init__(self, all_capacities):
        self.capacities = all_capacities

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


    def decrement_capacity_from_affiliate(self, affiliate):
        capacity_obj = self.get_capacity_by_affiliate(affiliate)
        if capacity_obj:
            capacity_obj.decrement_capacity()

