import unittest

from Customer import Customer


class CustomerTest(unittest.TestCase):

    def test_customer_data(self):
        test_customer = Customer("A", 1, 2)

        expected_customer_type = "A"

        expected_arrival_time = 1

        expected_item_count = 2

        self.assertEqual(expected_customer_type, test_customer.customer_type, "Incorrect customer type")
        self.assertEqual(expected_arrival_time, test_customer.arrival_time, "Incorrect customer arrival time")
        self.assertEqual(expected_item_count, test_customer.item_count, "Incorrect item count")

        test_customer.item_count = 3
        expected_item_count = 3

        self.assertEqual(test_customer.item_count, expected_item_count, "Incorrect item count after setter call")
