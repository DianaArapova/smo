import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams


def save(name='', fmt='png'):
    pwd = os.getcwd()
    iPath = './{}'.format(fmt)
    if not os.path.exists(iPath):
        os.mkdir(iPath)
    os.chdir(iPath)
    plt.savefig('{}.{}'.format(name, fmt), fmt='png')
    os.chdir(pwd)
    #plt.close()

rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Arial'


class PlotsDrawer:
    def __init__(self, min_param, avg_param, weight_param, statistic):
        self.statistic = statistic
        self.weight_param = weight_param
        self.avg_param = avg_param
        self.min_param = min_param

    def draw_plot_for_each_people(self):
        ids = []
        weight_param = []
        for s in self.weight_param:
            ids.append(s.people_id)
            weight_param.append(s.parameter)
        avg_param = []
        for s in self.avg_param:
            avg_param.append(s.parameter)
        min_param = []
        for s in self.min_param:
            min_param.append(s.parameter)

        x = np.array(ids)
        y = np.array(weight_param)
        z = np.array(avg_param)
        r = np.array(min_param)

        # Способ 1 с помощью label
        plt.plot(x, y, label=u'weight_param', color='r')
        plt.plot(x, z, label=u'avg_param', color='g')
        plt.plot(x, r, label=u'min_param', color='b')

        plt.grid(True)
        plt.xlabel(u'People id')
        plt.ylabel(u'Quality')
        plt.title(u'Qualities')

        plt.legend()  # легенда для всего рисунка fig

        save('pic_12_1_4', fmt='png')

        plt.show()

    def draw_plot_for_each_route_average_min(self):
        route_and_min_quality = self.__get_min_quality_group_by_route__()

        routes = list()
        avg_min_quality = list()
        for route in route_and_min_quality:
            avg_min_quality.append(np.average(route_and_min_quality[route]))
            str_route = [str(r) for r in route]
            routes.append("-".join(str_route))

        x = np.array(routes)
        y = np.array(avg_min_quality)

        # Способ 1 с помощью label
        plt.plot(x, y, label=u'average of minimum qualities', color='r')

        plt.grid(True)
        plt.xlabel(u'Routes')
        plt.ylabel(u'Quality')
        plt.title(u'Qualities group by route')

        plt.legend()  # легенда для всего рисунка fig

        save('group_by_rote_min_1_1', fmt='png')

        plt.show()

    def draw_plot_for_each_route_count_of_people(self):
        route_and_min_quality = self.__get_min_quality_group_by_route__()

        routes = list()
        people_count = list()
        for route in route_and_min_quality:
            people_count.append(len(route_and_min_quality[route]))
            str_route = [str(r) for r in route]
            routes.append("-".join(str_route))

        x = np.array(routes)
        y = np.array(people_count)

        # Способ 1 с помощью label
        plt.plot(x, y, label=u'people per a route', color='b')

        plt.grid(True)
        plt.xlabel(u'Routes')
        plt.ylabel(u'Quality')
        plt.title(u'People count per route')

        plt.legend()  # легенда для всего рисунка fig

        save('group_by_route_count_of_people_1_1', fmt='png')

        plt.show()

    def __get_min_quality_group_by_route__(self):
        route_and_min_quality = dict()
        for s in self.statistic:
            if tuple(s.total_route) not in route_and_min_quality:
                route_and_min_quality[tuple(s.total_route)] = [s.min_quality]
            else:
                route_and_min_quality[tuple(s.total_route)].append(s.min_quality)

        for route in route_and_min_quality:
            route_and_min_quality[route] = np.array(route_and_min_quality[route])

        return route_and_min_quality
