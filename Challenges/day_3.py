"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: ₹1200  
People: Aman, Neha, Ravi

Each person owes: ₹400

Final output:
  Aman owes ₹400  
  Neha owes ₹400  
  Ravi owes ₹400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

num_people = int(input("How many people are in your group? "))

name_str = input("Enter the name of each person, separated by a comma (ex: John, Craig, Amare): ")
names = name_str.split(",")

total_bill = float(input("Enter the total bill amount: "))

amount_per_person = total_bill / num_people

print("*" * 20)
for name in names:
    print(f"* {name.strip()} owes ${amount_per_person:.2f} *")
print("*" * 20)

