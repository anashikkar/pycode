def list_input():
  l = raw_input("Enter list of numbers")
  number = map(int,l.split(' '))
  return(number)


no = list_input
print(no)
