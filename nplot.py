"""
@author Ryan Zaveruha
"""
import argparse
from serial.tools import list_ports
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import datetime
import time
import random


class Session():
    def __init__(self, sim, interval, batch, title=''):
        self.sim = sim
        self.batch = batch
        self.samples = []
        self.timeline = []
        self.title = title
        #styles = ['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight', 'seaborn-whitegrid', 'classic', '_classic_test', 'fast', 'seaborn-talk', 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale', 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn', 'Solarize_Light2', 'seaborn-paper', 'bmh', 'tableau-colorblind10', 'seaborn-white', 'dark_background', 'seaborn-poster', 'seaborn-deep']
        style.use('dark_background')
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1, 1, 1)
        self.ani = animation.FuncAnimation(
            self.fig, self.animate, interval=interval)
        plt.show()

    def animate(self, i):
        for _ in range(self.batch):
            results = self.sim.get_data()
            # self.x_samp = 
            # t = self.x_samp/1000
            self.timeline.append(results[1])  # Time is second result.
            row = []
            for sample in results[2:]:  # Rest of results are samples.
                row.append(sample)
            self.samples.append(row)

        self.ax1.clear()
        self.ax1.set_title(self.title, size=8)
        self.ax1.plot(self.timeline, self.samples)

        if results[0]:  # Stop is first result.
            self.ani._stop()
            return


class Sim():
    def __init__(self, title=''):
        self.title = title
        self.end = False
        self.x = 0
        self.y = 0
        self.z = 0
        self.time = 0

    def get_data(self):
        self.simulate()
        data = [self.x, self.y, self.z]
        result = [self.end,self.time] + data
        return result

    def simulate(self):
        self.x += random.random()
        self.y += random.random()
        self.z += random.random()
        self.time += 1
        if self.time > 20:
            self.end = True


def main():
    _ = Session(Sim(), 100, 1, title='Example')


if __name__ == "__main__":
    main()
