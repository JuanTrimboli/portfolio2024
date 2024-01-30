""" Follow these steps:
● Imagine you are running a cafe. Create a new Python file in your folder
called cafe.py.
● Create a list called menu, which should contain at least four items sold in
the cafe.
● Next, create a dictionary called stock, which should contain the stock
value for each item on your menu.
● Create another dictionary called price, which should contain the prices for
each item on your menu.
● Next, calculate the total_stock worth in the cafe. You will need to
remember to loop through the appropriate dictionaries and lists to do
this.
Tip: When you loop through the menu list, the 'items' can be set as keys
to access the corresponding 'stock' and 'price' values. Each 'item_value' is
calculated by multiplying the stock value by the price value. For example:
item_value = (stock[items] * price[items])
● Finally, print out the result of your calculation """

#T This is a simple version on the task requested.
cafe_menu = []

# Append individual lists to cafe_menu
cafe_menu.append(['croissants', 'muffins', 'shortbread', 'cookies', 'cakes'])  # pastries
cafe_menu.append(['latte', 'cappuccino', 'tea', 'americano', 'chai', 'matcha'])  # beverages
cafe_menu.append(['soy milk', 'oat milk', 'almond milk'])  # milk types

# Now you can access the individual lists using indices
a = cafe_menu[0]  # pastries
b = cafe_menu[1]  # beverages
c = cafe_menu[2]  # milk types

stock_levels = {a[0] : 15, a[1]: 12, a[2]: 8, a[3]: 4, a[4]: 7,
                b[0]: 100, b[1]: 120, b[2]: 35, b[3]: 158, b[4]: 22, b[5]: 82,
                c[0]: 150, c[1]: 200, c[2]: 200}
items_price = {a[0] : 3.50, a[1]: 2.75, a[2]: 1.25, a[3]: 2.25, a[4]: 6.50,
                b[0]: 4.50, b[1]: 5, b[2]: 3.25, b[3]: 3.50, b[4]: 5.35, b[5]: 6.15,
                c[0]: 0.5, c[1]: 0.75, c[2]: 0.75}

# Calculate total_stock worth in the cafe
total_stock_worth = 0
for item in stock_levels:
    item_value = stock_levels[item] * items_price[item]
    total_stock_worth += item_value
    
# Print out the result of the calculation
print("Total stock worth in the cafe: $", round(total_stock_worth, 2))



#If I had to create a smarter version, it'd be similar to the example with the grades:

cafe_menu = []

# Append individual lists to cafe_menu
cafe_menu.append(['croissants', 'muffins', 'shortbread', 'cookies', 'cakes'])  # pastries
cafe_menu.append(['latte', 'cappuccino', 'tea', 'americano', 'chai', 'matcha'])  # beverages
cafe_menu.append(['soy milk', 'oat milk', 'almond milk'])  # milk types

# Prices for each item in the menu
current_prices = {cafe_menu[0][0]: 3.50, cafe_menu[0][1]: 2.75, cafe_menu[0][2]: 1.25, cafe_menu[0][3]: 2.25, cafe_menu[0][4]: 6.50,
                 cafe_menu[1][0]: 4.50, cafe_menu[1][1]: 5, cafe_menu[1][2]: 3.25, cafe_menu[1][3]: 3.50, cafe_menu[1][4]: 5.35, cafe_menu[1][5]: 6.15,
                 cafe_menu[2][0]: 0.5, cafe_menu[2][1]: 0.75, cafe_menu[2][2]: 0.75}

# Dictionaries for stock levels and prices
stock_levels = {}
price_for_items = {}

# Set prices
for item in cafe_menu[0] + cafe_menu[1] + cafe_menu[2]:
    price_for_items[item] = current_prices[item]

# Input stock levels for each item
for item_list in cafe_menu:
    for item in item_list:
        stock = int(input(f"Enter stock level for {item}: "))
        stock_levels[item] = stock

# Display current prices
print("\nCurrent Prices:")
for item, price in price_for_items.items():
    print(f"{item}: £{price}")

# Allow the user to modify prices
modify_prices = input("\nDo you want to modify prices? (yes/no): ").lower()
if modify_prices == 'yes':
    item_to_change = input("Enter the item you want to change the price for: ")
    if item_to_change in price_for_items:
        new_price = float(input(f"Enter new price for {item_to_change} in pounds: "))
        price_for_items[item_to_change] = round(new_price, 2)
    else:
        print("Invalid item. Price not modified.")

# Calculate total_stock worth in the cafe
total_stock_worth = sum(stock_levels[item] * price_for_items[item] for item_list in cafe_menu for item in item_list)

# Print out the result of the calculation
print("\nTotal stock worth in the cafe: £", round(total_stock_worth, 2))