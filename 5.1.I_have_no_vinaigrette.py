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
    first_date, last_date = min(first_date, last_date), max(first_date, last_date)
    random_epoch_time = random.choice(numpy.arange(first_date.timestamp(), last_date.timestamp()))
    return datetime.datetime.fromtimestamp(random_epoch_time)


def main():
    """
    Gets two dates from the user and prints a message if the random date is a Monday.
    """
    first_date, last_date = input("Enter 2 dates in the following format: YYYY-MM-DD\n").split()
    first_date = datetime.datetime.strptime(first_date, '%Y-%m-%d')
    last_date = datetime.datetime.strptime(last_date, '%Y-%m-%d')
    random_date = pick_random_date_in_range(first_date, last_date)
    if random_date.weekday() == 0:
        print("I have no vinaigrette!")


if __name__ == "__main__":
    main()
