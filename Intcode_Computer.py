#!/usr/bin/env python3

class Intcode_Computer:
    
    # Parameter-Modi
    # POSITION_MODE: Lese/Schreibe an im Parameter angegebene Adresse
    PARAM_MODE_POSITION = 0
    # IMMEDIATE_MODE Nur Lesen: Wert aus Parameter übernehmen
    PARAM_MODE_IMMEDIATE = 1
    # RELATIVE_MODE: Lese/Schreibe an im Parameter angegebene Adresse, verschoben um variables Offset
    PARAM_MODE_RELATIVE = 2
    
    def __init__(self, instructions):
        self.instructions = instructions
    
    # Simple input: Ask user
    def read_input(self):
        return int(input("INPUT: "))
    
    # Simple output: Print to command line
    def process_output(self, output):
        print("OUTPUT:", output)
    
    # Instruktionen ausführen
    def run(self):
        
        # Arbeitsspeicher
        memory = self.instructions[:]
        
        # Bereich für beliebig große Adressen außerhalb des ursprünglichen Speichers
        memory_random_access = {}
        
        # Pointer für Parameter-Modus "RELATIVE"
        relative_memory_pointer = 0
        
        # Aktueller Opcode-Zeiger
        current_instruction_pointer = 0
        
        # Loop über alle Opcodes
        while True:
            
            # Annahme: Opcodes stehen immer im normalen Speicherbereich,
            # nicht im erweiterten Random Access-Speicher
            # Muss ggf. in Zukunft korrigiert werden
            if current_instruction_pointer >= len(memory):
                raise Exception("Opcode pointer overflow")
            
            instruction = f"%05d" % int(memory[current_instruction_pointer])
            instruction = list(instruction)
            instruction.reverse()
            current_opcode = int(instruction[1] + instruction[0])
            parameter_modes = instruction[2:]
            
            def read_memory(num, mode = -1):
                if mode == -1:
                    mode = int(parameter_modes[num-1])
                
                if mode == self.PARAM_MODE_POSITION:
                    param_pos = int(memory[current_instruction_pointer+num])
                
                elif mode == self.PARAM_MODE_IMMEDIATE:
                    param_pos = current_instruction_pointer+num
                
                elif mode == self.PARAM_MODE_RELATIVE:
                    param_pos = relative_memory_pointer + int(memory[current_instruction_pointer+num])
                
                else:
                    raise Exception("Invalid parameter mode")
                
                if param_pos >= len(memory):
                    if param_pos in memory_random_access:
                        return int(memory_random_access[param_pos])
                    else:
                        return 0
                else:
                    return int(memory[param_pos])
            
            def write_memory(num, val):
                mode = int(parameter_modes[num-1])
            
                if mode == self.PARAM_MODE_POSITION:
                    param_pos = int(memory[current_instruction_pointer+num])
                
                elif mode == self.PARAM_MODE_IMMEDIATE:
                    raise Exception("Cannot write in immediate mode")
                
                elif mode == self.PARAM_MODE_RELATIVE:
                    param_pos = relative_memory_pointer + int(memory[current_instruction_pointer+num])
                
                else:
                    raise Exception("Invalid parameter mode")
                
                if param_pos >= len(memory):
                    memory_random_access[param_pos] = int(val)
                else:
                    memory[param_pos] = int(val)
            
            
            # Starten
            
            if current_opcode == 1:
                # ADD
                param1 = read_memory(1)
                param2 = read_memory(2)
                result = param1 + param2
                write_memory(3, result)
                current_instruction_pointer += 4
        
            
            elif current_opcode == 2:
                # MUL
                param1 = read_memory(1)
                param2 = read_memory(2)
                result = param1 * param2
                write_memory(3, result)
                current_instruction_pointer += 4
            
            
            elif current_opcode == 3:
                # INPUT (Wert in Speicher schreiben)
                write_memory(1, self.read_input())
                current_instruction_pointer += 2
        
        
            elif current_opcode == 4:
                # OUTPUT (Wert aus Speicher lesen)
                self.process_output(read_memory(1))
                current_instruction_pointer += 2
        
        
            elif current_opcode == 5:
                # Jump if true
                param1 = read_memory(1)
                if (param1 != 0):
                    current_instruction_pointer = read_memory(2)
                else:
                    current_instruction_pointer += 3
            
            
            elif current_opcode == 6:
                # Jump if false
                param1 = read_memory(1)
                if (param1 == 0):
                    current_instruction_pointer = read_memory(2)
                else:
                    current_instruction_pointer += 3
            
            
            elif current_opcode == 7:
                # less than
                param1 = read_memory(1)
                param2 = read_memory(2)
                if (param1 < param2):
                    write_memory(3, 1)
                else:
                    write_memory(3, 0)
                current_instruction_pointer += 4
        
        
            elif current_opcode == 8:
                # equals
                param1 = read_memory(1)
                param2 = read_memory(2)
                if (param1 == param2):
                    write_memory(3, 1)
                else:
                    write_memory(3, 0)
                current_instruction_pointer += 4
            
            
            elif current_opcode == 9:
                # adjust relative memory address base
                param1 = read_memory(1)
                relative_memory_pointer += param1
                current_instruction_pointer += 2
            
            
            elif current_opcode == 99:
                # HALT
                #print("HALT")
                break
            
            
            else:
                raise Exception("Invalid opcode @ " + str(current_instruction_pointer) + ": " + str(current_opcode))

