from collections import deque

from CustomerType import CustomerType


class RegisterHelper:

    # using deque instead of lists for better runtimes for pop() and insert()
    @staticmethod
    def create_registers(register_count):
        registers = {}
        for i in range(1, register_count + 1):
            registers[i] = deque()
        return registers

    # In every dict, key = Register Number. Value = Deque()
    # Every Deque comprises of customer objects
    @staticmethod
    def add_customer_to_register(customer, registers):
        registers = dict(sorted(registers.items()))
        if customer.customer_type == CustomerType.A:

            RegisterHelper.add_customer_a_to_register(customer, registers)
        else:
            if customer.customer_type == CustomerType.B:
                RegisterHelper.add_customer_b_to_register(customer, registers)

    @staticmethod
    def add_customer_a_to_register(customer, registers):
        if len(registers) < 1:
            return 0
        min_idx = 1
        min_line_size = len(registers.get(min_idx))
        # key = index of register
        for idx, register in registers.items():
            if len(register) < min_line_size:
                min_line_size = len(register)
                min_idx = idx
        registers.get(min_idx).append(customer)
        return min_idx

    @staticmethod
    def add_customer_b_to_register(customer, registers):

        empty_register_idx = RegisterHelper.empty_registers_found(registers)

        if empty_register_idx != -1:
            registers.get(empty_register_idx).append(customer)
            return

        min_idx = 1
        min_item_count = registers.get(min_idx)[-1].item_count
        for idx, register in registers.items():
            if register[-1].item_count < min_item_count:
                min_idx = idx
                min_item_count = register[-1].item_count

        registers.get(min_idx).append(customer)
        return min_idx

    @staticmethod
    def empty_registers_found(registers):

        not_found = -1

        for idx, register in registers.items():
            if len(register) == 0:
                return idx

        return not_found
