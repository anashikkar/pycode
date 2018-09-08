import sys


USAGE = '''
Please pass a valid argument to the script
USAGE : <script_name> <filename> <mode> <type>
'''
def input_arguments(*args):
    for arg in args:
        print ("Argument passed is ",args)

try:
    if len(sys.argv) <= 1:
        sys.exit()
    else:
        args = ("hey", 14, "joey")
        input_arguments(args)
        print ("Else condition executed")
        print ("Total no of arguments is ",len(args))
except:
    print ('')
    print(sys.stderr, USAGE)
    sys.exit()
