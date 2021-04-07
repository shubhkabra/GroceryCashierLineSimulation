import sys

from CashierLineHelper import CashierLineHelper
from ProcessData import ProcessData
from RegisterHelper import RegisterHelper


class CashierLineMain:

    @staticmethod
    def main():
        filename = sys.argv[1]
        if not ProcessData.check_valid_file(filename):
            return
        else:
            print("t =", CashierLineMain.calculate_time(filename), "minutes")

    @staticmethod
    def calculate_time(filename):

        total_time = 0

        register_count, pre_sorted_customer_list = ProcessData.parse_input_file_data(filename)

        # sorting the customer_list based on arrival_time, item_count and customer_type in that order respectively.

        customer_list = sorted(pre_sorted_customer_list, key=lambda customer:
                    (customer.arrival_time, customer.item_count, customer.customer_type))

        # customer_list accounts for customers that need to be added to the cashier lines

        prev_time = 0

        registers = RegisterHelper.create_registers(register_count)

        for customer in customer_list:
            curr_time = customer.arrival_time

            time_diff = curr_time - prev_time

            CashierLineHelper.reduce_item_count(registers, time_diff, register_count)

            RegisterHelper.add_customer_to_register(customer, registers)

            prev_time = curr_time

            total_time += time_diff

        total_time += CashierLineHelper.process_remaining_customers(registers, register_count)

        return int(total_time)
