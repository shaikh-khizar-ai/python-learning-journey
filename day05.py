# Day 5 - Lists

# 1. List Banana
shipments = ["SHIP001", "SHIP002", "SHIP003", "SHIP004"]
weights = [120, 85, 200, 150]

# 2. Basic Info
print(f"Shipments: {shipments}")
print(f"Total: {len(shipments)}")

# 3. Indexing
print(f"First: {shipments[0]}")
print(f"Last: {shipments[-1]}")

# 4. Slicing
print(f"First two: {shipments[:2]}")
print(f"Last two: {shipments[-2:]}")

# 5. Append
shipments.append("SHIP005")
print(f"After append: {shipments}")

# 6. Remove
shipments.remove("SHIP002")
print(f"After remove: {shipments}")

# 7. Sort
weights.sort()
print(f"Sorted weights: {weights}")

# 8. Reverse
weights.reverse()
print(f"Reversed: {weights}")

# 9. Mixed Data
shipment_info = ["SHIP001", 120, "Mumbai", 2500.50]
print(f"\nShipment Info: {shipment_info}")
print(f"ID: {shipment_info[0]}")
print(f"Weight: {shipment_info[1]}")
print(f"City: {shipment_info[2]}")

# 10. Loop (Dhyan se - alag lines mein)
print("\nAll shipments:")
for s in shipments:
    print(f"- {s}")