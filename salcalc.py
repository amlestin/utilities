import sys

def calc_sal(hourly_rate, hours = 40):
	weeks = 52
	return hours*weeks*hourly_rate

try:
	hourly_rate = int(sys.argv[1])
except IndexError:
	hourly_rate = int(input("Enter the hourly rate of the job: "))
finally:
	salary = calc_sal(hourly_rate)	

# TODO: format as currency
print(f"An hourly rate of ${hourly_rate}/hr equates to an approximate annual salary of ${salary}")
