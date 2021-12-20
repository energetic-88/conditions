def my_function(*tuple_, list_=None):

    for i in tuple_:
        list_.append(i)
    list_2 = []
    sum_ = 0
    for num in list_:
        if num % 2 == 1:
            sum_ = sum_ + num
            list_2.append(num)
    return sum_/len(list_2)