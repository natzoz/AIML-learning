from vacuum import *
import random

directions = ['north', 'east', 'south', 'west']
last_move = ''


def reflex_agent(is_dirty):
    if is_dirty:
        return 'clean'
    else:
        return 'west'


def random_agent(is_dirty):
    if is_dirty:
        return 'clean'
    else:
        return random.choice(directions)


def state_agent(is_dirty):
    global last_move
    if is_dirty:
        return 'clean'
    else:
        if last_move == '':
            last_move = random.choice(directions)
            return last_move
        elif last_move == 'west':
            last_move = random.choice(['north', 'west', 'south'])
            return last_move
        elif last_move == 'east':
            last_move = random.choice(['north', 'east', 'south'])
            return last_move
        elif last_move == 'south':
            last_move = random.choice(['south', 'east', 'west'])
            return last_move
        elif last_move == 'north':
            last_move = random.choice(['north', 'east', 'west'])
            return last_move


def state_agent_reset():
    global last_move
    last_move = ''


# run(20, 50000, reflex_agent)
# print(many_runs(20, 50000, 10, reflex_agent))
# run(20, 50000, random_agent)
# print(many_runs(20, 50000, 10, random_agent))
# run(20, 50000, state_agent, state_agent_reset)
# print(many_runs(20, 50000, 10, state_agent, state_agent_reset))
