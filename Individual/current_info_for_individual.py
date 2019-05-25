class CurrentInfoForIndividual:
    def __init__(self, start_trip_time, finish_trip_time, smo_start, smo_finish, quality_scale):
        self.quality_scale = quality_scale
        self.smo_finish = smo_finish
        self.smo_start = smo_start
        self.finish_trip_time = finish_trip_time
        self.start_trip_time = start_trip_time
        self.trip_time = finish_trip_time - start_trip_time
