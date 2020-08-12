# pyplotsim
Utility for creating updating plots with matplotlib. Utility for simulating any number of agents and a special agent. Example simulation.

Output of booboo.py. Simulates a bear (SpecialAgent) hunting prey (Agents).

[example]: example.png "example"

![alt text][example]


### Contents
nplot.py: Plotting utility.

simulator.py: Simulation utility.

booboo.py: Example simulation.

```
cycles = 1000
interval = 1
batch = 100
title = 'Example'
_ = nplot.Session(simulator.Sim(cycles, SpecialAgent, Agent), interval, batch, title=title)
```
