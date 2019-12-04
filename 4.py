#!/usr/bin/env python3

low = 353096
high = 843212

num_possible = 0

# Teil 1
for n in range(low + 1, high):
    digits = list(str(n))
    
    prev_digit = 0
    has_ascending_digits = True
    has_double_digit = False
    for digit in digits:
        
        digit = int(digit)
        
        # Folgende Ziffer kleiner als vorherige
        if digit < prev_digit:
            has_ascending_digits = False
            break
        
        # Ziffer identisch zu vorheriger
        if digit == prev_digit:
            has_double_digit = True
    
        prev_digit = digit
    
    if has_double_digit and has_ascending_digits:
        #print("Valid:", str(n))
        num_possible += 1
    else:
        #print("Invalid:", str(n))
        pass
    
# 579
print(num_possible, "Kombinationen im Bereich von (", low, ",", high, "); Teil 1")


# Teil 2
num_possible = 0
for n in range(low + 1, high):
    digits = list(str(n))
    
    has_double_digit = False
    has_ascending_digits = True
    double_digits = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7:0, 8: 0, 9: 0}
    prev_digit = 0
    for digit in digits:
        
        digit = int(digit)
        
        # Folgende Ziffer kleiner als vorherige
        if digit < prev_digit:
            has_ascending_digits = False
            break
        
        # Ziffer identisch zu vorheriger
        if digit == prev_digit:
            double_digits[digit] += 1
        
        prev_digit = digit
    
    for num in double_digits.values():
        if num == 1:
            has_double_digit = True
            break
    
    if has_double_digit and has_ascending_digits:
        #print("Valid:", str(n))
        num_possible += 1
    else:
        #print("Invalid:", str(n))
        pass
    
# 358
print(num_possible, "Kombinationen im Bereich von (", low, ",", high, "); Teil 2")

