import unittest
from collections import deque

from CashierLineHelper import CashierLineHelper
from Customer import Customer


class CashierLineHelperTest(unittest.TestCase):
    test_customer_one = Customer("A", 1, 3)
    test_customer_two = Customer("B", 1, 2)
    customers_list_one = deque()
    customers_list_two = deque()
    registers = {}

    def setUp(self):
        self.customers_list_one.append(self.test_customer_one)
        self.customers_list_two.append(self.test_customer_two)
        self.registers = {1: self.customers_list_one, 2: self.customers_list_two}

    def test_reduce_item_count(self):
        test_customer_one = Customer("A", 1, 2)
        test_customer_two = Customer("B", 1, 1.5)
        self.customers_list_one.append(test_customer_one)
        self.customers_list_two.append(test_customer_two)
        expected_registers = {1: self.customers_list_one, 2: self.customers_list_two}
        time_diff = 1
        CashierLineHelper.reduce_item_count(self.registers, time_diff, 2)

        for key, value in self.registers.items():
            self.assertEqual(expected_registers[key], value, "Incorrectly reduced item count")

    def test_process_remaining_customer(self):
        self.registers = {1: self.customers_list_one, 2: self.customers_list_two}
        expected_value = 4
        self.assertEqual(expected_value, CashierLineHelper.process_remaining_customers(self.registers, 2),
                         "Incorrectly processed remaining customers")
