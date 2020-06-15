from src.utility.Simluationinformationreader import SimulationInformationReader


class TimeFunction:

    def scenario_start_end_tuple(self):
        if not self.start_end_point:
            self.start_end_point = SimulationInformationReader.extract_time(self.path_to_scenario_conf())
        return self.start_end_point

    def scenario_start_time(self):
        return self.scenario_start_end_tuple()[0]

    def scenario_end_time(self):
        return self.scenario_start_end_tuple()[1]

    def scenario_duration(self):
        return (float(self.scenario_end_time()) - float(self.scenario_start_time())) / 3600

    @staticmethod
    def get_num_of_cells(duration, interval_length):
        """
        :param duration: simulation duration (finish time - start time)
        :param interval_length: 2 hours per one cell
        :return:num of cells this simulation
        """
        num_of_cells = duration / interval_length
        if num_of_cells.is_integer():
            return int(num_of_cells)
        else:
            return int(num_of_cells + 1)

    @staticmethod
    def get_cells_number(num_of_cells, calc_time, interval_length):
        """
        :param num_of_cells:num of total cells
        :param calc_time: specific time
        :param interval_length: interval length (2)
        :return: cell location to specific time (calc_time)
        """
        count = 0
        start = interval_length
        if start >= calc_time:
            return count
        while start <= calc_time:
            start += interval_length
            count += 1
        if num_of_cells < count:
            count = -1
        return count

    @staticmethod
    def get_real_time(time):
        """
        :param time:simulation time
        :return:real time in tuple
        """
        hours = int(time)
        hours = time / 3600
        minutes = (hours * 60) % 60
        seconds = (minutes * 60) % 60
        tuple_date = (round(hours), round(minutes), round(seconds))
        return tuple_date

    @staticmethod
    def check_is_next_interval_cell(next_interval_step, current_time, delta):
        """
        :param next_interval_step: time now + step
        :param current_time: time now
        :param delta: minimum time between cells
        :return:update or empty string
        """
        outPut = ""
        if next_interval_step - current_time <= delta:
            outPut = "Update to next phase"
        return outPut


if __name__ == "__main__":
    print("Check if next interval cell: ->1. no 2. yes")
    printed1 = TimeFunction.check_is_next_interval_cell(2, 0.5, 0.5)
    printed2 = TimeFunction.check_is_next_interval_cell(2, 1.8, 0.5)
    print("1.-> Empty-> ", printed1)
    print("2.-> Update to next phase -> ", printed2)
    print("-----------------------------------------------------")
    print("get_real_time-> 4:00:00 (4,0,0) ")
    print(TimeFunction.get_real_time(14400))
    print("-----------------------------------------------------")
    print("get_num_of_cells: TimeFunction.get_num_of_cells(14, 2)-> 7")
    print(TimeFunction.get_num_of_cells(14, 2))
    print("TimeFunction.get_num_of_cells(11, 2)-> 6")
    print(TimeFunction.get_num_of_cells(11, 2))
    print("-----------------------------------------------------")
    print("TimeFunction.get_cells_number(6, 4, 2)-> 2")
    print(TimeFunction.get_cells_number(6, 4, 2))
