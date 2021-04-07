class Customer:

    def __init__(self, customer_type, arrival_time, item_count):
        self.__customer_type = customer_type
        self.__arrival_time = arrival_time
        self.__item_count = item_count

    # using pythonic properties instead of traditional setters and getters.
    @property
    def customer_type(self):
        return self.__customer_type

    @property
    def arrival_time(self):
        return self.__arrival_time

    @property
    def item_count(self):
        return self.__item_count

    @item_count.setter
    def item_count(self, item_count):
        self.__item_count = item_count

    # overriding eq to compare two customer objects
    def __eq__(self, other):
        if isinstance(other, Customer):
            return self.customer_type == other.customer_type and self.arrival_time == other.arrival_time \
                   and self.item_count == other.item_count

        return False

    def __hash__(self):
        return hash((self.customer_type, self.arrival_time, self.item_count))

    # a helper function for debugging
    def print_customer_details(self):
        print("Customer Type : ", self.customer_type,"Customer Arrival Time : ", self.arrival_time,
              "Customer Item Count : ", self.item_count)
