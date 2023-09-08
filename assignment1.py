"""
### Assignment 1
#### Calculation of Simple Interest
The simple interest formula is I = P*r*t where I = the amount of interest, P is the principal or the amount invested, r is the interest rate per year (converted to a decimal) and t is the length of time in years.
Write a program that calculates the amount of simple interest for an investment.

Criteria:
Your program should ask the user for 
* an initial investment
* the annual interest rate as a percentage
* the length of time.
  * the user should have the option of entering in the length of time in years, months or days
* The program will calculate the amount of interest earned and display it.
* Appropriate formatting of the output is a requirement for this assignment
"""
a = int(input ("Enter your initial investment "))
b = int(input ("Enter your interest rate as a percentage "))
b = (b/100)
c = int(input("Enter the length of investment "))
d = str(input("Years, Months, or Days? "))
if d == "Months":
  c = (c/12)
  print(f"{a}*{b}*{c} = {a*b*c}$")
elif d == "Days":
    c = (c/365)
    print(f"{a}*{b}*{c} = {a*b*c}$")
elif d == "Years":
      print(f"{a}*{b}*{c} = {a*b*c}$")