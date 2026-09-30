# Day 4 - Strings

# Basic Strings
name = "Khizar Shaikh"
print(f"Name: {name}")
print(f"Lenght: {len(name)}")

# Indexing
print(f"First char: {name[0]}")
print(f"Last char: {name[-1]}")

# Slicing
print(f"First name: {name[:6]}")
print(f"Last name: {name[7:]}")

# Methods
print(f"Upper: {name.upper()}")
print(f"Lower: {name.lower()}")
print(f"Title: {name.title()}")
print(f"Count 'a': {name.count('a')}")
print(f"Find 'y': {name.find('y')}")


# Split#
parts = name.split(" ")
print(f"Parts: {parts}")

# Logistics Example
tracking = "SHIP123456"
print(f"\nTracking ID: {tracking}")
print(f"Prefix: {tracking[:4]}")
print(f"Number: {tracking[4:]}")