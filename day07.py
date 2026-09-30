# Day 7 - Revision (Day 1 to Day 6)

print("=" * 40)
print("Day 1: Variables & Data Types")
print("=" * 40)

name = "Shaikh Khizar"
age = 24
height = 5.8
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")

print("\n" + "=" * 40)
print("Day 2: Input/Output")
print("=" * 40)

# Note: input() neeche comment out hai kyunki revision mein manual input nahi chahiye
# Uncomment karke test kar sakte ho
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}")

print("Input/Output concept revised")

print("\n" + "=" * 40)
print("Day 3: Numbers & Math")
print("=" * 40)

rate_per_kg = 50
weight_kg = 120
total_cost = rate_per_kg * weight_kg
print(f"Freight Cost: {total_cost}")

total_hours = 50
hours_per_day = 8
full_days = total_hours // hours_per_day
remaining =  total_hours % hours_per_day
print(f"Full days: {full_days}, Remaining: {remaining}")

print(f"BODMAS Test: {10 + 5 * 2}")
print(f"BODMAS with brackets: {(10 + 5) * 2}")

print("\n" + "=" * 40)
print("Day 4: Strings")
print("=" * 40)

full_name = "Shaikh Khizar"
print(f"Full Name: {full_name}")
print(f"Length: {len(full_name)}")
print(f"First char: {full_name[0]}")
print(f"Last char: {full_name[-1]}")
print(f"Upper: {full_name.upper()}")
print(f"Lower:  {full_name.lower()}")
print(f"Split: {full_name.split(' ')}")

tracking = "SHIP123456"
print(f"Tracking Prefix: {tracking[:4]}")
print(f"Tracking Number: {tracking[4:]}")

print("\n" + "=" * 40)
print("Day 5: Lists")
print("=" * 40)

shipments = ["SHIP001", "SHIP002", "SHIP003", "SHIP004"]
weights = [120, 85, 200, 150]

print(f"Shipments: {shipments}")
print(f"Total: {len(shipments)}")
print(f"First: {shipments[0]}")
print(f"Last: {shipments[-1]}")
print(f"First two: {shipments[:2]}")

shipments.append("SHIP005")
print(f"After append: {shipments}")

shipments.remove("SHIP002")
print(f"After remove: {shipments}")

weights.sort()
print(f"Sorted weights: {weights}")

print("\n" + "=" * 40)
print("Day 6: Loops")
print("="  * 40)

print("For Loop (range):")
for i in range(5):
    print(f" Number: {i}")

print("\nFor Loop (list):")
for s in shipments:
    print(f" Processing: {s}")

print("\nWhile Loop:")
count = 1
while count <= 3:
    print(f" Count: {count}")
    count = count + 1

print("\nLoop with Calculation:")
total_weight = 0
for w in weights:
    total_weight = total_weight + w
    print(f" Total Weight: {total_weight} kg")

print("\n" + "=" * 40)
print("REVISION COMPLETE - Alhamdulillah!")
print("=" * 40)
