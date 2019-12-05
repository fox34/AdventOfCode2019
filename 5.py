#!/usr/bin/env python3

puzzle_input = "3,225,1,225,6,6,1100,1,238,225,104,0,1102,31,68,225,1001,13,87,224,1001,224,-118,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1,174,110,224,1001,224,-46,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1101,13,60,224,101,-73,224,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1101,87,72,225,101,47,84,224,101,-119,224,224,4,224,1002,223,8,223,1001,224,6,224,1,223,224,223,1101,76,31,225,1102,60,43,225,1102,45,31,225,1102,63,9,225,2,170,122,224,1001,224,-486,224,4,224,102,8,223,223,101,2,224,224,1,223,224,223,1102,29,17,224,101,-493,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,52,54,225,1102,27,15,225,102,26,113,224,1001,224,-1560,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1002,117,81,224,101,-3645,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1108,677,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,226,224,102,2,223,223,1006,224,359,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,374,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,389,101,1,223,223,8,677,677,224,102,2,223,223,1006,224,404,1001,223,1,223,1007,677,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,434,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,479,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,494,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,539,101,1,223,223,7,226,677,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,569,101,1,223,223,1008,226,677,224,102,2,223,223,1005,224,584,101,1,223,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1007,226,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,674,1001,223,1,223,4,223,99,226"
puzzle_input = puzzle_input.split(",")

def run_opcode():
    memory = puzzle_input[:]
    
    current_pointer = 0
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
            val = int(input("MEMCPY INPUT: "))
            dest = get_parameter(1, False) # Nur Position Mode
            #print(current_pointer, "WRITE", val, "=>", dest)
            memory[dest] = val
            
            # Nächste Instruktion
            current_pointer += 2
        
        
        elif current_opcode == 4:
            # ECHO
            target = get_parameter(1, False) # Nur Position Mode
            print(current_pointer, "\t****\t\t\tMEMORY @", target, ":", memory[target])
            
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
            print("HALT")
            break
        
        else:
            raise Exception("Invalid opcode @ " + str(current_pointer) + ": " + str(current_opcode))
    

# Teil 1 + 2
run_opcode()
