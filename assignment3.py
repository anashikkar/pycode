list_of_number = [5,100,29,8,9,102]

def largest_number(x):
    largest = 0
    length = len(x)
    count = 0
    while (count < length) :
        if x[count] > largest:
            #If loop to assign largest index value to var
            largest = x[count]
        count = count + 1
    return(largest)
print ("Largest no from list is {}".format(largest_number(list_of_number)))
