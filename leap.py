# read day month year
day=int(input("enter the day from 1 (1-31)"))
month=int(input("enter the month(1-12)"))
year=int(input("enter the year"))

#display the dmy

print("entered date:{day:02d}-{month:02d}-{year}")
#check leap year

if(year % 4==0 and year % 100 !=0) or (year  % 400==0):
    print(f"the year{year} is a leap year.")
else:
    print(f"the year {year} is not a leap year.")


