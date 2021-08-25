# Task 1
states = {"VIC": "Victoria", "NSW": "New South Wales",
          "QLD": "Queensland", "TAS": "Tasmania",
          "SA": "South Australia", "WA": "Western Australia",
          "NT": "Northern Territory", "ACT": "Australian Capital Territory"}

for abbreviation, full_name in states.items():
    print(abbreviation, full_name)

# Task 2
try:
    x = int(input("Enter an integer: "))
except ValueError:
    print("Only integers are allowed")

# Task 3
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

# Task 4
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have", cheese_count, "cheeses!")
    print("You have", boxes_of_crackers, "boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# 1
cheese_and_crackers(5, 8)

# 2
cheeses = "four"
boxes = "ten"
cheese_and_crackers(cheeses, boxes)

# 3
print(cheese_and_crackers(cheeses, boxes))

# 4
print(cheese_and_crackers(5, 20))

# 5
types = ["Feta", "Brie", "Cheddar"]
crackers = ["Cracked pepper", "Cheese", "Rosemary sea salt"]

print(cheese_and_crackers(types, crackers))