name = input("What is your name? ").strip().title()
hourly_wage = input("What is your hourly wage? ")
hours_worked = input("How many hours have you worked? ")

earnings = float(hourly_wage) * float(hours_worked)

print(f"{name} earned ${earnings} this week")

# Below formatting prints in $XXX.00 format
print(f"{name} earned ${earnings:.2f} this week")

