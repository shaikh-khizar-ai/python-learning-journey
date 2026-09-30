# Day 9 - Function with Return

# 1. Function with Return
def add(a, b):
    return a + b

result = add(5, 10)
print(f"Sum: {result}")

# 2. Return value Use Karna
def multiply(a, b):
    return a * b

total = multiply(5, 4) + 10
print(f"Total: {total}")

# 3. Function with Return + Condition
def check_delay(actual_days, estimated_days):
    if actual_days > estimated_days:
        return "Delayed"
    else:
        return "On Time"

status = check_delay(10, 7)
print(f"Status: {status}")

# 4. Function Returning Multiple Values
def shipment_info(shipment_id, weight, rate):
    cost = weight * rate
    return shipment_id, cost

sid, cost = shipment_info("SHIP001", 120, 50)
print(f"Shipment: {sid}, Cost: {cost}")