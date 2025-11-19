
# A closure in programming is a function that “remembers” the variables from the
# scope in which it was created, even after that scope has finished executing.

# In other words, when a function is defined inside another function, the inner
# function has access not only to its own local variables but also to the
# variables of the outer function — and it keeps that access even if the outer
# function is no longer active.

# Example (in Python):
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

# closure = outer_function(10)  # returns inner_function, with x=10 "remembered"
# print(closure(5))  # 15
# print(closure(20)) # 30

# outer_function returns inner_function.

# inner_function keeps access to x, even though outer_function has finished
# running.

# That combination of the function (inner_function) + its remembered environment
# (x=10) is the closure.

# Why closures are useful:

# Encapsulation / Data hiding You can keep certain data private, accessible only
# through the closure. Example: creating private counters or stateful functions
# without using classes.

# Factory functions You can generate specialized functions dynamically. Example:
# building different math functions (e.g., make_multiplier(2) for doubling,
# make_multiplier(3) for tripling).

# Callbacks & Event Handlers Common in JavaScript, closures let callbacks
# “remember” the context they were created in.

# Functional programming patterns They enable currying, partial application, and
# more advanced techniques.


def counter(start) -> tuple:
    count = start

    def increase_count(increase)-> int:
        nonlocal count
        count += increase
        return count
    
    def decrease_count(decrease)-> int:
        nonlocal count
        count -= decrease
        return count

    return increase_count, decrease_count

# count_up, count_down = counter(1)

# print(count_up(2))
# print(count_up(4))
# print(count_up(5))
# print(count_up(8))
# print(count_down(10))


# from datetime import datetime


# def timer(func):

#     def inner():
#         start = datetime.now()
#         result = func()
#         # print(result)
#         end = datetime.now()
#         # print(end-start)
#         return f"It took {end - start} to run the function"
    
#     return inner

# def say_hello():
#     print("Hello! there!")

# hi_timer = timer(say_hello)
# print(hi_timer())

# @timer
# def say_hello():
#     print("Hello!")

# @timer
# def say_goodbye():
#     print("Goodbye!")


# print(say_hello())
# print(say_goodbye())



# # DECORATORS
# # from datetime import datetime 


# # def timer(func):
# #     """ decorator definition for timing the 
# #     wrapped function"""
# #     def wrapper(*args, **kwargs):
# #         start_time = datetime.now()
# #         val = func(*args, **kwargs)
# #         print(val)
# #         end_time = datetime.now()
# #         time_elapsed = end_time - start_time
# #         return time_elapsed

# #     return wrapper


# # @timer
# # def say_hi(name="you"):
# #     return f"Hello there {name}!"

# # @timer
# # def say_bye():
# #     return "Have a nice day!"

# # timed_hi = timer(say_hi)
# # print(timed_hi())
# # print(say_hi("Brad"))
# # print(say_bye())
# # print(say_hi())

# # @timer
# # def do_stuff(num):
# #     counter = 1
# #     for val in range(num):
# #         counter += 1
# #     return counter

# # # print(do_stuff(100_00))
# # # print(do_stuff(1_000_00))
# # # print(do_stuff(100_000_000))
# # print(do_stuff(1_000_000_000))


# ARGS AND KWARGS


# def summer(num1, num2, num3=15, *args, **kwargs):
#     """function that will sum anything we throw at it"""
#     total = sum([num1, num2, num3])
#     print(args)
#     for arg in args:
#         total += arg

#     print(kwargs)
#     for kwarg in kwargs.values():
#         total += kwarg

#     return total


# print(summer(5, 10, 20, 25, 30, 35, num7=40, num8=45))


# lst1 = ['a', 'b', 'c']
# lst2 = [1, 2, 3]
# lst3 = [*lst1, *lst2]
# print(lst3)

# dict1 = {
#     "breakfast": "eggs",
#     "lunch": "leftover beef and broccoli",
#     "dinner": "wings"
# }

# dict2 = {**dict1}

# print(dict2)


