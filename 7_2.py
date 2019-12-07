#!/usr/bin/env python3

import time
import threading

puzzle_input = "3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99"
puzzle_input = puzzle_input.split(",")

class Opcode_Run:
    def __init__(self, title, phase_setting):
        self.title = title
        self.input_pool = [phase_setting]
        self.return_value = False
    
    def run(self):
        memory = puzzle_input[:]
    
        current_pointer = 0
        while True:
        
            if current_pointer >= len(memory):
                raise Exception("Reached end")
        
            instruction = f"%05d" % int(memory[current_pointer])
            instruction = list(instruction)
            instruction.reverse()
            current_opcode = int(instruction[1] + instruction[0])
            parameter_modes = instruction[2:]
        
            def get_parameter(num, parse_mode = True):
                if parse_mode == False:
                    mode = 1
                else:
                    mode = int(parameter_modes[num-1])
            
                if mode == 0:
                    param_pos = int(memory[current_pointer+num])
                    return int(memory[param_pos])
                elif mode == 1:
                    return int(memory[current_pointer+num])
                else:
                    raise Exception("Invalid parameter mode")
        
            if current_opcode == 1:
                # ADD
                param1 = get_parameter(1)
                param2 = get_parameter(2)
                dest = get_parameter(3, False) # Nur Position Mode
                result = param1 + param2
                memory[dest] = result
                current_pointer += 4
        
            elif current_opcode == 2:
                # MUL
                param1 = get_parameter(1)
                param2 = get_parameter(2)
                dest = get_parameter(3, False) # Nur Position Mode
                result = param1 * param2
                memory[dest] = result
                current_pointer += 4
        
            elif current_opcode == 3:
                # MEMCPY
                #val = int(input("MEMCPY INPUT: ")) # Nutzer fragen
                
                while len(self.input_pool) == 0:
                    #print(self.title, "Waiting for input...")
                    time.sleep(.001)
                
                val = int(self.input_pool.pop(0)) # Aus dem Compiler übergebenen Argumenten lesen
                dest = get_parameter(1, False) # Nur Position Mode
                #print(current_pointer, "WRITE", val, "=>", dest)
                memory[dest] = val
            
                # Nächste Instruktion
                current_pointer += 2
        
        
            elif current_opcode == 4:
                # ECHO/READ
                target = get_parameter(1, False) # Nur Position Mode
                self.return_value = int(memory[target])
                
                #print(current_pointer, "\t****\t\t\tMEMORY @", target, ":", return_value)
                
                self.target_obj.input_pool.append(self.return_value)
                
                current_pointer += 2
        
        
            elif current_opcode == 5:
                # Jump if true
                param1 = get_parameter(1)
                if (param1 != 0):
                    current_pointer = get_parameter(2)
                else:
                    current_pointer += 3
        
            elif current_opcode == 6:
                # Jump if false
                param1 = get_parameter(1)
                if (param1 == 0):
                    current_pointer = get_parameter(2)
                else:
                    current_pointer += 3
        
            elif current_opcode == 7:
                # less than
                param1 = get_parameter(1)
                param2 = get_parameter(2)
                dest = get_parameter(3, False)
                if (param1 < param2):
                    memory[dest] = 1
                else:
                    memory[dest] = 0
                current_pointer += 4
        
        
            elif current_opcode == 8:
                # equals
                param1 = get_parameter(1)
                param2 = get_parameter(2)
                dest = get_parameter(3, False)
                if (param1 == param2):
                    memory[dest] = 1
                else:
                    memory[dest] = 0
                current_pointer += 4
            
            elif current_opcode == 99:
                # HALT
                print(self.title, "HALT")
                break
        
            else:
                raise Exception("Invalid opcode @ " + str(current_pointer) + ": " + str(current_opcode))
    

# 5 Amplifiers: A, B, C, D, E
# Jeder Amplifier nimmt zwei Inputs:
# 1. Phase Setting: 0/1/2/3/4, jede Zahl exakt einmal, Reihenfolge unbekannt
# 2. Input Signal = Output des vorherigen Amplifiers
# Ausgabe: Output Instruction. Solange Amplifier noch kein Input hat, warten


# Teil 2
max_signal = 0
max_combination = []

# Sicherlich eleganter möglich, aber wenn es schon nur fünf Möglichkeiten gibt...
for a in range(5, 10):
    for b in range(5, 10):
        if b == a:
            continue
        for c in range(5, 10):
            if c == b or c == a:
                continue
            for d in range(5, 10):
                if d == c or d == b or d == a:
                    continue
                for e in range(5, 10):
                    if e == d or e == c or e == b or e == a:
                        continue
                    
                    print("Running", a,b,c,d,e)
                    
                    cpu_a = Opcode_Run("A" + str(a), a)
                    cpu_b = Opcode_Run("B" + str(b), b)
                    cpu_c = Opcode_Run("C" + str(c), c)
                    cpu_d = Opcode_Run("D" + str(d), d)
                    cpu_e = Opcode_Run("E" + str(e), e)
                    
                    # Initial-Startwert
                    cpu_a.input_pool.append(0)
                    
                    # Parallel starten
                    cpu_a.target_obj = cpu_b
                    cpu_b.target_obj = cpu_c
                    cpu_c.target_obj = cpu_d
                    cpu_d.target_obj = cpu_e
                    cpu_e.target_obj = cpu_a
                    
                    thread_a = threading.Thread(target = cpu_a.run)
                    thread_b = threading.Thread(target = cpu_b.run)
                    thread_c = threading.Thread(target = cpu_c.run)
                    thread_d = threading.Thread(target = cpu_d.run)
                    thread_e = threading.Thread(target = cpu_e.run)
                    
                    thread_a.start()
                    thread_b.start()
                    thread_c.start()
                    thread_d.start()
                    thread_e.start()
                    
                    thread_a.join()
                    thread_b.join()
                    thread_c.join()
                    thread_d.join()
                    thread_e.join()
                    
                    if cpu_e.return_value > max_signal:
                        max_signal = cpu_e.return_value
                        max_combination = [a,b,c,d,e]
                    
                    
print("Max signal:", max_signal, "from", max_combination)
