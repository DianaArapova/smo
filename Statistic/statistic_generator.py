import numpy as np


class StatisticAboutTrip:
    def __init__(self, id, statistic_by_single_people):
        print(f"Error {statistic_by_single_people}")
        self.statistic_by_single_people = sorted(statistic_by_single_people, key=lambda s: s.start_time)
        self.id = id
        self.min_quality = self.__get_min_of_quality__()
        self.avg_quality = self.__get_average_of_quality__()
        self.min_time = self.__get_min_of_time__()
        self.avg_time = self.__get_average_of_time__()
        self.total_trip_time = self.__get_total_trip_time__()
        self.total_route = self.__get_all_route__()
        self.weighted_avg_with_min_quality = self.__get_weighted_average_with_min_quality__()

    def __repr__(self):
        return f"id {self.id} min_quality {self.min_quality} avg_quality {self.avg_quality} min_time {self.min_quality}" \
            f"avg_time {self.avg_time} total_trip_time {self.total_trip_time} total_route {self.total_route}" \
            f"weighted_avg_with_min_quality {self.weighted_avg_with_min_quality}"

    def __get_min_of_quality__(self):
        qualities = []
        for s in self.statistic_by_single_people:
            qualities.append(s.quality_of_channel)

        return min(qualities)

    def __get_average_of_quality__(self):
        qualities = []
        for s in self.statistic_by_single_people:
            qualities.append(s.quality_of_channel)

        qualities = np.array(qualities)
        return np.average(qualities)

    def __get_min_of_time__(self):
        times = []
        for s in self.statistic_by_single_people:
            times.append(s.duration)

        return min(times)

    def __get_average_of_time__(self):
        times = []
        for s in self.statistic_by_single_people:
            times.append(s.duration)

        times = np.array(times)
        return np.average(times)

    def __get_time_on_min_quality_channel__(self):
        time_on_min_quality = 0
        for s in self.statistic_by_single_people:
            if s.quality_of_channel == self.min_quality:
                time_on_min_quality += s.duration

        return time_on_min_quality

    def __get_total_trip_time__(self):
        times = []
        for s in self.statistic_by_single_people:
            times.append(s.duration)

        times = np.array(times)
        return np.sum(times)

    def __get_all_route__(self):
        route = []

        for s in self.statistic_by_single_people:
            route.append(s.start_smo_id)
        route.append(self.statistic_by_single_people[-1].finish_smo_id)

        return route

    def __get_weighted_average_with_min_quality__(self):
        time_on_min_quality = self.__get_time_on_min_quality_channel__()
        total_time = self.__get_total_trip_time__()
        proportion_time = time_on_min_quality / total_time

        return self.avg_quality * (1 - proportion_time) + self.min_quality * proportion_time


class StatisticParameters:
    def __init__(self, people_id, parameter):
        self.people_id = people_id
        self.parameter = parameter


class StatisticProvider:
    def __init__(self, statistic):
        self.statistic = statistic
        self.extra_statistic = self.provide_statistics_by_all_people()

    def provide_statistics_by_all_people(self):
        statistics_by_people = dict()
        for s in self.statistic:
            if s.people_id in statistics_by_people:
                statistics_by_people[s.people_id].append(s.trip_info)
            else:
                statistics_by_people[s.people_id] = [s.trip_info]

        extra_statistics_by_people = list()
        for people_id in statistics_by_people:
            extra_statistics_by_people.append(StatisticAboutTrip(people_id, statistics_by_people[people_id]))

        return extra_statistics_by_people

    def get_for_all_people_min_quality(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.min_quality)

    def get_for_all_people_avg_quality(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.avg_quality)

    def get_for_all_people_min_time(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.min_time)

    def get_for_all_people_avg_time(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.avg_time)

    def get_for_all_people_weighted_avg_with_min_quality(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.weighted_avg_with_min_quality)

    def get_for_all_people_total_trip_time(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.total_trip_time)

    def get_for_all_people_total_routes(self):
        return self.__get_for_all_people_paramentrs_with_lambda__(lambda s: s.total_route)

    def __get_for_all_people_paramentrs_with_lambda__(self, what_parameter_is_useful):
        parametrs = []
        for s in self.extra_statistic:
            parametrs.append(StatisticParameters(s.id, what_parameter_is_useful(s)))
        return parametrs
