def calc_sal(hourly_rate, hours = 40):
	weeks = 52
	return hours*weeks*hourly_rate


hourly = int(input("Enter the number hourly rate of the job: "))
salary = calc_sal(hourly)	

print(f"An hourly rate of ${hourly}/hr equates to an approximate annual salary of ${salary}")
