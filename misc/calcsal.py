import sys

def calc_sal(hourly_rate, hours = 40, weeks=52):
	return hours*weeks*hourly_rate

def get_hourly_rate():
	user_hourly_rate = float(input("Enter the hourly rate of the job: "))
	if user_hourly_rate > 0:
		return user_hourly_rate
	else:
		print("Error: The hourly rate must be positive!")
		return get_hourly_rate()

try:
	hourly_rate = float(sys.argv[1])
except IndexError:
	hourly_rate = get_hourly_rate()
finally:
	salary = calc_sal(hourly_rate)	

print("An hourly rate of ${}/hr equates to an approximate annual salary of ${:,.2f}".format(hourly_rate, salary))

if __name__ == '__main__':
	main()