"""
@author Ryan Zaveruha
"""
import nplot
import random 
import simulator

class SpecialAgent():
    def __init__(self):
        self.position = 0    
        self.dead = False
    
    def data(self):
        return([self.position])

    def process(self, env):
        self.position += random.choice([-1,0,1,2,4]) 
        if env['alive_count'] == 1:
            self.dead = True
        env['special_agent_position'] = self.position
        return env

FEAR = 10
MAX_FEAR = 100
BASE_SPEED = 6
BASE_BOREDOM = 4
BASE_POSITION = 50
class Agent():
    def __init__(self):
        self.position = BASE_POSITION + random.random()*200
        self.fear = 0
        self.bored = 0
        self.action = ''
        self.dead = False
        self.speed = BASE_SPEED * (1 + random.random())
        self.max_strength = self.speed  * (1 + random.random())
        self.base_strength = self.max_strength 
        self.strength = self.base_strength
        self.bored_limit = BASE_BOREDOM * (1 + random.random())

    def data(self):
        return[self.position] #,self.strength]

    def process(self,env):
        bear_position = env['special_agent_position']
        self.action = 'Chill.'
        if self.dead:
            self.action = 'Dead.'
        elif (self.position - bear_position) < 1:
            self.action = 'Die!'
        elif (self.position - bear_position) < 5:
            self.action = 'Run!'
            self.fear += FEAR
            if self.fear > MAX_FEAR:
                self.fear = MAX_FEAR
        elif self.fear > 0:
            self.action = random.choice(['Run!','Chill.','Chill.'])
        elif self.bored > self.bored_limit:
            self.action = 'Explore!'    
        
        if self.action == 'Run!':
            self.position += self.run()   
        if self.action == 'Die!':     
            self.die()       
        if self.action == 'Chill.':     
            self.chill()          
        if self.action == 'Explore!':
            self.position += self.explore()  
        #print(self.action)
        return env

    def die(self):
        self.dead = True
        self.strength = 0
        self.fear = 0
        self.position = 0
        print('Strength: {} Speed: {}'.format(self.max_strength,self.speed))

    def run(self):
        self.bored = 0
        if self.strength >= self.speed:
            self.strength -= self.speed
            self.fear -= 1
            return(self.speed)
        else:
            self.max_strength -= 1
            if self.max_strength < 0:
                self.max_strength = 0
            self.strength += 1
            return(0)
    
    def chill(self):
        self.bored +=1
        self.max_strength += 1
        if self.max_strength > self.base_strength:
            self.max_strength = self.base_strength
        self.strength += 2
        if self.strength > self.max_strength:
            self.strength = self.max_strength
        self.fear -= 1
        if self.fear < 0:
            self.fear = 0
        
    def explore(self):
        self.bored = 0
        return random.choice(range(-10,10,1))

def main():
    _ = nplot.Session(simulator.Sim(1000,SpecialAgent,Agent),1,100,title='booboo')


if __name__ == "__main__":
    main()
