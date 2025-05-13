print("=== Personal Budget Tracker ===")

# Step 1: Get income
income = float(input("Enter your monthly income: "))

# Step 2: Get expenses
rent = float(input("Enter your rent expense: "))
food = float(input("Enter your food expense: "))
transport = float(input("Enter your transport expense: "))
entertainment = float(input("Enter your entertainment expense: "))

# Step 3: Calculate totals
total_expenses = rent + food + transport + entertainment
remaining = income - total_expenses
savings_percentage = (remaining / income) * 100

# Step 4: Display results
print("\n=== Monthly Summary ===")
print("Total expenses:", total_expenses)
print("Remaining balance:", remaining)
print("You saved", round(savings_percentage, 2), "% of your income this month.")
