try:   
    galons = float(input("Введіть кількість галонів для заправки - "))
    money = float(input("Введіть суму за один галон в долларах США - "))
except: 
    print('Введіть, будь-ласка, число.')

if galons < 2:
    print ('Загальна вартість:', round(galons * money, 2), 'центів.')
elif 2 <= galons < 4:
    print ('Загальна вартість:', round(galons * money - 0.05, 2), 'центів.')
elif 4 <= galons < 6:
    print ('Загальна вартість:', round(galons * money - 0.1, 2), 'центів.')
elif 6 <= galons < 8:
    print ('Загальна вартість:', round(galons * money - 0.15, 2), 'центів.')
elif 8 <= galons < 10:
    print ('Загальна вартість:', round(galons * money - 0.2, 2), 'центів.')
else:
    print('Загальна вартість:', round(galons * money - 0.25, 2), 'центів.')