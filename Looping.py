#1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#2
total = 0
for i in range(1, 10):
    if i % 2 == 0:
        total += i
print(total)

#3
def longest_string_length(string_list):
    max_len = 0
    for string in string_list:
        length = len(string)
        if length > max_len:
            max_len = length
    return max_len
my_list = ['I', 'love', 'python', 'coding']
print(longest_string_length(my_list))