import sys
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def calc_sal(hourly_rate: float, weekly_hours: float, yearly_work_weeks: int) -> float:
	return weekly_hours*yearly_work_weeks*hourly_rate

def prompt_user_for_hourly_rate() -> float:
	user_hourly_rate = float(input("Enter the hourly rate of the job: "))
	while user_hourly_rate <= 0:
		logger.error("Error: The hourly rate must be positive!")
		user_hourly_rate = get_hourly_rate()
	return user_hourly_rate

def get_hourly_rate() -> float:
	try:
		hourly_rate = float(sys.argv[1])
	except IndexError:
		hourly_rate = prompt_user_for_hourly_rate()
	return hourly_rate

def prompt_user_for_yearly_work_weeks() -> int:
	user_yearly_work_weeks = int(input("Enter the number of work weeks in a year: "))
	while user_yearly_work_weeks <= 0:
		logger.error("Error: The number of work weeks in a year must be positive!")
		user_yearly_work_weeks = get_yearly_work_weeks()

	return user_yearly_work_weeks

def get_yearly_work_weeks() -> int:
	try:
		yearly_work_weeks = int(sys.argv[2])
	except IndexError:
		yearly_work_weeks = prompt_user_for_yearly_work_weeks()
	return yearly_work_weeks

def prompt_user_for_weekly_hours() -> float:
	user_weekly_hours = float(input("Enter the number of hours worked per week: "))
	while user_weekly_hours <= 0:
		logger.error("Error: The number of hours worked per week must be positive!")
		user_weekly_hours = get_weekly_hours()
	return user_weekly_hours

def get_weekly_hours() -> float:
	try:
		weekly_hours = float(sys.argv[3])
	except IndexError:
		weekly_hours = prompt_user_for_weekly_hours() 
	return weekly_hours

def main() -> None:
	hourly_rate: float = get_hourly_rate()
	yearly_work_weeks: int = get_yearly_work_weeks()
	weekly_hours: float = get_weekly_hours()

	salary: float = calc_sal(hourly_rate, weekly_hours, yearly_work_weeks)	
	print("An hourly rate of ${}/hr with an average weekly hours of {} hours per week, and {} work weeks, equates to an approximate annual salary of ${:,.2f}".format(hourly_rate, weekly_hours, yearly_work_weeks, salary))

if __name__ == '__main__':
	main()