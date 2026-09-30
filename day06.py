# Day 6 - Loops

# 1. For Loop with range
print("For Loop with range:")
for i in range(5):
    print(i)

# 2. For Loop with range (start, end)
print("\nFor Loop 1 to 5:")
for i in range(1, 6):
    print(i)

# 3. For Loop with List
print("\nShipments:") 
shipments = ["SHIP001", "SHIP002", "SHIP003"]
for s in shipments:
    print(f"Processing: {s}")

# 4. For Loop with Numbers
print("\nWeights:")
weights = [120, 85, 200]
for w in weights:
    print(f"Weights: {w} kg")

# 5. While Loop
print("\nWhile Loop:")
count = 1
while count <= 3:
    print(f"Count: {count}")
    count = count + 1

# 6. Loop with Calculation
print("\nTotal weight:")
weights = [120, 85, 200]
total = 0
for w in weights:
    total = total + w
print(f"Total: {total} kg")
