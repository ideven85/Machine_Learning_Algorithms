import datetime


def convert_to_string(time: datetime.datetime):
    month = time.month
    day = time.day
    year = time.year
    return str(month) + "/" + str(day) + "/" + str(year)


def main():
    time = datetime.datetime.now()
    print(convert_to_string(time))


if __name__ == "__main__":
    main()
