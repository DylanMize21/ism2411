# Reflection Questions

#1 It is suprising how lists work since in excel you start at 1 and looking up values in a list you start at 0. python allows you to also count backwards using negaative numbers.

#2 As I used to manage my pokemon collection tracking sets and prices using excel. Knowing how to use lists and tuples in python will allow me to create a better program to track my collection.




# Exercise 1
print("---Exercise 1: List practice ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
# Exercise 2
print("---Exercise 2: Index practice ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])
# Exercise 3
print("---Exercise 3: Slicing practice ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
print("---Exercise 4: modify ---")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)
# Exercise 5
print("---Exercise 5: tuple comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as e:
    print("type Error caught:", {e})
    print("tuples protect cordinates from being modified on accident")

# Exercise 6
print("---Exercise 6: avg list of sales ---")
sales = [100, 250, 75, 480, 200]
total_sales = sum(sales)
count_sales = len(sales)
avg_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)
print(f"Total: {total_sales} | Average: {avg_sales} | Best: {best_day} | Worst: {worst_day}")
# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    new_price = round(price * 0.9, 2)
    discounted.append(new_price)

    print(prices)
print(discounted)
# Exercise 8
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

        high_sales_count = len(high_sales)
        high_sales_avg = sum(high_sales) / high_sales_count
        print(f"{high_sales} | Count: {high_sales_count} | Avg: {high_sales_avg:.2f}")