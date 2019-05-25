from Individual.current_info_for_individual import CurrentInfoForIndividual


class Individual:
    def __init__(self, smo_routes_for_trip, t_for_starting_trip):
        self.smo_routes_for_trip = smo_routes_for_trip
        self.trip_info = [CurrentInfoForIndividual(0, t_for_starting_trip, -1, smo_routes_for_trip[0], 0)]

    def try_departure_to_next_smo(self, t_start, t_finish, quality_of_channel):
        if len(self.smo_routes_for_trip) == len(self.trip_info):
            return False

        next_smo = self.smo_routes_for_trip[len(self.trip_info) + 1]
        current_smo = self.smo_routes_for_trip[len(self.trip_info)]
        self.trip_info.append(
            CurrentInfoForIndividual(t_start, t_finish, current_smo, next_smo, quality_of_channel))
        return True

    def where_is_individual_now(self):
        return self.trip_info[-1].smo_finish
