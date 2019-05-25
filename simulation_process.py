class SimulationProcess:
    def __init__(self, smos:list, graph_of_smo:list, count_of_iteration=10):
        self.count_of_iteration = count_of_iteration
        self.smos = smos
        self.graph_of_smo = graph_of_smo

    def simulate(self, start_time, finish_time):
        time_internals = self.__get_time_intervals__(start_time, finish_time)
        all_statistic = []

        for interval in time_internals:
            print(interval)
            start_time_interval = interval[0]
            finish_time_interval = interval[1]
            for smo in self.smos:
                #todo: scecify max_people count depending on loading on road
                smo.generate_peoples_desires(start_time_interval, finish_time_interval)

            for edge in self.graph_of_smo:
                statistic = edge.make_new_iteration(start_time_interval, finish_time_interval)
                for s in statistic:
                    all_statistic.append(s)

        return all_statistic

    def _get_step_count(self, start_time, finish_time):
        return (finish_time - start_time) // self.count_of_iteration

    def __get_time_intervals__(self, start_time, finish_time):
        time_interval = self._get_step_count(start_time, finish_time)
        time_intervals = []

        for current_time in range(start_time, finish_time, time_interval):
            if current_time + time_interval < finish_time:
                time_intervals.append((current_time, current_time + time_interval))
            else:
                time_intervals.append((current_time, finish_time))
                return time_intervals
        return time_intervals
