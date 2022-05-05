expenses = [10.50, 8, 5, 15, 20, 5, 3]
sum = 0

for x in expenses:
   sum = sum + x

print(f"You spent ${sum} this week on lunch.")

expenses = [10.50, 8, 5, 15, 20, 5, 3]
total = sum(expenses)

print(f"You spent ${total} this week on lunch.")

for i in range(7):
   print(i)

total = 0
expenses=[]
for i in range(7):
   expenses.append(float(input("Enter an expense.")))
total = sum(expenses)
print(f"You spent ${total}.")

total = 0
expenses=[]
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
   expenses.append(float(input("Enter an expense.")))
total = sum(expenses)
print(f"You spent ${total}.")