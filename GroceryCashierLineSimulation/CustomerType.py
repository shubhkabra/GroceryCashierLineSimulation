import enum


class CustomerType(enum.Enum):
    A = "A"
    B = "B"

    # overriding less than function in python, to help with sorting
    def __lt__(self, other):
        if other == CustomerType.B:
            return True

        return False
