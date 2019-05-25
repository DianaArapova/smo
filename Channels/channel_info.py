import random


class ChannelInfo:
    def __init__(self, capacity, quality, id, waiting_time,
                 start_of_movement, average_time_for_route, time_deviation_for_route):
        self.time_deviation_for_route = time_deviation_for_route
        self.average_time_for_route = average_time_for_route
        self.waiting_time = waiting_time
        self.id = id
        self.quality = quality
        self.capacity = capacity
        self.is_arrived = False
        self.start_of_movement = start_of_movement
        self.arrived_time = start_of_movement
        self.trip_times = []

    def get_times_for_starting_movement(self, t_start, t_finish):
        current_time = self.start_of_movement
        times_for_starting_movements = []

        for i in range(len(self.trip_times)):
            trip_time = self.trip_times[i]
            if self.is_in_between_start_and_finish(current_time, t_start, t_finish):
                times_for_starting_movements.append((current_time, trip_time))
            current_time += trip_time
            current_time += self.waiting_time

        while current_time <= t_finish:
            trip_time = self.get_time_for_trip()
            if self.is_in_between_start_and_finish(current_time, t_start, t_finish):
                self.trip_times.append(trip_time)
                times_for_starting_movements.append((current_time, trip_time))

            current_time += trip_time
            current_time += self.waiting_time

        return times_for_starting_movements

    @staticmethod
    def is_in_between_start_and_finish(t, t_start, t_finish):
        return t_start <= t <= t_finish

    def get_time_for_trip(self):
        return random.gauss(self.average_time_for_route, self.time_deviation_for_route)
