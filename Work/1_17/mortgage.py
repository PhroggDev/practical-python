# mortgage.py
#
# Exercise 1.17
# Using f-strings
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    total_paid += payment

print(f"Total paid: {total_paid:0.2f}")
