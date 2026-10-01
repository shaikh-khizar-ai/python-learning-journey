# Day 12 - Nested Dictionaries

# 1. Creating a Nested Dictionary
shipments = {
    "SHIP001": { "origin": "Mumbai", "destination": "Dubai", "weight": 120, "status": "Delivered" },
    "SHIP002": { "origin": "Delhi", "destination": "London", "weight": 85, "status": "In Transit" },
    "SHIP003": { "origin": "Chennai", "destination": "Singapore", "weight": 200, "status": "Delivered" }
}

print("=" * 40)
print("1. All Shipments")
print("=" * 40)
print(shipments)

# 2. Accessing Specific Values
print("\n" + "=" * 40)
print("2. Specific Access")
print("=" * 40)
print(f"SHIP001 Origin: {shipments['SHIP001']['origin']}")
print(f"SHIP002 Weight {shipments['SHIP002']['weight']} kg")
print(f"SHIP003 Destination: {shipments['SHIP003']['destination']}")

# 3. Updating Values in Nested Dictionary
print("\n" + "=" * 40)
print("3. Update Value")
print("=" * 40)
shipments["SHIP002"]["status"] = "Delivered"
print(f"SHIP002 New Status: {shipments['SHIP002']['status']}")

# 4. Adding New Key in Nested Dictionary
shipments["SHIP001"]["delay"] = 2
print(f"SHIP001 Delay: {shipments['SHIP001']['delay']} days")

# 5. Loop Through Nested Dictionary
print("\n" + "=" * 40)
print("5. Loop Through Shipments")
print("=" * 40)
for ship_id, details in shipments.items():
    print(f"\n{ship_id}:")
    for key, value in details.items(): print(f" {key}: {value}")

# 6. Filtering Data with Logic
print("\n" + "=" * 40)
print("6. Delivered Shipments")
print("=" * 40)
for ship_id, details in shipments.items():
    if details["status"] == "Delivered":
        print(f" {ship_id} - {details['origin']} to {details['destination']}")

# 7. Calculating Total Weight
print("\n" + "=" * 40)
print("7. Total Weight")
print("=" * 40)
total_weight = 0
for ship_id, details in shipments.items():
    total_weight = total_weight + details["weight"]
    print(f"Total Weight: {total_weight} kg")