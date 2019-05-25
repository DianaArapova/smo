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
    def __init__(self, min_param, avg_param, weight_param):
        self.weight_param = weight_param
        self.avg_param = avg_param
        self.min_param = min_param

    def draw_plot(self):
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
