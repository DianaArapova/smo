from Smo.smo_info import NewPeopleInfo


class TripInfo:
    def __init__(self, start_time, duration, capacity_of_channel, quality_of_channel, id_of_channel, start_smo_id, finish_smo_id):
        self.finish_smo_id = finish_smo_id
        self.start_smo_id = start_smo_id
        self.id_of_channel = id_of_channel
        self.quality_of_channel = quality_of_channel
        self.capacity_of_channel = capacity_of_channel
        self.duration = duration
        self.start_time = start_time

    def __repr__(self):
        return f"start_smo_id {self.start_smo_id} finish_smo_id {self.finish_smo_id} " \
            f"channel_id: {self.id_of_channel} with quality {self.quality_of_channel} and with capacity {self.capacity_of_channel} " \
            f"start_time {self.start_time} and duration {self.duration}"


class StatisticInfo:
    def __init__(self, people_id:int, trip_info:TripInfo):
        self.trip_info = trip_info
        self.people_id = people_id


class EdgeInSMO:
    def __init__(self, from_smo, to_smo, info_about_channels):
        self.from_smo = from_smo
        self.to_smo = to_smo
        self.info_about_channels = info_about_channels
        self.current_state_of_edge = []

    def make_new_iteration(self, t_start, t_finish):
        statistic_for_peoples_and_channels = []

        channels_info = []
        for channel in self.info_about_channels:
            movement_times = channel.get_times_for_starting_movement(t_start, t_finish)
            for movement_time in movement_times:
                start_time = movement_time[0]
                duration = movement_time[1]
                channels_info.append(TripInfo(start_time, duration,
                                              channel.capacity, channel.quality, channel.id,
                                              self.from_smo.id, self.to_smo.id))

        queue_of_channels = sorted(channels_info, key=lambda trip_info: trip_info.start_time)

        for channel_in_stop in queue_of_channels:
            peoples_in_channel = self.from_smo.queue_in_smo.get_first_people_from_queue(
                self.to_smo.id, channel_in_stop.capacity_of_channel, channel_in_stop.start_time)
            self.from_smo.take_away_people(peoples_in_channel)

            for people_id in peoples_in_channel:
                statistic_for_peoples_and_channels.append(StatisticInfo(people_id, channel_in_stop))

            self.to_smo.add_new_people(self.__make_list_of_info_about_new_peoples_in_smo__(
                peoples_in_channel, channel_in_stop.start_time + channel_in_stop.duration))

        return statistic_for_peoples_and_channels

    @staticmethod
    def __make_list_of_info_about_new_peoples_in_smo__(people_in_channel, arrival_time):
        new_people_info = []
        for people_id in people_in_channel:
            new_people_info.append(NewPeopleInfo(people_id, arrival_time))
        return new_people_info
