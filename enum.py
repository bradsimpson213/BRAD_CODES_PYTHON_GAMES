# To "enumerate" means to list or count things one by one 
# or to determine the number of something. It can also refer 
# to a specific programming function, such as in Python, 
# which adds a counter to an iterable object to allow access
# to both the index and the item

numbers = ["one", "two", "three", "four", "five" ]
enum_numbers = enumerate(numbers)
print(enum_numbers)
print(list(enum_numbers))

for index, num in enumerate(numbers, 1):
    print(f"{index}. {num}")