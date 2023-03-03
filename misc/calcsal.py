import sys

def calc_sal(hourly_rate, hours = 40, weeks=52):
	return hours*weeks*hourly_rate

def get_hourly_rate():
	user_hourly_rate = float(input("Enter the hourly rate of the job: "))

	while user_hourly_rate <= 0:
		print("Error: The hourly rate must be positive!")
		user_hourly_rate = get_hourly_rate()

	return user_hourly_rate

def main():
	try:
		hourly_rate = float(sys.argv[1])
	except IndexError:
		hourly_rate = get_hourly_rate()

	salary = calc_sal(hourly_rate)	
	print("An hourly rate of ${}/hr equates to an approximate annual salary of ${:,.2f}".format(hourly_rate, salary))

if __name__ == '__main__':
	main()