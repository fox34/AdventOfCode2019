#!/usr/bin/env python3

from collections import defaultdict
from random import randint
from Intcode_Computer import Intcode_Computer
import signal
import sys

print("Incomplete. Missing length + 2nd part.")
sys.exit(1)

puzzle_input = "3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,102,1,1036,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1105,1,124,1002,1034,1,1039,101,0,1036,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,101,0,1035,1040,1001,1038,0,1043,1001,1037,0,1042,1105,1,124,1001,1034,1,1039,1008,1036,0,1041,1002,1035,1,1040,102,1,1038,1043,101,0,1037,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,37,1032,1006,1032,165,1008,1040,37,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1101,1,0,1044,1105,1,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,73,1044,1105,1,224,1102,1,0,1044,1105,1,224,1006,1044,247,1002,1039,1,1034,1001,1040,0,1035,101,0,1041,1036,101,0,1043,1038,101,0,1042,1037,4,1044,1105,1,0,58,87,52,69,28,16,88,43,75,16,91,2,94,51,62,80,96,46,64,98,72,8,54,71,47,84,88,44,81,7,90,13,80,42,62,68,85,27,34,2,13,89,87,79,63,76,9,82,58,60,93,63,78,79,43,32,84,25,34,80,87,15,89,96,1,50,75,25,67,82,27,3,89,48,99,33,36,77,86,62,99,19,86,92,6,56,24,96,2,79,9,3,84,41,94,79,76,91,66,50,82,88,85,13,88,18,93,79,12,98,46,75,52,99,95,11,16,25,17,77,55,87,17,74,76,81,41,77,80,92,46,20,99,22,16,41,90,64,89,53,3,61,88,97,14,2,33,79,62,79,90,80,77,71,45,40,51,62,67,82,42,27,97,17,72,77,12,38,97,85,85,35,92,82,3,84,96,40,27,93,96,18,45,98,16,49,82,52,90,43,81,10,88,94,15,42,77,67,84,88,51,35,84,20,99,7,9,79,65,86,39,93,52,98,11,19,83,75,92,27,72,77,77,78,99,18,53,35,75,14,23,90,15,83,15,98,74,14,75,67,98,93,64,97,97,58,77,88,28,19,1,82,96,69,92,34,1,90,45,79,27,25,85,59,89,88,13,91,93,38,95,55,24,61,79,56,63,61,80,10,76,84,24,80,41,83,37,86,81,93,53,33,75,78,6,81,66,84,98,3,37,84,48,89,88,70,93,96,17,94,38,82,39,74,65,90,9,77,55,53,78,10,98,27,96,11,18,86,54,98,53,86,66,19,93,52,99,44,85,79,19,7,53,86,13,90,46,33,86,19,52,79,60,92,94,97,4,99,83,67,84,58,10,96,5,91,75,47,74,93,68,76,74,50,45,99,15,85,13,99,96,30,99,84,59,81,51,64,74,9,27,2,99,34,49,76,61,28,87,56,84,81,32,6,88,48,57,89,43,76,77,15,80,91,45,9,6,52,93,84,77,17,82,32,67,97,92,74,54,46,99,80,5,83,74,85,64,89,36,41,77,47,94,24,86,45,23,99,59,90,43,61,95,98,91,90,33,91,15,19,88,49,54,86,75,42,67,43,54,97,10,10,42,85,10,11,60,76,17,90,43,80,80,34,90,85,71,70,40,80,97,31,55,80,3,58,99,31,31,99,31,90,90,57,29,85,76,22,14,77,76,87,21,88,77,85,33,81,77,94,57,56,18,83,54,90,90,2,89,87,36,13,85,36,85,70,96,20,85,82,43,34,97,93,27,40,44,80,97,2,81,16,44,12,91,35,90,24,49,75,71,96,5,29,65,80,87,35,51,92,43,94,30,84,88,10,99,4,71,76,65,77,71,1,89,90,58,28,77,42,57,81,87,13,16,72,74,32,98,83,8,75,79,10,96,11,92,34,84,13,1,77,78,71,21,63,78,37,98,86,53,84,75,1,60,75,66,86,22,78,32,31,78,97,97,89,23,88,78,4,75,59,99,65,13,85,70,74,77,83,39,62,76,81,33,98,87,25,41,90,48,42,33,24,94,86,15,94,89,21,23,81,29,36,99,93,60,20,90,19,66,52,90,80,97,95,21,86,45,80,78,7,37,80,84,22,6,97,79,34,87,27,43,52,97,84,72,9,89,93,2,75,82,60,92,12,87,89,59,74,64,90,38,71,89,12,26,81,6,53,78,96,8,81,91,69,68,89,76,79,50,77,19,83,14,75,26,76,34,78,1,83,70,80,39,99,62,95,89,99,6,79,93,80,10,83,50,79,80,92,41,78,20,86,9,84,53,87,13,74,0,0,21,21,1,10,1,0,0,0,0,0,0"
puzzle_input = puzzle_input.split(",")

class RepairDroid(Intcode_Computer):
    
    def __init__(self, instructions, starting_direction):
        Intcode_Computer.__init__(self, instructions)
        
        # Umgebungsgröße
        self.w = 0
        self.W = 0
        self.h = 0
        self.H = 0
        
        # Karte der Umgebung
        self.map = defaultdict(lambda: 3)
        
        # Position des Roboters
        self.position = (0,0)
        
        # Aktuelle Richtung
        # 1 = Nord
        # 2 = Süd
        # 3 = West
        # 4 = Ost
        self.direction = starting_direction
        
    
    def print_map(self):
        print("###################################")
        print("Current map:")
        print("\n      ", end="")
        for x in range(self.w, self.W + 1):
            print(abs(x) % 10, end="")
        print("\n    " + "+" * (self.W + 5 - self.w))
        for y in range(self.H, self.h - 1, -1):
            print(f"%3d + " % y, end="")
            for x in range(self.w, self.W + 1):
                tile = self.get_symbol((x,y))
                print(tile, end="")
            print(" +")
    
        print("    " + "+" * (self.W + 5 - self.w))
        print("\n###################################")
        
    
    def get_direction(direction):
        return {1: "⬆", 2: "⬇", 3: "⬅", 4: "⮕"}[direction]
    
    def get_target_position(self, direction = -1):
        pos = self.position
        if direction == -1:
            direction = self.direction
        movement = {1: (0,1), 2: (0,-1), 3: (-1,0), 4: (1,0)}[direction]
        return (pos[0]+movement[0], pos[1]+movement[1])
    
    def turn_after_movement(self):
        
        target_direction = randint(1,4)
        target_position = self.get_target_position(target_direction)
        
        # Ziel ist eine Mauer: Andere Richtung
        while target_position == 0:
            target_direction = randint(1,4)
            target_position = self.get_target_position(target_direction)
        
        #print("Turning from", RepairDroid.get_direction(self.direction), "to", RepairDroid.get_direction(target_direction))
        self.direction = target_direction
    
    def get_symbol(self, position):
        if position == self.position:
            return "."
        return {0: "#", 1: " ", 2: "*", 3: "?"}[self.map[position]]
    
    def read_input(self):
        
        #print("Position:", self.position)
        
        # Sende Richtung an Roboter
        #print("\nMoving", RepairDroid.get_direction(self.direction))
        return self.direction
        
    def process_output(self, output):
        # Empfange Statuscode
        # 0 = Mauer getroffen, Roboter nicht bewegt
        # 1 = Erfolgreich bewegt
        # 2 = Erfolgreich bewegt und Ziel erreicht
        target_position = self.get_target_position()
        
        self.map[target_position] = output
        #print("Got output", output, "for target position", target_position)
        
        if output == 0:
            # Wand, keine weitere Aktion
            pass
            
        elif output == 1:
            self.position = target_position
        
        elif output == 2:
            self.position = target_position
            
            # Part 1
            # 16, -16
            print("Found target at", target_position)
            self.print_map()
            sys.exit(0)
            # Length?!?
        
        else:
            raise Exception("Unexpected output: " + output)
        
        #print("New position:", self.position)
        self.turn_after_movement()
        
        self.w = min(self.w, target_position[0])
        self.W = max(self.W, target_position[0])
        self.h = min(self.h, target_position[1])
        self.H = max(self.H, target_position[1])


cpu = RepairDroid(puzzle_input, 2)

def handle_sigint(sig, frame):
    cpu.print_map()
    sys.exit(0)
signal.signal(signal.SIGINT, handle_sigint)

cpu.run()

