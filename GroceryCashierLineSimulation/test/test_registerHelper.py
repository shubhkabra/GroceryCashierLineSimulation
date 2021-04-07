import unittest
from collections import deque

from Customer import Customer
from RegisterHelper import RegisterHelper


class RegisterHelperTest(unittest.TestCase):

    def test_create_registers(self):
        customers_list_one = deque()
        customers_list_two = deque()
        expected_registers = {1: customers_list_one, 2: customers_list_two}

        output_registers = RegisterHelper.create_registers(2)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Incorrect registers generated")

    def test_add_customer_a_to_register(self):
        test_customer = Customer("A", 1, 2)
        customers_list_one = deque()
        customers_list_one.append(test_customer)
        customers_list_two = deque()
        expected_registers = {1: customers_list_one, 2: customers_list_two}

        output_registers = RegisterHelper.create_registers(2)
        RegisterHelper.add_customer_a_to_register(test_customer, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Customer A added to incorrect register")

        test_customer2 = Customer("A", 2, 3)
        expected_registers[2].append(test_customer2)
        RegisterHelper.add_customer_a_to_register(test_customer2, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Second Customer A added to incorrect register")

        test_customer3 = Customer("A", 3, 3)
        expected_registers[1].append(test_customer3)
        RegisterHelper.add_customer_a_to_register(test_customer3, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Third Customer A added to incorrect register")

    def test_add_customer_b_to_register(self):
        test_customer = Customer("B", 1, 3)
        customers_list_one = deque()
        customers_list_one.append(test_customer)
        customers_list_two = deque()
        expected_registers = {1: customers_list_one, 2: customers_list_two}

        output_registers = RegisterHelper.create_registers(2)
        RegisterHelper.add_customer_b_to_register(test_customer, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Customer B added to incorrect register")

        test_customer2 = Customer("B", 2, 3)
        expected_registers[2].append(test_customer2)
        RegisterHelper.add_customer_b_to_register(test_customer2, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Second Customer B added to incorrect register")

        test_customer3 = Customer("B", 3, 3)
        expected_registers[1].append(test_customer3)
        RegisterHelper.add_customer_b_to_register(test_customer3, output_registers)

        for key, value in output_registers.items():
            self.assertEqual(expected_registers[key], value, "Third Customer B added to incorrect register")

    def test_empty_registers_found(self):
        test_customer = Customer("B", 1, 3)
        customers_list_one = deque()
        customers_list_one.append(test_customer)
        customers_list_two = deque()

        expected_registers = {1: customers_list_one, 2: customers_list_two}
        expected_result = 2
        self.assertEqual(expected_result, RegisterHelper.empty_registers_found(expected_registers),
                         "Could not find empty registers")

        expected_registers[2].append(test_customer)
        expected_result = -1
        self.assertEqual(expected_result, RegisterHelper.empty_registers_found(expected_registers),
                         "No empty registers expected")
