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




