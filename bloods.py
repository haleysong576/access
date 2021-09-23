# didn't specify how the html form will look like, so I only used inputs from a file or from the command line.

# getting the input from command line
string_unit = input()
unit_string = string_unit.split()

# check if it's a file name. If not, it's the actual input, convert it into a list. If yes, then conver the lines into a list
if (len(unit_string) == 1): 
    f = open(string_unit)
    unit = list(map(int, f.readline().split()))
    required = list(map(int, f.readline().split()))
else: 
    unit = list(map(int, unit_string))
    required = list(map(int, input().split()))

# number of bloods that can be given
possible = 0

# first, get the blood supply from the same blood type
for i in range(8):
    if unit[i] >= required[i]:
        possible += required[i]
        unit[i] = unit[i] - required[i]
        required[i] = 0
    else:
        possible += unit[i]
        required[i] = required[i] - unit[i]
        unit[i] = 0

# for positive blood types, you can also receive blood from its negative, or O positive.
for i in range(1, 6, 2):
    while (required[i] > 0):
        if unit[i - 1] > 0:
            if unit[i - 1] >= required[i]:
                possible += required[i]
                unit[i - 1] = unit[i - 1] - required[i]
                required[i] = 0
            else:
                possible += unit[i - 1]
                required[i] = required[i] - unit[i - 1]      
                unit[i - 1] = 0
                
        else:
            if unit[1] >= required[i]:
                possible += required[i]
                unit[1] = unit[1] - required[i]
                required[i] = 0
            else:
                possible += unit[1]
                required[i] = required[i] - unit[1]
                unit[1] = 0
            break
    

# this is for AB-, which gets blood from all the negatives
for i in range(0, 5, 2): 
    if unit[i] > 0:
        if unit[i] >= required[6]:
            possible += required[6]
            unit[i] = unit[i] - required[6]
            required[6] = 0
        else:
            possible += unit[i]
            required[6] = required[6] - unit[i]
            unit[i] = 0

# this is for AB+, which gets blood from all the options. First receive from non o negative bloods.

for i in range(1,8): 
    if required[7] == 0: 
        break
    if unit[i] > 0:
        if unit[i] >= required[7]:
            possible += required[7]
            unit[i] = unit[i] - required[7]
            required[7] = 0
        else:
            possible += unit[i]
            required[7] = required[7] - unit[i]
            unit[i] = 0

# O negatives can work for anyone. If there are remaining O negatives, distribute it to remaining required people.
for i in range(8):
    if unit[0] == 0:
        break
    if required[i] > 0:
        if unit[0] >= required[i]:
            possible += required[i]
            unit[0] = unit[0] - required[i]
            required[i] = 0 
        else:
            possible += unit[0]
            required[i] = required[i] - unit[0]
            unit[0] = 0

# Now print the total number
print(possible)