import unittest

from Customer import Customer
from CustomerType import CustomerType
from ProcessData import ProcessData


class ProcessDataTest(unittest.TestCase):

    def test_valid_file(self):
        file_name_1 = "testFiles/departing_customers.txt"
        self.assertTrue(ProcessData.check_valid_file(file_name_1), "Valid File Test Failed")

    def test_parse_customer_data(self):
        valid_customer_data = "A 2 1"
        invalid_customer_type = "C 2 3"
        invalid_customer_arrival_time = "A -1 2"
        invalid_customer_item_count = "A 1 -1"
        invalid_customer_data = "A 1"
        expected_customer = Customer(CustomerType.A, 2, 1)
        result_customer = ProcessData.parse_customer_data(valid_customer_data)
        self.assertEqual(expected_customer, result_customer,
                         "Incorrect customer data parsing")
        with self.assertRaises(Exception):
            ProcessData.parse_customer_data(invalid_customer_type, "Invalid Customer Type test failed")

        with self.assertRaises(Exception):
            ProcessData.parse_customer_data(invalid_customer_arrival_time, "Invalid Customer Arrival Time test failed")

        with self.assertRaises(Exception):
            ProcessData.parse_customer_data(invalid_customer_item_count, "Invalid Customer Item Count test failed")

        with self.assertRaises(Exception):
            ProcessData.parse_customer_data(invalid_customer_data, "Invalid Customer data test failed")

    def test_parse_input_file_data(self):
        test_customer_1 = Customer(CustomerType.A, 1, 3)
        test_customer_2 = Customer(CustomerType.A, 1, 5)

        file_name_1 = "testFiles/sample_input_valid_file.txt"
        file_name_2 = "testFiles/sample_input_file_without_register_count.txt"

        expected_customer_list = [test_customer_1, test_customer_2]

        expected_register_count = 2

        output_register_count, output_customer_list = ProcessData.parse_input_file_data(file_name_1)

        self.assertEqual(expected_register_count, output_register_count, "Incorrect register count")

        for i in range(len(output_customer_list)):
            self.assertEqual(expected_customer_list[i], output_customer_list[i], "Incorrect customer list")

        with self.assertRaises(Exception):
            ProcessData.parse_input_file_data(file_name_2, "Does not raise exception for missing register count")
