import enum


class CustomerType(enum.Enum):
    A = "A"
    B = "B"

    def __lt__(self, other):
        if other == CustomerType.B:
            return True

        return False
