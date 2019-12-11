#!/usr/bin/env python3

puzzle_input = "3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99"
puzzle_input = puzzle_input.split(",")

def run_opcode(memcpy_args = []):
    memory = puzzle_input[:]
    
    current_pointer = 0
    return_value = False
    while True:
        
        if current_pointer >= len(memory):
            raise Exception("Reached end")
        
        # A B C D E
        # D E = Opcode
        # A, B, C = Parameter-Modi für Parameter 1 (C), 2 (B), 3 (A)
        
        # Instruktion auf korrekte Länge bringen
        instruction = f"%05d" % int(memory[current_pointer])
        
        instruction = list(instruction)
        
        # E D C B A
        instruction.reverse()
        
        current_opcode = int(instruction[1] + instruction[0])
        parameter_modes = instruction[2:]
        
        def get_parameter(num, parse_mode = True):
            if parse_mode == False:
                mode = 1
            else:
                mode = int(parameter_modes[num-1])
            
            if mode == 0:
                # Position mode
                param_pos = int(memory[current_pointer+num])
                return int(memory[param_pos])
                
            elif mode == 1:
                # Immediate mode
                return int(memory[current_pointer+num])
            
            else:
                raise Exception("Invalid parameter mode")
        
        
        if current_opcode == 1:
            # ADD
            param1 = get_parameter(1)
            param2 = get_parameter(2)
            dest = get_parameter(3, False) # Nur Position Mode
            result = param1 + param2
            #print(current_pointer, "ADD", param1, "+", param2, "=", result, "=>", dest)
            memory[dest] = result
            
            # Nächste Instruktion
            current_pointer += 4
        
        
        elif current_opcode == 2:
            # MUL
            param1 = get_parameter(1)
            param2 = get_parameter(2)
            dest = get_parameter(3, False) # Nur Position Mode
            result = param1 * param2
            #print(current_pointer, "MUL", param1, "*", param2, "=", result, "=>", dest)
            memory[dest] = result
            
            # Nächste Instruktion
            current_pointer += 4
        
        
        elif current_opcode == 3:
            # MEMCPY
            #val = int(input("MEMCPY INPUT: ")) # Nutzer fragen
            val = int(memcpy_args.pop(0)) # Aus dem Compiler übergebenen Argumenten lesen
            dest = get_parameter(1, False) # Nur Position Mode
            #print(current_pointer, "WRITE", val, "=>", dest)
            memory[dest] = val
            
            # Nächste Instruktion
            current_pointer += 2
        
        
        elif current_opcode == 4:
            # ECHO/READ
            target = get_parameter(1, False) # Nur Position Mode
            #print(current_pointer, "\t****\t\t\tMEMORY @", target, ":", memory[target])
            if return_value != False:
                raise Exception("Return value already set")
            
            return_value = int(memory[target])
            
            # Nächste Instruktion
            current_pointer += 2
        
        
        elif current_opcode == 5:
            # Jump if true
            param1 = get_parameter(1)
            if (param1 != 0):
                # Jump
                current_pointer = get_parameter(2)
            else:
                current_pointer += 3
        
        
        elif current_opcode == 6:
            # Jump if false
            param1 = get_parameter(1)
            if (param1 == 0):
                # Jump
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
            #print("HALT")
            return return_value
        
        else:
            raise Exception("Invalid opcode @ " + str(current_pointer) + ": " + str(current_opcode))
    

# 5 Amplifiers: A, B, C, D, E
# Jeder Amplifier nimmt zwei Inputs:
# 1. Phase Setting: 0/1/2/3/4, jede Zahl exakt einmal, Reihenfolge unbekannt
# 2. Input Signal = Output des vorherigen Amplifiers
# Ausgabe: Output Instruction. Solange Amplifier noch kein Input hat, warten


# Teil 1
max_signal = 0
max_combination = []

for a in range(5):
    
    out_a = run_opcode([a, 0])
    
    for b in range(5):
        if b == a:
            continue
        
        out_b = run_opcode([b, out_a])
        
        for c in range(5):
            if c == b or c == a:
                continue
            
            out_c = run_opcode([c, out_b])
            
            for d in range(5):
                if d == c or d == b or d == a:
                    continue
                
                out_d = run_opcode([d, out_c])
                
                for e in range(5):
                    if e == d or e == c or e == b or e == a:
                        continue
                    
                    out_e = run_opcode([e, out_d])
                    if out_e > max_signal:
                        max_signal = out_e
                        max_combination = [a,b,c,d,e]

print("Max signal:", max_signal, "from", max_combination)
