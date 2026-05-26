# Task 2 - Smart Bill Splitter

bill_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage (e.g. 10 for 10%): "))

# Arithmetic operations using +, -, *, /, %
tip_amount = bill_amount * (tip_percentage / 100)   # * and /
total_with_tip = bill_amount + tip_amount            # +
amount_per_person = total_with_tip / num_people      # /
remaining_cents = round((total_with_tip % 1) * 100)  # %
discount = bill_amount - tip_amount                  # - (just to use operator)

amount_per_person = round(amount_per_person, 2)
tip_amount = round(tip_amount, 2)
total_with_tip = round(total_with_tip, 2)

print("\n")
print("=" * 35)
print("       🧾  BILL SPLIT SUMMARY")
print("=" * 35)
print(f"  Bill Amount     : ₹{bill_amount}")
print(f"  Tip ({tip_percentage}%)       : ₹{tip_amount}")
print(f"  Total with Tip  : ₹{total_with_tip}")
print(f"  Number of People: {num_people}")
print(f"  Each Person Pays: ₹{amount_per_person}")
print("=" * 35)
