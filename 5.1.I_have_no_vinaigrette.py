import datetime
import random
import numpy


def pick_random_date_in_range(first_date, last_date):
    """
     Returns a random date between first_date and last_date.
    :param first_date: The first date in the range.
    :param last_date: The last date in the range.
    :return: A random date between first_date and last_date.
    """
    first_date, last_date = (first_date, last_date) if first_date <= last_date else (last_date, first_date)
    random_epoch_time = random.choice(numpy.arange(first_date.timestamp(), last_date.timestamp()))
    return datetime.datetime.fromtimestamp(random_epoch_time)


def main():
    """
    Gets two dates from the user and prints a message if the random date is a Monday.
    """
    date_1_str, date_2_str = input("Enter 2 dates in the following format: YYYY-MM-DD\n").split()
    date_1 = datetime.datetime.strptime(date_1_str, '%Y-%m-%d')
    date_2 = datetime.datetime.strptime(date_2_str, '%Y-%m-%d')
    random_date = pick_random_date_in_range(date_1, date_2)
    if random_date.weekday() == 0:
        print("I have no vinaigrette!")


if __name__ == "__main__":
    main()
