import sys

def calc_sal(hourly_rate, hours = 40):
	weeks = 52
	return hours*weeks*hourly_rate

try:
	hourly_rate = float(sys.argv[1])
except IndexError:
	hourly_rate = float(input("Enter the hourly rate of the job: "))
finally:
	salary = calc_sal(hourly_rate)	

print("An hourly rate of ${}/hr equates to an approximate annual salary of ${:,.2f}".format(hourly_rate, salary))
