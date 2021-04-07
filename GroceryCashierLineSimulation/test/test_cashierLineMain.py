import unittest

from CashierLineMain import CashierLineMain


class CashierLineMainTest(unittest.TestCase):

    def test_two_registers(self):
        file_name = "testFiles/two_registers.txt"

        expected_value = 13

        output_value = CashierLineMain.calculate_time(file_name)

        self.assertEqual(expected_value, output_value, "Two Registers test case failed")

    def test_departing_customers(self):
        file_name = "testFiles/departing_customers.txt"

        expected_value = 6

        output_value = CashierLineMain.calculate_time(file_name)

        self.assertEqual(expected_value, output_value, "Departing customers are not counted in line")

    def test_type_a_before_b(self):
        file_name = "testFiles/type_a_before_b.txt"

        expected_value = 11

        output_value = CashierLineMain.calculate_time(file_name)

        self.assertEqual(expected_value, output_value, "Type A Customers are not chosen before type B")

    def test_customer_with_fewer_items(self):
        file_name = "testFiles/customer_with_fewer_items.txt"

        expected_value = 9

        output_value = CashierLineMain.calculate_time(file_name)

        self.assertEqual(expected_value, output_value, "customers with fewer items don't choose lines sooner")

    def test_no_customer(self):
        file_name = "testFiles/no_customer.txt"

        expected_value = 0

        output_value = CashierLineMain.calculate_time(file_name)

        self.assertEqual(expected_value, output_value, "Incorrect value for no customers")

    def test_invalid_input_data(self):
        file_name = "testFiles/invalid_input_data.txt"

        with self.assertRaises(Exception):
            CashierLineMain.calculate_time(file_name, "Not accounting for invalid data")
