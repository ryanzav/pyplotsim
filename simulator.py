"""
@author Ryan Zaveruha
"""
import random

import nplot


class Sim():
    def __init__(self, count, SpecialAgent, Agent):
        self.agents = [SpecialAgent()]
        for _ in range(count):
            self.agents.append(Agent())
        self.cycle = 0
        self.env = {}
        self.env['alive_count'] = 0

    def get_data(self):
        self.simulate()
        data = []
        alive_count = 0
        for agent in self.agents:
            data += agent.data()
            if not agent.dead:
                alive_count += 1
        self.env['alive_count'] = alive_count

        result = [self.env['alive_count'] == 0, self.cycle] + data
        return result

    def simulate(self):
        self.cycle += 1
        for agent in self.agents:
            if not agent.dead:
                self.env = agent.process(self.env)


class SpecialAgentEx():
    def __init__(self):
        self.position = 0
        self.dead = False

    def data(self):
        return [self.position]

    def process(self, env):
        self.position += random.choice([-1, 0, 1, 2])
        if self.position > 100:
            self.dead = True
        env['special_agent_position'] = self.position
        return env


class AgentEx():
    def __init__(self):
        self.position = 0
        self.dead = False

    def data(self):
        return [self.position]

    def process(self, env):
        self.position += random.choice([-1, 0, 1])
        if env['special_agent_position'] > 100:
            self.dead = True
        return env


def main():
    _ = nplot.Session(Sim(20, SpecialAgentEx, AgentEx), 1, 10, title='booboo')


if __name__ == "__main__":
    main()
