print("choose the thing on which bases you want calculate the time \n 1. hour \n 2. minute \n 3. seconds \n 4. days \n 5. years")
choose = input("Enter your Choice ",)
if choose == "1":
    h = int(input("Enter hours: "))
    print('HOURS =', h)
    print('MINUTES =', h * 60)
    print('SECONDS =', h * 60 * 60)
    print('DAYS =', int(h / 24))
    print('YEARS =', int(h / 8760))
elif choose == "2":
    m = int(input("Enter minutes: "))
    print('HOURS =', int(m/60))
    print('MINUTES =', m)
    print('SECONDS =', m * 60)
    print('DAYS =', int(m / 1440))
    print('YEARS =', int(m / 525600))
elif choose == "3":
    s = int(input("Enter seconds: "))
    print('HOURS =', int(s / 3600))
    print('MINUTES =', int(s/60))
    print('SECONDS =', s)
    print('DAYS =', int(s / 86400))
    print('YEARS =', int(s / 31536000))
elif choose == "4":
    d = int(input("Enter days: "))
    print('HOURS =', (d*24))
    print('MINUTES =', d*24*60)
    print('SECONDS =', d*24*60*60)
    print('DAYS =', d)
    print('YEARS =', int(d / 365))
elif choose == "5":
    y = int(input('Enter years: '))
    print('HOURS =', y*365*24)
    print('MINUTES =', y*365*24*60)
    print('SECONDS =', y * 365*24*60*60)
    print('DAYS =', y*365)
    print('YEARS =', y)
else:
    print("Invalid Choose")





