#!/usr/bin/env python3

import re, time
from numpy import lcm

puzzle_input = """<x=17, y=-7, z=-11>
<x=1, y=4, z=-1>
<x=6, y=-2, z=-6>
<x=19, y=11, z=9>"""

puzzle_input = puzzle_input.split("\n")

class Moon:
    def __init__(self, id, x, y, z):
        self.id = id
        self.pos = (int(x), int(y), int(z))
        self.vel = (0, 0, 0)
    
    def calculate_increment(p1, p2):
        return -1 if p1 > p2 else 1 if p1 < p2 else 0
    
    def update_velocity(self, other_moons):
        # Geschwindigkeit in Abhängigkeit anderer Monde bestimmen
        #print("Updating", self.id, "with", [other.id for other in other_moons])
        for other in other_moons:
            px, py, pz = self.pos
            vx, vy, vz = self.vel
            
            vx += Moon.calculate_increment(px, other.pos[0])
            vy += Moon.calculate_increment(py, other.pos[1])
            vz += Moon.calculate_increment(pz, other.pos[2])
            self.vel = (vx, vy, vz)
        
    
    def update_position(self):
        # Position mit aktueller Geschwindigkeit neu berechnen
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1], self.pos[2] + self.vel[2])
    
    def e_pot(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
    
    def e_kin(self):
        return abs(self.vel[0]) + abs(self.vel[1]) + abs(self.vel[2])


def get_moons(definition):
    moons = []
    for id, scanned_position in enumerate(definition):
        scanned_position = [id] + [re.search("=(-?\d+)", param)[1] for param in scanned_position.split(",")]
        moons.append(Moon(*scanned_position))
    
    return moons


period_length = [0]*3
count = 0
hist = {}
current_dimension = 0
moons = get_moons(puzzle_input)
while True:
    
    # Part 1
#     if count == 1000:
#         total_energy = sum([moon.e_pot()*moon.e_kin() for moon in moons])
#         print("# Part 1: Energy:", [[moon.e_pot(), moon.e_kin(), moon.e_pot()*moon.e_kin()] for moon in moons])
#         print("# Part 1: Total energy:", total_energy)
#         break

    # Part 2
    current_state = ""
    for moon in moons:
        current_state += str(moon.pos[current_dimension]) + "," + str(moon.vel[current_dimension]) + ","
    
    # Repeated pattern in current dimension found
    if current_state in hist:
        print("Period length =", count, "for dimension", current_dimension)
        period_length[current_dimension] = count
        
        # Reset
        count = 0
        hist = {}
        current_dimension += 1
        moons = get_moons(puzzle_input)
        
        if current_dimension > 2:
            print("# Part 2: KgV:", lcm(lcm(period_length[0], period_length[1]), period_length[2]))
            break
        
        continue # Restart cycle
    else:
        hist[current_state] = 1
    
    # Part 1+2
    initial_moon_state = moons[:]
    for moon in moons:
        # Update this moon with a unmodified copy of all others        
        moon.update_velocity([other_moon for other_moon in initial_moon_state if other_moon.id != moon.id])
    
    for moon in moons:
        # Update positions
        moon.update_position()
    
    count += 1
    if count % 100000 == 0:
        print(time.strftime("%H:%M:%S:"), count, "tried for dimension", current_dimension)
