#Self-Assessment Questions
#1  The first bug I spotted was by reading the error message and checking my code. This helped me understand how to find mistakes and debug my code.
#2 The apply_discount(price, tier) function takes a price and a customer tier. It checks the tier and returns the price after the correct discount. A colleague could use it by entering the price and tier without needing to read the whole function.
#3 I used ChatGPT to help explain Python functions, discounts, and variable scope. The AI helped me understand how the code works, but I still needed to run and test the code myself.

#Exercise 1

def calculate_tax(price, rate):
    return price * rate

# call function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax 1: ${tax1:.2f}")
print(f"Tax 2: ${tax2:.2f}")
print(f"Tax 3: ${calculate_tax(350, 0.05):.2f}")
#Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # Apply 20% discount
    elif tier == "silver":
        return price * 0.9  # Apply 10% discount
    elif tier == "bronze":
        return price * 0.95  # Apply 5% discount
    else:
        return price  # No discount

original_price = 200.00
for tier in ["gold", "silver", "bronze", "none"]:
    print(f'tier: {tier}, ${apply_discount(original_price, tier):.2f}')

#Exercise 3
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f'final_price(200, 0.07,"gold"): ${final_price(200, "gold", 0.07):.2f}')
#Exercise 4
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
rate = 0.07

for price, tier in orders:
    total = final_price(price, tier, rate)
    print(f'Order: ${price:.2f}, Tier: {tier}, Total: ${total:.2f}')
#Exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
#Exercise 6
x = 100 #global x
def double_it():
    x=999 #local x
    return x * 2
print (x)
print (double_it())
print (x)
# I believe it will run 100, 1998, 100 because the local variable x inside the function double_it() does not affect the global variable x. The function returns the value of the local x multiplied by 2, which is 999 * 2 = 1998. The global x remains unchanged at 100.
