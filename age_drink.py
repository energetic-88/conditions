age = input("Скільки Вам років? ")
if age.isdigit() == True:
    age_integer = int(age)
    if age_integer < 14:
        print ('Ваша вікова група - діти. \nВам рекомендується випити - молоко.')
    elif 14 <= age_integer < 18:
        print ('Ваша вікова група - тінейджери. \nВам рекомендується випити - кока-колу.')
    elif 18 <= age_integer < 21:
        print ('Ваша вікова група - молодь. \nВам рекомендується випити - пиво.')
    else:
        print ('Ваша вікова група - дорослі. \nВам рекомендується випити - віскі.')
else:
    print ('Ваш вік має визначатись цілим числом, яке відповідає Вашим повним рокам.')