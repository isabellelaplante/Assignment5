def compute_seed(student_key):
    return sum(ord(ch) for ch in student_key.strip())

def get_valid_name(prompt):
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")

def get_valid_price(prompt):
    while True:
        try:
            price = float(input(prompt).strip())
            if price > 0:
                return price
            print("Price cannot be negative or zero. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the price.")

def get_valid_quantity(prompt):
    while True:
        try:
            quantity = int(input(prompt).strip())
            if quantity > 0:
                return quantity
            print("Quantity must be greater than or equal to one. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer for the quantity.")


student_key = input("Enter your student key: ")
seed = compute_seed(student_key)

subtotal = 0.0
units = 0

while True:
    item_name = input("Enter item name (or 'DONE' to finish): ").strip()

    if item_name.upper() == "DONE":
        break

    if item_name == '':
        print("Item name cannot be empty. Please try again.")
        continue

    item_price = get_valid_price("Enter item price: ")
    item_quantity = get_valid_quantity("Enter item quantity: ")
    
    subtotal += item_price * item_quantity
    units += item_quantity

if units >= 10 or subtotal >= 100:
    discount_percentage = 10
else:
    discount_percentage = 0

discount_amount = subtotal * discount_percentage / 100
total = subtotal - discount_amount

if seed % 2 == 1:
    total -= 3.00
    perk ="YES"
else:   
    perk = "NO"

if total < 0:
    total = 0.0

print(f"Seed: {seed}")
print(f"Units: {units}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: {discount_percentage}%")
print(f"Perk applied: {perk}")
print(f"Total: ${total:.2f}")
