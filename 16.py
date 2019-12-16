#!/usr/bin/env python3

import math

puzzle_input = "59756772370948995765943195844952640015210703313486295362653878290009098923609769261473534009395188480864325959786470084762607666312503091505466258796062230652769633818282653497853018108281567627899722548602257463608530331299936274116326038606007040084159138769832784921878333830514041948066594667152593945159170816779820264758715101494739244533095696039336070510975612190417391067896410262310835830006544632083421447385542256916141256383813360662952845638955872442636455511906111157861890394133454959320174572270568292972621253460895625862616228998147301670850340831993043617316938748361984714845874270986989103792418940945322846146634931990046966552"
#puzzle_input = "69317163492948606335995924319873"

numbers = list(map(int, list(puzzle_input)))


def calc_phase(in_list):
    result = []
    pattern = [0, 1, 0, -1]
    for repeat_idx in range(len(in_list)):
        fft = 0
        for num_idx, num in enumerate(in_list):
            pattern_idx = math.floor((num_idx+1)/(repeat_idx+1)) % len(pattern)
            #print(repeat_idx, ",", num, ":", pattern_idx)
            fft += pattern[pattern_idx] * num
            
        result.append(abs(fft) % 10)
    return result


step = 0
steps = 100
result = numbers[:]
while step < steps:
    step += 1
    result = calc_phase(result)

# Teil 1: 6954915595770795875296...
print("".join(list(map(str, result))))


# Teil 2
print("Part 2 incomplete, obvious optimization necessary. Ain't nobody got time for that.")
quit()

real_signal = (numbers[:])*10000
message_offset = int(puzzle_input[0:7])

step = 0
steps = 100
result = real_signal
while step < steps:
    step += 1
    print(step, "steps...")
    result = calc_phase(result)

print("Result:", result[message_offset:message_offset+8])
