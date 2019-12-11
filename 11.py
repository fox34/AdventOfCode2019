#!/usr/bin/env python3

import time
from Intcode_Computer import Intcode_Computer

puzzle_input = "3,8,1005,8,325,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,102,1,8,29,1006,0,41,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,54,3,8,102,-1,8,10,101,1,10,10,4,10,1008,8,1,10,4,10,102,1,8,76,1,9,11,10,2,5,2,10,2,1107,19,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,110,2,1007,10,10,2,1103,13,10,1006,0,34,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,142,1006,0,32,1,101,0,10,2,9,5,10,1006,0,50,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,1,10,4,10,101,0,8,179,1,1005,11,10,2,1108,11,10,1006,0,10,1,1004,3,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1002,8,1,216,1,1002,12,10,2,1102,3,10,1,1007,4,10,2,101,7,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,253,2,104,3,10,1006,0,70,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,102,1,8,282,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,101,0,8,305,101,1,9,9,1007,9,962,10,1005,10,15,99,109,647,104,0,104,1,21102,838211572492,1,1,21102,342,1,0,1105,1,446,21102,825326674840,1,1,21101,0,353,0,1106,0,446,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,29086686211,1,21102,1,400,0,1106,0,446,21102,209420786919,1,1,21101,0,411,0,1105,1,446,3,10,104,0,104,0,3,10,104,0,104,0,21101,0,838337298792,1,21101,434,0,0,1105,1,446,21101,988661154660,0,1,21102,1,445,0,1106,0,446,99,109,2,21201,-1,0,1,21101,40,0,2,21101,0,477,3,21101,0,467,0,1105,1,510,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,472,473,488,4,0,1001,472,1,472,108,4,472,10,1006,10,504,1101,0,0,472,109,-2,2106,0,0,0,109,4,1201,-1,0,509,1207,-3,0,10,1006,10,527,21102,0,1,-3,22102,1,-3,1,22102,1,-2,2,21101,0,1,3,21101,546,0,0,1105,1,551,109,-4,2105,1,0,109,5,1207,-3,1,10,1006,10,574,2207,-4,-2,10,1006,10,574,21201,-4,0,-4,1105,1,642,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21102,1,593,0,1105,1,551,21202,1,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,612,21102,0,1,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,634,21202,-1,1,1,21102,1,634,0,105,1,509,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0"
puzzle_input = puzzle_input.split(",")

class Day11(Intcode_Computer):
    
    def __init__(self, instructions):
        
        Intcode_Computer.__init__(self, instructions)
        
        # Position des Roboters
        self.direction = "U" # U R D L
        self.position = (0,0)
        
        # Bild-Matrix
        self.image = {}
        
        # Abmessungen
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0
        
        # Erwarteter Output
        # 0 = Farbe
        # 1 = Position
        self.expected_output = 0
    
        # Hintergrundfarbe
        self.background = 0
        
    
    def read_input(self):
        self.expected_output = 0
        if self.position in self.image:
            #print("Reading:", self.position, ":", self.image[x][y])
            return self.image[self.position]
        else:
            #print("Reading:", self.position, ": Nothing printed, return", self.background)
            return self.background
    
    def process_output(self, output):
        
        if self.expected_output == 0:
            # Malen
            #print("Got output", output, ", painting pixel at", x, y)
            self.image[self.position] = output
        
        elif self.expected_output == 1:
            #print("Got output", output, ", moving from", self.position, " to ", end="")
            # Bewegen
            if output == 0:
                # 90° links
                self.direction = {"U":"L","L":"D","D":"R","R":"U"}[self.direction]
            
            elif output == 1:
                # 90° rechts
                self.direction = {"U":"R","R":"D","D":"L","L":"U"}[self.direction]
                
            else:
                raise Exception("Unexpected direction")
            
            if self.direction == "U":
                self.position = (self.position[0], self.position[1] + 1)
            elif self.direction == "D":
                self.position = (self.position[0], self.position[1] - 1)
            elif self.direction == "R":
                self.position = (self.position[0] + 1, self.position[1])
            elif self.direction == "L":
                self.position = (self.position[0] - 1, self.position[1])
            else:
                raise Exception("Unknown direction!!!")
            
            self.min_x = min(self.min_x, self.position[0])
            self.max_x = max(self.max_x, self.position[0])
            self.min_y = min(self.min_y, self.position[1])
            self.max_y = max(self.max_y, self.position[1])
            #print(self.position, ", moved in direction:", self.direction)
            
        else:
            raise Exception("Unexpected output")
            
        self.expected_output += 1



cpu = Day11(puzzle_input)
cpu.run()

num = len(cpu.image)

# 2219
print(num)


# Teil 2
print()
cpu = Day11(puzzle_input)
cpu.background = 1
cpu.run()

width = abs(cpu.min_x) + abs(cpu.max_x)
height = abs(cpu.min_y) + abs(cpu.max_y)

# HAFULAPE
for y in range(cpu.max_y, cpu.min_y - 1, -1):
    curr_line = ""
    for x in range(cpu.min_x + 1, cpu.max_x - 1):
        pixel = cpu.background
        if (x,y) in cpu.image:
            pixel = cpu.image[(x,y)]
        
        if pixel == 0:
            curr_line += " "
        elif pixel == 1:
            curr_line += "#"
        else:
            curr_line += "?"
    
    print(curr_line)

