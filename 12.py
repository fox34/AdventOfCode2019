#!/usr/bin/env python3

import copy, re, time

puzzle_input = """<x=17, y=-7, z=-11>
<x=1, y=4, z=-1>
<x=6, y=-2, z=-6>
<x=19, y=11, z=9>"""

puzzle_input = """<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>"""

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
    

# Part 1
moons = []
for id, scanned_position in enumerate(puzzle_input):
    scanned_position = [id] + [re.search("=(-?\d+)", param)[1] for param in scanned_position.split(",")]
    moons.append(Moon(*scanned_position))

for step in range(1000):
    
    initial_moon_state = [copy.copy(moon) for moon in moons]
    for moon in moons:
        # Update this moon with a unmodified copy of all others        
        moon.update_velocity([other_moon for other_moon in initial_moon_state if other_moon.id != moon.id])
    
    for moon in moons:
        # Update positions
        moon.update_position()
    
    
total_energy = sum([moon.e_pot()*moon.e_kin() for moon in moons])
print("Energy:", [[moon.e_pot(), moon.e_kin(), moon.e_pot()*moon.e_kin()] for moon in moons])
print("Total energy:", total_energy)


# Part 2 ?????
# moons = []
# for id, scanned_position in enumerate(puzzle_input):
#     scanned_position = [id] + [re.search("=(-?\d+)", param)[1] for param in scanned_position.split(",")]
#     moons.append(Moon(*scanned_position))
# 
# count = 0
# historical_states = []
# while True:
#     
#     current_state = ()
#     for moon in moons:
#         current_state = current_state + moon.pos + moon.vel
# 
#     if current_state in historical_states:
#         print(count, "Steps for previous state")
#         break
#     
#     historical_states.append(current_state)
#     
#     initial_moon_state = [copy.copy(moon) for moon in moons]
#     for moon in moons:
#         # Update this moon with a unmodified copy of all others        
#         moon.update_velocity([other_moon for other_moon in initial_moon_state if other_moon.id != moon.id])
#     
#     for moon in moons:
#         # Update positions
#         moon.update_position()
#     
#     count += 1
#     if count % 10000 == 0:
#         print(time.strftime("%H:%M:%S:"), count, "tried")
