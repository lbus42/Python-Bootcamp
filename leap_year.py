year = int(2018)

year = int(year)


print(year)

if year % 4 == 0:

    if year % 100 == 0:
        # Not a leap year, unless special case
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
