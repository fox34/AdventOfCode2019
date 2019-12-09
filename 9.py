#!/usr/bin/env python3

import time

puzzle_input = "1102,34463338,34463338,63,1007,63,34463338,63,1005,63,53,1102,3,1,1000,109,988,209,12,9,1000,209,6,209,3,203,0,1008,1000,1,63,1005,63,65,1008,1000,2,63,1005,63,904,1008,1000,0,63,1005,63,58,4,25,104,0,99,4,0,104,0,99,4,17,104,0,99,0,0,1102,33,1,1011,1102,1,26,1010,1101,0,594,1029,1101,0,20,1018,1102,38,1,1000,1102,35,1,1001,1101,800,0,1023,1101,0,599,1028,1101,0,34,1013,1101,0,737,1026,1102,21,1,1005,1102,1,0,1020,1102,1,195,1024,1101,31,0,1016,1101,0,1,1021,1102,22,1,1004,1102,1,32,1014,1102,37,1,1019,1102,36,1,1002,1101,23,0,1003,1102,190,1,1025,1101,28,0,1009,1101,807,0,1022,1102,30,1,1015,1101,0,27,1017,1102,1,25,1012,1102,1,39,1008,1101,0,29,1007,1101,734,0,1027,1101,0,24,1006,109,28,2105,1,-4,4,187,1105,1,199,1001,64,1,64,1002,64,2,64,109,-19,1208,-9,37,63,1005,63,219,1001,64,1,64,1106,0,221,4,205,1002,64,2,64,109,20,1206,-8,233,1106,0,239,4,227,1001,64,1,64,1002,64,2,64,109,-29,2101,0,4,63,1008,63,21,63,1005,63,259,1106,0,265,4,245,1001,64,1,64,1002,64,2,64,109,-2,2107,37,4,63,1005,63,285,1001,64,1,64,1106,0,287,4,271,1002,64,2,64,109,14,1206,8,301,4,293,1105,1,305,1001,64,1,64,1002,64,2,64,109,11,21101,40,0,-6,1008,1017,40,63,1005,63,331,4,311,1001,64,1,64,1105,1,331,1002,64,2,64,109,-21,1208,1,23,63,1005,63,353,4,337,1001,64,1,64,1106,0,353,1002,64,2,64,109,26,1205,-7,371,4,359,1001,64,1,64,1106,0,371,1002,64,2,64,109,-15,21102,41,1,2,1008,1015,40,63,1005,63,395,1001,64,1,64,1106,0,397,4,377,1002,64,2,64,109,-3,2108,22,-6,63,1005,63,415,4,403,1105,1,419,1001,64,1,64,1002,64,2,64,109,-6,1201,-4,0,63,1008,63,35,63,1005,63,439,1106,0,445,4,425,1001,64,1,64,1002,64,2,64,109,14,21102,42,1,-4,1008,1014,42,63,1005,63,467,4,451,1105,1,471,1001,64,1,64,1002,64,2,64,109,-23,1201,10,0,63,1008,63,21,63,1005,63,497,4,477,1001,64,1,64,1105,1,497,1002,64,2,64,109,16,21101,43,0,2,1008,1013,42,63,1005,63,521,1001,64,1,64,1105,1,523,4,503,1002,64,2,64,109,3,21107,44,45,1,1005,1015,541,4,529,1105,1,545,1001,64,1,64,1002,64,2,64,109,-2,1205,8,561,1001,64,1,64,1106,0,563,4,551,1002,64,2,64,109,-7,1207,2,28,63,1005,63,579,1106,0,585,4,569,1001,64,1,64,1002,64,2,64,109,24,2106,0,-1,4,591,1106,0,603,1001,64,1,64,1002,64,2,64,109,-4,21108,45,45,-9,1005,1016,625,4,609,1001,64,1,64,1105,1,625,1002,64,2,64,109,-24,2101,0,0,63,1008,63,35,63,1005,63,651,4,631,1001,64,1,64,1106,0,651,1002,64,2,64,109,10,1202,-7,1,63,1008,63,24,63,1005,63,675,1001,64,1,64,1105,1,677,4,657,1002,64,2,64,109,-2,2102,1,-1,63,1008,63,41,63,1005,63,697,1105,1,703,4,683,1001,64,1,64,1002,64,2,64,109,-2,21108,46,45,3,1005,1010,723,1001,64,1,64,1105,1,725,4,709,1002,64,2,64,109,28,2106,0,-8,1106,0,743,4,731,1001,64,1,64,1002,64,2,64,109,-37,2102,1,3,63,1008,63,35,63,1005,63,769,4,749,1001,64,1,64,1105,1,769,1002,64,2,64,109,26,21107,47,46,-8,1005,1016,789,1001,64,1,64,1106,0,791,4,775,1002,64,2,64,109,7,2105,1,-8,1001,64,1,64,1106,0,809,4,797,1002,64,2,64,109,-37,1202,7,1,63,1008,63,35,63,1005,63,831,4,815,1105,1,835,1001,64,1,64,1002,64,2,64,109,18,1207,-5,30,63,1005,63,853,4,841,1106,0,857,1001,64,1,64,1002,64,2,64,109,-7,2108,37,-5,63,1005,63,873,1105,1,879,4,863,1001,64,1,64,1002,64,2,64,109,-7,2107,23,8,63,1005,63,897,4,885,1106,0,901,1001,64,1,64,4,64,99,21101,27,0,1,21102,1,915,0,1106,0,922,21201,1,12374,1,204,1,99,109,3,1207,-2,3,63,1005,63,964,21201,-2,-1,1,21101,942,0,0,1105,1,922,22102,1,1,-1,21201,-2,-3,1,21102,957,1,0,1105,1,922,22201,1,-1,-2,1106,0,968,21201,-2,0,-2,109,-3,2106,0,0"
puzzle_input = puzzle_input.split(",")

class Opcode_Run:
    
    # Parameter-Modi
    # POSITION_MODE: Lese/Schreibe an im Parameter angegebene Adresse
    PARAM_MODE_POSITION = 0
    # IMMEDIATE_MODE Nur Lesen: Wert aus Parameter übernehmen
    PARAM_MODE_IMMEDIATE = 1
    # RELATIVE_MODE: Lese/Schreibe an im Parameter angegebene Adresse, verschoben um variables Offset
    PARAM_MODE_RELATIVE = 2
    
    def __init__(self, title):
        self.title = title
        
        # Letztes Ergebnis von Opcode 4
        self.return_value = False
        
        # Eingabe-Pool für IPC (Inter-Prozess-Kommunikation)
        # Nicht genutzt hier
        self.input_pool = []
        
        # Input für Opcode 3 von Nutzer fragen (keine IPC)
        self.ask_for_input = True
        
        # Ergebnis von Opcode 4 einfach ausgeben
        self.output_as_echo = True
        
        # Ergebnis von Opcode 4 an self.target_obj.input_pool übergeben (IPC)
        self.pass_opcode_4_to_target_obj = False
    
    
    def run(self):
        memory = puzzle_input[:]
        
        # Bereich für beliebige größere Adressen
        memory_random_access = {}
        
        # Offset für Parameter-Modus "RELATIVE"
        relative_param_base = 0
        
        # Aktueller Zeiger
        current_pointer = 0
        
        # Loop über alle Opcodes
        while True:
            
            # Annahme: Opcodes stehen immer im normalen Speicherbereich,
            # nicht im erweiterten Random Access-Speicher
            # Korrekt für dieses Rätsel, muss ggf. in Zukunft korrigiert werden
            if current_pointer >= len(memory):
                raise Exception("Opcode offset overflow")
        
            instruction = f"%05d" % int(memory[current_pointer])
            instruction = list(instruction)
            instruction.reverse()
            current_opcode = int(instruction[1] + instruction[0])
            parameter_modes = instruction[2:]
            
            def read_memory(num, mode = -1):
                if mode == -1:
                    mode = int(parameter_modes[num-1])
                
                if mode == self.PARAM_MODE_POSITION:
                    param_pos = int(memory[current_pointer+num])
                
                elif mode == self.PARAM_MODE_IMMEDIATE:
                    param_pos = current_pointer+num
                
                elif mode == self.PARAM_MODE_RELATIVE:
                    param_pos = relative_param_base + int(memory[current_pointer+num])
                
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
                    param_pos = int(memory[current_pointer+num])
                
                elif mode == self.PARAM_MODE_IMMEDIATE:
                    raise Exception("Cannot write in immediate mode")
                
                elif mode == self.PARAM_MODE_RELATIVE:
                    param_pos = relative_param_base + int(memory[current_pointer+num])
                
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
                current_pointer += 4
        
            
            elif current_opcode == 2:
                # MUL
                param1 = read_memory(1)
                param2 = read_memory(2)
                result = param1 * param2
                write_memory(3, result)
                current_pointer += 4
            
            
            elif current_opcode == 3:
                # MEMCPY (Wert in Speicher schreiben)
                
                if self.ask_for_input:
                    # Nutzer fragen
                    val = int(input("MEMCPY INPUT: "))
                
                else:
                    # Aus dem Compiler übergebenen Argumenten lesen (IPC)
                    while len(self.input_pool) == 0:
                        print(self.title, "Waiting for input...")
                        time.sleep(1)
                    val = int(self.input_pool.pop(0))
                
                write_memory(1, val)
                current_pointer += 2
        
        
            elif current_opcode == 4:
                # ECHO/READ/RETURN (Wert ausgeben oder an anderen Prozess übergeben, IPC)
                self.return_value = read_memory(1)
                
                if self.output_as_echo:
                    print("Opcode 4 output:", self.return_value)
                
                if self.pass_opcode_4_to_target_obj:
                    self.target_obj.input_pool.append(self.return_value)
                
                current_pointer += 2
        
        
            elif current_opcode == 5:
                # Jump if true
                param1 = read_memory(1)
                if (param1 != 0):
                    current_pointer = read_memory(2)
                else:
                    current_pointer += 3
            
            
            elif current_opcode == 6:
                # Jump if false
                param1 = read_memory(1)
                if (param1 == 0):
                    current_pointer = read_memory(2)
                else:
                    current_pointer += 3
            
            
            elif current_opcode == 7:
                # less than
                param1 = read_memory(1)
                param2 = read_memory(2)
                if (param1 < param2):
                    write_memory(3, 1)
                else:
                    write_memory(3, 0)
                current_pointer += 4
        
        
            elif current_opcode == 8:
                # equals
                param1 = read_memory(1)
                param2 = read_memory(2)
                if (param1 == param2):
                    write_memory(3, 1)
                else:
                    write_memory(3, 0)
                current_pointer += 4
            
            
            elif current_opcode == 9:
                # adjust relative memory address base
                param1 = read_memory(1)
                relative_param_base += param1
                current_pointer += 2
            
            
            elif current_opcode == 99:
                # HALT
                print(self.title, "HALT")
                break
            
            
            else:
                raise Exception("Invalid opcode @ " + str(current_pointer) + ": " + str(current_opcode))


cpu = Opcode_Run("09.12.")
cpu.run()
