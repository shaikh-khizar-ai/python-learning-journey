# Day 10 - Functions Advanced

# 1. Print vs Return
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(5, 10) # Sirf dikhata
result = add_return(5, 10) # Wapas deta
print(f"Return Result: {result}")

# 2. Multiple Parameters
def auto_fare(distance, rate, wait_time):
    total = (distance * rate) + (wait_time * 2)
    return total

fare = auto_fare(10, 15, 5)
print(f"Fare: ₹{fare}")

# 3. Default Parameters
def chai_banao(cups, sugar=2):
    print(f"{cups} cup chai, {sugar} chamach cheeni")

chai_banao(2)  # Default sugar = 2
chai_banao(3, 1)  # Sugar = 1

# 4. Real Logistics Example
def shipment_summary(shipment_id, weight, rate, distance, currency="INR"):
    freight = rate * weight
    transport = distance * 2
    total = freight + transport
    return f"{shipment_id}: {currency} {total}"

print(shipment_summary("SHIP001", 120, 50, 300))
print(shipment_summary("SHIP002", 200, 80, 500, "USD"))