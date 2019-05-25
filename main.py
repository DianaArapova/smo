import random

from Channels.channel_info import ChannelInfo
from Smo.edge_in_smo import EdgeInSMO
from Statistic.plots_drawer import PlotsDrawer
from simulation_process import SimulationProcess
from Smo.smo_info import SMO, NewPeopleInfo
from Statistic.statistic_generator import StatisticProvider


def add_info_to_smo_about_neighbours(graph_of_smo):
    for edge in graph_of_smo:
        edge.from_smo.add_info_about_smo_neighbour(edge.to_smo.id)


def main():
    smo = [
        SMO(1, [NewPeopleInfo(i, 0) for i in range(15)], False, 1024),
        SMO(2, [NewPeopleInfo(i, 0) for i in range(15, 20)], False, 1025),
        SMO(3, [NewPeopleInfo(i, 0) for i in range(20, 25)], True, 1026),
        SMO(4, [NewPeopleInfo(i, 0) for i in range(25, 40)], False, 1027)
    ]
    graph_of_smo = [
        EdgeInSMO(
            from_smo=smo[0],
            to_smo=smo[1],
            info_about_channels=[
                ChannelInfo(capacity=5, quality=2, id=1, waiting_time=1, start_of_movement=0,
                            average_time_for_route=15, time_deviation_for_route=2),
                ChannelInfo(capacity=5, quality=3, id=2, waiting_time=1, start_of_movement=0,
                            average_time_for_route=5, time_deviation_for_route=2),
                ChannelInfo(capacity=5, quality=1, id=3, waiting_time=1, start_of_movement=0,
                            average_time_for_route=12, time_deviation_for_route=2)]),
        EdgeInSMO(
            from_smo=smo[1],
            to_smo=smo[2],
            info_about_channels=[ChannelInfo(capacity=5, quality=4, id=4, waiting_time=1, start_of_movement=0,
                                             average_time_for_route=11, time_deviation_for_route=2)]),
        EdgeInSMO(
            from_smo=smo[0],
            to_smo=smo[2],
            info_about_channels=[
                ChannelInfo(capacity=5, quality=1, id=5, waiting_time=1, start_of_movement=0,
                            average_time_for_route=15, time_deviation_for_route=2),
                ChannelInfo(capacity=5, quality=5, id=6, waiting_time=1, start_of_movement=0,
                            average_time_for_route=4, time_deviation_for_route=2)]),
        EdgeInSMO(
            from_smo=smo[0],
            to_smo=smo[3],
            info_about_channels=[
                ChannelInfo(capacity=5, quality=3, id=7, waiting_time=1, start_of_movement=0,
                            average_time_for_route=15, time_deviation_for_route=2),
                ChannelInfo(capacity=5, quality=4, id=8, waiting_time=1, start_of_movement=0,
                            average_time_for_route=12, time_deviation_for_route=2)]),
        EdgeInSMO(
            from_smo=smo[3],
            to_smo=smo[0],
            info_about_channels=[ChannelInfo(capacity=5, quality=1, id=9, waiting_time=1, start_of_movement=0,
                                             average_time_for_route=20, time_deviation_for_route=2)])
    ]
    add_info_to_smo_about_neighbours(graph_of_smo)

    random.seed(1000)
    process = SimulationProcess(smo, graph_of_smo)
    data_for_statistic = process.simulate(0, 100)
    data_for_statistic = sorted(data_for_statistic, key=lambda s: s.people_id)

    statistic_provider = StatisticProvider(data_for_statistic)

    for s in statistic_provider.provide_statistics_by_all_people():
        print(s)

    min_quality_parameters = statistic_provider.get_for_all_people_min_quality()
    avg_quality_parameters = statistic_provider.get_for_all_people_avg_quality()
    wight_quality_parameters = statistic_provider.get_for_all_people_weighted_avg_with_min_quality()

    plot_drawer = PlotsDrawer(min_quality_parameters, avg_quality_parameters, wight_quality_parameters)
    plot_drawer.draw_plot()

    for s in data_for_statistic:
        print(s.people_id, s.trip_info)


if __name__ == "__main__":
    main()







