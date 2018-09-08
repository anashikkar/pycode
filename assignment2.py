def even_odd(x):
    return(x % 2)

num = input("Enter number to compare if even or odd: ")
x = even_odd(num)
if x == 0:
    print ("Number is even {}".format(num))
else:
    print ("Number is Odd {}".format(num))
