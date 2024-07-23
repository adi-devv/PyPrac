units_consumed = float(input("Enter the units of electricity consumed: "))

if units_consumed <= 100:
    cost = 0.0
elif units_consumed <= 200:
    cost = (units_consumed - 100) * 2.55
elif units_consumed <= 300:
    cost = 100 * 2.55 + (units_consumed - 200) * 3.55
elif units_consumed <= 400:
    cost = 100 * 2.55 + 100 * 3.55 + (units_consumed - 300) * 5.55
else:
    cost = 100 * 2.55 + 100 * 3.55 + 100 * 5.55 + (units_consumed - 400) * 6.55

print(f"The estimated electricity bill is Rs. {cost:.3f}")