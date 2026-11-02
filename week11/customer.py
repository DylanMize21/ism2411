print("---Exercise 1 --- ")
customer = {
    "name" : "Alice",
    "email" : "alice@example.com",
    "tier" : "Gold",
    "ytd_spend" : 12400
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("---Exercise 2 --- ")
customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'Platinum'
print(customer)
del customer['name']

print(customer.get('ytd_spend',0))


print("---Exercise 3 --- ")
print(customer.get("email", "no email on file"))

print("---Exercise 4 --- ")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("---Exercise 5 --- ")

tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}


customer_tier = "platinum"  
purchase_amount = 200

discount_rate = tier_discounts.get(customer_tier, 0)

discount_amount = purchase_amount * discount_rate
final_price = purchase_amount - discount_amount

print(f"Tier: {customer_tier}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")

print("---Exercise 6 --- ")

tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "gold", "ytd_spend": 1200},
    {"name": "Bob", "email": "bob@example.com", "tier": "bronze", "ytd_spend": 250},
    {"name": "Charlie", "email": "charlie@example.com", "tier": "platinum", "ytd_spend": 3400}
]

purchase_amount = 300

for customer in customers:
    name = customer["name"]
    tier = customer["tier"]
    
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = purchase_amount * discount_rate

    print(f"Customer: {name} | Tier: {tier.capitalize()} | Discount on ${purchase_amount}: ${discount_amount:.2f}")

    print("---Exercise 7 --- ")
    catalog = {
        "widget A": {"price": 9.99, "stock": 150},
        "gadget C": {"price": 49.99, "stock": 8}
    }

    for product_name, product_details in catalog.items():
        if product_details["stock"] < 20:
            print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")

            print("---Exercise 8 --- ")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
    {"region": "East", "amount": 450},
    {"region": "North", "amount": 100}
]

region_summary = {}

for tx in transactions:
    region = tx["region"]
    amount = tx["amount"]
    
    region_summary[region] = region_summary.get(region, 0) + amount

print("Sales Summary by Region:")
for region in sorted(region_summary.keys()):
    print(f"{region}: ${region_summary[region]:.2f}")