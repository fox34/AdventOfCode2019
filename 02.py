#!/usr/bin/env python3

import copy

input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0"
input = input.split(",")

def run(noun, verb, desired_result = False):
    
    memory = copy.copy(input)
    memory[1] = noun
    memory[2] = verb
    
    current_pointer = 0
    while True:
    
        if current_pointer >= len(memory):
            raise Exception("Reached end")
    
        current_opcode = int(memory[current_pointer])
    
        if current_opcode == 1:
            # ADD
            pos1 = int(memory[current_pointer+1])
            pos2 = int(memory[current_pointer+2])
            pos3 = int(memory[current_pointer+3])
            param1 = int(memory[pos1])
            param2 = int(memory[pos2])
            result = param1 + param2
            #print(str(param1), "+", str(param2), "=", str(result), "=>", str(current_pointer+3))
            memory[pos3] = result
    
        elif current_opcode == 2:
            # MUL
            pos1 = int(memory[current_pointer+1])
            pos2 = int(memory[current_pointer+2])
            pos3 = int(memory[current_pointer+3])
            param1 = int(memory[pos1])
            param2 = int(memory[pos2])
            result = param1 * param2
            #print(str(param1), "*", str(param2), "=", str(result), "=>", str(current_pointer+3))
            memory[pos3] = result
    
        elif current_opcode == 99:
            # END
            if (desired_result == False):
                print("End at position", current_pointer, "Result:", memory[0])
            elif (memory[0] == desired_result):
                print("Found desired result with params", noun, verb, "Solution =", 100*noun+verb)
            break
        
        else:
            raise Exception("Invalid opcode: " + str(current_opcode))
    
        # Nächste Instruktion
        current_pointer += 4



# Teil 1
run(12, 2)

# Teil 2
for noun in range(100):
    for verb in range(100):
        run(noun, verb, 19690720)

