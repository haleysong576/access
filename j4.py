import math

# if getting input form html form
import cgi
form = cgi.FieldStorage()
searchterm =  form.getvalue('D')

# if getting input from command line or from a file 
if searchterm == None:
    mins = input()
    if (mins.isnumeric() == 0): 
        f = open(mins)
        mins = int(f.readline())
    else: 
        mins = int(mins)
else:
    mins = searchterm

# setting up the 12 hour clock
hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11]
# variable to store the number of arithmetic sequence 
result = 0

# checks if a given list of integers are an artihmetic sequence
def is_arithmetic(numbers):
    term = numbers[1] - numbers[0]
    for i in range(2, len(numbers)):
        if numbers[i] - numbers [i - 1] != term:
            return 0

    return 1

# given the hour and the minute, it turns them into one list of integers
def listing(hour, min): 
    output = [int(d) for d in str(hour)]
    if (min >= 10):
        mins = [int(d) for d in str(min)]
        output.extend(mins)
    else:
        output.append(0)
        output.append(min)
    return output

# finds the number of arithmetic sequences in 12 hours
def twelve_hours(mins): 
    num_of_hours = round(math.floor(mins / 60))
    num_of_mins = round(mins % 60)
    possible = 0
    for i in range (num_of_hours):
        hour = i % 12
        for i in range(60):
            if (is_arithmetic(listing(hours[hour], i)) == 1):
                possible += 1

    final_hour = num_of_hours % 12 
    for i in range(num_of_mins + 1):
        if (is_arithmetic(listing(hours[final_hour], i)) == 1):
            possible += 1
    return possible

# if the input is more than 12 hours, multiply by the # of cycles and add remaining minutes. Otherwise, just put it in the fuction above.
if mins > 720:
    number = math.floor(mins / 720)
    minutes = mins % 720
    result = number * twelve_hours(720) + twelve_hours(minutes)
else:
    result = twelve_hours(mins)

# print the result
print(result)

