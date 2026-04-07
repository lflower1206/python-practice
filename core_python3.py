"""
Core Python 3 Features - Practice Exercises
============================================
Work through each section. Try to complete the TODOs before reading the hints.
"""

# =============================================================================
# 1. PRINT AS A FUNCTION
# =============================================================================
print("--- 1. Print as a Function ---")

# Python 2: print "hello"
# Python 3:
print("Hello, Python 3!")
print("a", "b", "c", sep="-")  # sep controls the separator
print("no newline", end=" ")  # end controls the line ending
print("<-- same line")

# TODO: Print your name and age on one line using sep="/"


# =============================================================================
# 2. DIVISION
# =============================================================================
print("\n--- 2. Division ---")

print(7 / 2)  # 3.5  (true division, always float)
print(7 // 2)  # 3    (floor division)
print(7 % 2)  # 1    (modulo)

# TODO: Calculate how many full weeks are in 100 days, and the remaining days


# =============================================================================
# 3. F-STRINGS (Python 3.6+)
# =============================================================================
print("\n--- 3. F-strings ---")

name = "Alice"
age = 30
pi = 3.14159

# Old ways (still valid but less readable):
# "Hello, %s" % name
# "Hello, {}".format(name)

# F-string:
print(f"Hello, {name}! You are {age} years old.")
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"10 + 5 = {10 + 5}")  # expressions work inside {}
print(f"{name!r}")  # !r calls repr(), !s calls str()
print(f"{name=}")  # Python 3.8+: prints name='Alice'

# TODO: Use an f-string to print a product's name, price (2 decimal places), and tax (8.5%)


# =============================================================================
# 4. TYPE HINTS
# =============================================================================
print("\n--- 4. Type Hints ---")


# Type hints are optional but improve readability and tooling support
def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def get_scores() -> list[int]:  # Python 3.9+: built-in generics
    return [95, 87, 72]


print(greet("Bob"))
print(add(3, 4))
print(get_scores())

# TODO: Write a typed function that takes a list of floats and returns their average


# =============================================================================
# 5. WALRUS OPERATOR := (Python 3.8+)
# =============================================================================
print("\n--- 5. Walrus Operator ---")

# Assigns AND returns a value in one expression — useful inside conditions/loops
numbers = [1, 3, 7, 2, 9, 4]

# Without walrus:
total = sum(numbers)
if total > 20:
    print(f"Total {total} is large")

# With walrus (assigns and checks in one line):
if (total := sum(numbers)) > 20:
    print(f"Total {total} is large (walrus)")

# Useful in while loops:
data = [4, 3, 1, 0, 7]
index = 0
while (value := data[index]) != 0:
    print(f"  value: {value}")
    index += 1

# TODO: Use walrus in a list comprehension to keep only words longer than 4 chars,
#       printing both the word and its length.
words = ["hi", "python", "code", "learn", "go"]

# =============================================================================
# 6. DATACLASSES (Python 3.7+)
# =============================================================================
print("\n--- 6. Dataclasses ---")

from dataclasses import dataclass, field


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass
class Student:
    name: str
    grades: list[int] = field(default_factory=list)  # mutable default

    def average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


p = Point(3.0, 4.0)
print(p)  # __repr__ for free
print(p.distance_from_origin())  # 5.0

s = Student("Alice", [90, 85, 92])
print(s)
print(f"Average: {s.average():.1f}")

# TODO: Create a dataclass `Product` with name (str), price (float), and in_stock (bool, default True)


# =============================================================================
# 7. PATHLIB
# =============================================================================
print("\n--- 7. Pathlib ---")

from pathlib import Path

# Modern, OO path handling — replaces os.path
current_file = Path(__file__)
print(f"This file:  {current_file}")
print(f"File name:  {current_file.name}")
print(f"Stem:       {current_file.stem}")
print(f"Suffix:     {current_file.suffix}")
print(f"Parent dir: {current_file.parent}")

project_root = current_file.parent
print(f"\nFiles in project:")
for f in project_root.iterdir():
    print(f"  {f.name}")

# Building paths safely (no more os.path.join):
config_path = project_root / "config" / "settings.json"
print(f"\nExample path: {config_path}")

# TODO: Check if README.md exists in the project root and print its size in bytes


# =============================================================================
# 8. MATCH STATEMENT (Python 3.10+)
# =============================================================================
print("\n--- 8. Match Statement ---")


def describe_type(value):
    match value:
        case int():
            return f"{value} is an integer"
        case str():
            return f'"{value}" is a string'
        case list():
            return f"A list with {len(value)} items"
        case None:
            return "Nothing here"
        case _:
            return f"Unknown type: {type(value)}"


print(describe_type(42))
print(describe_type("hello"))
print(describe_type([1, 2, 3]))
print(describe_type(None))


# Matching with structure:
def process_command(command: dict):
    match command:
        case {"action": "move", "direction": direction}:
            return f"Moving {direction}"
        case {"action": "shoot", "target": target}:
            return f"Shooting at {target}"
        case {"action": action}:
            return f"Unknown action: {action}"
        case _:
            return "Invalid command"


print(process_command({"action": "move", "direction": "north"}))
print(process_command({"action": "shoot", "target": "enemy"}))

# TODO: Write a match statement that categorizes an HTTP status code
#       (2xx -> "success", 3xx -> "redirect", 4xx -> "client error", 5xx -> "server error")


# =============================================================================
# 9. COMPREHENSIONS
# =============================================================================
print("\n--- 9. Comprehensions ---")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# List comprehension
squares = [x ** 2 for x in nums]
evens = [x for x in nums if x % 2 == 0]
print(f"Squares: {squares}")
print(f"Evens:   {evens}")

# Dict comprehension
square_map = {x: x ** 2 for x in range(1, 6)}
print(f"Square map: {square_map}")

# Set comprehension
unique_remainders = {x % 3 for x in nums}
print(f"Remainders mod 3: {unique_remainders}")

# Generator expression (lazy — no list built in memory)
total = sum(x ** 2 for x in range(1000))
print(f"Sum of squares 0–999: {total}")

# TODO: Using a dict comprehension, build a word-length map from this list:
sentence = "the quick brown fox jumps over the lazy dog".split()

# =============================================================================
# 10. GENERATORS AND YIELD
# =============================================================================
print("\n--- 10. Generators ---")


def count_up(start: int, stop: int):
    """Yields numbers one at a time — memory efficient."""
    current = start
    while current <= stop:
        yield current
        current += 1


for n in count_up(1, 5):
    print(f"  {n}", end="")
print()


def fibonacci():
    """Infinite Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
first_ten = [next(fib) for _ in range(10)]
print(f"Fibonacci: {first_ten}")

# TODO: Write a generator that yields only prime numbers up to a given limit


# =============================================================================
# 11. CONTEXT MANAGERS
# =============================================================================
print("\n--- 11. Context Managers ---")

import tempfile, os

# File I/O — the classic use case
with tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False) as f:
    f.write("line 1\n")
    f.write("line 2\n")
    tmp_path = f.name

# File is automatically closed after the with block
with open(tmp_path) as f:
    for line in f:
        print(f"  Read: {line}", end="")

os.unlink(tmp_path)  # clean up

# You can use multiple context managers in one line:
# with open("a.txt") as a, open("b.txt") as b:
#     ...

# TODO: Use contextlib.suppress to safely attempt to delete a file that may not exist
#       (instead of a try/except block)

fake_path = "/tmp/this_file_does_not_exist_xyz.txt"
# with suppress(...):
#     ...


# =============================================================================
# SUMMARY
# =============================================================================
print("\n--- Summary ---")
print("Topics covered:")
topics = [
    "print() as a function",
    "True division and floor division",
    "F-strings",
    "Type hints",
    "Walrus operator :=",
    "Dataclasses",
    "pathlib",
    "match statement",
    "Comprehensions (list, dict, set, generator)",
    "Generators and yield",
    "Context managers",
]
for i, topic in enumerate(topics, 1):
    print(f"  {i:2}. {topic}")
