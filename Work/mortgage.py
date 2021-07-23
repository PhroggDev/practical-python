# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
mos = 0

extra_payment = 1000
extra_payment_strt_mo = 61
extra_payment_end_mo = 108

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment
    mos += 1

    if mos >= extra_payment_strt_mo and mos <= extra_payment_end_mo:
        principal -= extra_payment
        total_paid += extra_payment
    print("Month: " + str(mos) + " TotalPaid: " + str(round(total_paid, 2)) +
          "PrincipalRemaining: " + str(round(principal, 2)))

print("Total paid: ", round(total_paid, 2))
# print("It took " + str(months) + " months to payoff loan")
