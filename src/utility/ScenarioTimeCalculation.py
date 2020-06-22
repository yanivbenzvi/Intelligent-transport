from src.utility.SimulationInformationReader import SimulationInformationReader


class ScenarioTimeCalculation:
    def __init__(self, scenario, interval_length):
        self.scenario = scenario
        self.start_end_point = None
        self.start_end_point = self.scenario_start_end_tuple()
        self.interval_length = interval_length

    def scenario_start_end_tuple(self):
        if not self.start_end_point:
            self.start_end_point = SimulationInformationReader.extract_time(self.scenario.path_to_scenario_conf())
        return self.start_end_point

    def scenario_start_time(self):
        return self.scenario_start_end_tuple()[0]

    def scenario_end_time(self):
        return self.scenario_start_end_tuple()[1]

    def scenario_duration(self):
        return (float(self.scenario_end_time()) - float(self.scenario_start_time())) / 3600

    def get_num_of_interval(self):
        """
        :param duration: simulation duration (finish time - start time)
        :param interval_length: 2 hours per one cell
        :return: num of the interval in scenario simulation
        """
        num_of_cells = self.scenario_duration() / self.interval_length
        if num_of_cells.is_integer():
            return int(num_of_cells)
        else:
            return int(num_of_cells + 1)

    def get_current_interval(self, current_time):
        """
        :param num_of_cells:num of total cells
        :param current_time: specific time
        :param interval_length: interval length (2)
        :return: cell location to specific time (calc_time)
        """
        current_time = ScenarioTimeCalculation.get_real_time(current_time)[0]
        count = 0
        current_bound = ScenarioTimeCalculation.get_real_time(self.start_end_point[0])[0] + self.interval_length

        while current_time >= current_bound:
            current_bound += self.interval_length
            count += 1

        if self.get_num_of_interval() < count:
            count = -1
        print("current_interval: ", count)
        return count

    @staticmethod
    def get_real_time(time):
        """
        :param time:simulation time
        :return:real time in tuple
        """
        time = int(time)
        hours = time / 3600
        minutes = (hours * 60) % 60
        seconds = (minutes * 60) % 60
        tuple_date = (int(hours), int(minutes), int(seconds))
        # tuple_date = (round(hours), round(minutes), round(seconds))
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

    def get_next_interval(self, current_interval):
        if self.get_num_of_interval() == current_interval:
            return -1
        return current_interval + 1

    def is_the_next_interval_near(self, current_time, delta):
        current_interval = self.get_current_interval(current_time)
        next_interval = self.get_next_interval(current_interval)
        delta_interval = self.get_current_interval(current_time + delta)

        return delta_interval >= next_interval






if __name__ == "__main__":
    print("Check if next interval cell: --> 1. no 2. yes")
    printed1 = ScenarioTimeCalculation.check_is_next_interval_cell(2, 0.5, 0.5)
    printed2 = ScenarioTimeCalculation.check_is_next_interval_cell(2, 1.8, 0.5)
    print("1.-> Empty--> ", printed1)
    print("2.-> Update to next phase --> ", printed2)
    print("-----------------------------------------------------")
    print("get_real_time-> 14400 = 04:00:00 --> (4,0,0) ")
    print(ScenarioTimeCalculation.get_real_time(14400))
    print("get_real_time-> 19900 = 06:32:40 --> (6,32,40) ")
    print(ScenarioTimeCalculation.get_real_time(19900)[0])
    print(ScenarioTimeCalculation.get_real_time(19900)[1])
    print(ScenarioTimeCalculation.get_real_time(19900)[2])
    print("-----------------------------------------------------")
    print("Real Time 19000 --> 5 ", ScenarioTimeCalculation.get_real_time(time=19000)[0])
    print("get_num_of_cells: TimeFunction.get_num_of_cells(14, 2)--> 7")
    print(ScenarioTimeCalculation.get_num_of_interval(14, 2))
    print("TimeFunction.get_num_of_cells(11, 2) --> 6")
    print(ScenarioTimeCalculation.get_num_of_interval(11, 2))
    print("-----------------------------------------------------")
    print("TimeFunction.get_cells_number(6, 4, 2) --> 2")
