from Customer import Customer
from CustomerType import CustomerType


class ProcessData:

    @staticmethod
    def parse_input_file_data(filename):

        input_file_data = open(filename, "r")

        lines_data = input_file_data.readlines()

        try:
            register_count = int(lines_data.pop(0))
        except ValueError:
            print("Invalid data format")
            return

        customer_list = []

        for line in lines_data:
            customer_list.append(ProcessData.parse_customer_data(line))

        return register_count, customer_list

    @staticmethod
    def parse_customer_data(input_line):

        input_line_data = input_line.split()

        arrival_time = int(input_line_data[1])

        customer_type = input_line_data[0]

        item_count = int(input_line_data[2])

        if len(input_line_data) < 3:
            raise Exception("Invalid data")

        if customer_type != 'A' and customer_type != 'B':
            raise Exception("Invalid customer type")

        if arrival_time < 0:
            raise Exception("Invalid arrival time")

        if item_count < 0:
            raise Exception("Invalid item_count")

        if customer_type == "A":
            customer_type = CustomerType.A
        elif customer_type == "B":
            customer_type = CustomerType.B
        else:
            raise Exception("Invalid Customer type")

        customer = Customer(customer_type, arrival_time, item_count)

        return customer

    @staticmethod
    def check_valid_file(filename):

        try:
            open(filename, "r")
            return True

        except IOError:
            print("Error: File does not appear to exist.")
            return False
