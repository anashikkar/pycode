#Function to print all the lines in a file
def read_file():
    f = open('test1.txt','r')
    value = f.read()
    print("###This is read function")
    print value
    f.close()

#Function to append a line to the end of a file
def append_file():
    f = open('test1.txt','a')
    f.write("Text from append function")
    print("###This is write function")
    f.close()

#Function to read last line in file
def read_last_line():
    with open('test1.txt','r') as f:
        lines = f.read().splitlines()
        last_line = lines[-1]
        print("###This is Last line read function")
        print last_line

#Function to read till specific line number passed in a file
def line_read(x):
    with open('test1.txt','r') as f:
        counter = 0
        for line in f:
            print (line)
            counter = counter + 1
            if counter == x: return

#Function to count no of lines in a file
def line_count():
    count = 0
    for line in open('test1.txt','r'):
        count = count + 1

    print ("Total no of lines:",count)

#Function to read each line and append as a list
def list_append():
    demo_list = []
    with open('test1.txt','r') as f:
        for line in f:
            demo_list.append(line)
    print("List from text file is :",demo_list)
    return


read_file()
append_file()
read_last_line()
line_read(2)
line_count()
list_append()
