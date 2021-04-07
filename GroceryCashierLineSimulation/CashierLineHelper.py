class CashierLineHelper:

    # reducing item count according to the time diff and cashier type
    @staticmethod
    def reduce_item_count(registers, time_diff, register_count):

        for idx, register in registers.items():

            for i in range(time_diff):

                if len(register) > 0:

                    if idx == register_count:
                        register[0].item_count -= 0.5

                    else:
                        register[0].item_count -= 1

                    if register[0].item_count <= 0:
                        register.popleft()

    # once there are no more customers left to be addded to the cashier lines, calculating
    # the max_time required to finish all check outs
    @staticmethod
    def process_remaining_customers(registers, register_count):

        max_time = 0

        for idx, register in registers.items():

            if idx == register_count:
                trainee_register = True
            else:
                trainee_register = False

            time_required = 0

            while len(register) > 0:

                temp_time = register.popleft().item_count

                if trainee_register:
                    temp_time *= 2

                time_required += temp_time

            max_time = max(max_time, time_required)

        return max_time
