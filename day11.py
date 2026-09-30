# Day 11 - Dictionaries

# 1. Dictionary Banana
shipment = {"id": "SHIP001", "weight": 120, "city": "Mumbai", "cost": 2500}
print("=" * 30)
print("1. Dictionary")
print("=" * 30)
print(shipment)

# 2. Value Access Karna (Key se)
print("\n" + "=" * 30)
print("2. Value Access")
print("=" * 30)
print(f"ID: {shipment['id']}")
print(f"Weight: {shipment['weight']} kg")
print(f"City: {shipment['city']}")
print(f"Cost: ₹{shipment['cost']}")

# 3. Value Badalna
print("\n" + "=" * 30)
print("3. Value Update")
print("=" * 30)
shipment["weight"] = 150
print(f"New Weight: {shipment['weight']} kg")

# 4. New Key Add Karna
print("\n" + "=" * 30)
print("4. New Key Add")
print("=" * 30)
shipment["status"] = "Delivered"
print(f"Status: {shipment['status']}")
print(f"Full Dict: {shipment}")

# 5. Keys, Values, Items
print("\n" + "=" * 30)
print("5. Keys / Values / Items")
print("=" * 30)
print(f"Keys: {shipment.keys()}")
print(f"Values: {shipment.values()}")

# 6. Loop Through Dictionary
print("\n" + "=" * 30)
print("6. Loop")
print("=" * 30)
for key, value in shipment.items():
    print(f" {key}: {value}")

# 7. List of Dictionary (Real Logistics)
print("\n" + "=" * 30)
print("7. List of Dictionaries")
print("=" * 30)

shipments = [{"id": "SHIP001", "weight": 120, "city": "Mumbai"}, {"id": "SHIP002", "weight": 85, "city": "Dubai"}, {"id": "SHIP003", "weight": 200, "city": "London"}]
print("\nAll Shipments:")
for s in shipments:
    print(f" {s['id']} - {s['city']} ({s['weight']} kg)")

# 8. Specific Shipment Access
print("\n" + "=" * 30)
print("=" * 30)
print(f"First Shipment ID: {shipments[0]['id']}")
print(f"Second Shipment City: {shipments[1]['city']}")
print(f"Third Shipment Weight: {shipments[2]['weight']} kg")

# 9. Total Weight Calculate
print("\n" + "=" * 30)
print("9. Total Weight")
print("=" * 30)
total_weight = 0
for s in shipments:
    total_weight = total_weight + s["weight"]
    print(f"Total Weight: {total_weight} kg")