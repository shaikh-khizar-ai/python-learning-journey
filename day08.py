# Day 8 - Functions (Basics)

# 1. Simple Function
def greet():
    print("Assalamualaikum")

greet()
greet()

# 2. Function with Parameter
def greet_name(name):
    print(f"Hello, {name}")

greet_name("Zayn")
greet_name("Ammi")

# 3. Function with Multiple Parameters
def freight_cost(rate, weight):
    total = rate * weight
    print(f"Freight Cost: {total}")

freight_cost(50, 120)
freight_cost(80,200)

# 4. Function with Listv
def show_shipments(shipments):
    for s in shipments:
        print(f"Processing: {s}")

my_shipments = ["SHIP001", "SHIP002", "SHIP003"]
show_shipments(my_shipments)