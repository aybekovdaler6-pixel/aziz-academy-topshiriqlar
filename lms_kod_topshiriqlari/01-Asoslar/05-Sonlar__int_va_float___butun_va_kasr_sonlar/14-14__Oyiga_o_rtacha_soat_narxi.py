data = input().split()
total_salary = float(data[0])
hours_worked = float(data[1])
hourly_rate = total_salary / hours_worked
print(f"Hourly: {hourly_rate}")