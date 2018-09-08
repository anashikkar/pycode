#File to show list of numbers divisible by 7 and not multiple of 5 between 200 and 300


def division(x,y):
    list = []
    while x < y:
        x = x + 1
        if ( x % 7 == 0) and ( x % 5 != 0 ):
            list.append(x)
    return list

print(division(200,300))
