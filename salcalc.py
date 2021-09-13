import sys

def calc_sal(hourly_rate, hours = 40):
	weeks = 52
	return hours*weeks*hourly_rate

hourly_rate = int(sys.argv[1])
#hourly = int(input("Enter the number hourly rate of the job: "))
salary = calc_sal(hourly_rate)	

print(f"An hourly rate of ${hourly_rate}/hr equates to an approximate annual salary of ${salary}")
