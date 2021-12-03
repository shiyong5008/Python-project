# NEU CS5001 week8 project 7 lsystem.py version 1
# Yong Shi/shi.yong@northeastern.edu/NUID 001578845

import sys

# returns an empty L-system
def init():
    return ['', []]

# returns the base string of the L-system
def getBase( lsys ):
    return lsys[0]

# sets the L-system base string
def setBase( lsys, base ):
    lsys[0] = base

# adds the rule to the L-system
def addRule( lsys, rule ):
    lsys[1].append( rule )

# returns the rule at position index in the L-system
def getRule( lsys, index ):
    return lsys[1][index]


# def main():
#     my_lsys = init()
#     setBase(my_lsys, 'A')
#     addRule(my_lsys, ['A', 'AB'])
#     print(my_lsys)
#     print("the base is ", getBase(my_lsys))
#     print("the first rule is ", getRule(my_lsys, 0))
#
# if __name__ == '__main__':
#     main()


def createLsystemFromFile( filename ):
    """ Create an L-system list by reading in the specified file """
    # assign to lsys the result of calling the function init()
    my_lsys=init()

    # assign to fp the result of opening the file (use open(filename, "r") )
    fp=open(filename,"r")

    # assign to lines the result of calling fp.readlines()
    lines=fp.readlines()

    # close the file using the close method of the file object held in fp
    fp.close()

    # for each line in the list lines
    for line in lines:
        # assign to line the result of calling line.strip()
        strip_line=line.strip()
        # print(strip_line) # test
        # assign to words the result of calling line.split(' ')
        words=strip_line.split(' ')
        # print(words) # test
        # if the first item in words is equal to 'base'
        if words[0]=='base':
            # use the setBase function passing in the second item in words as the new base string
            setBase(my_lsys,words[1])
        # else if the first item in words is equal to 'rule'
        elif words[0]=='rule':
            # use the addRule function passing in all but the first item in words as the new rule
            addRule(my_lsys,words[1:])
  # return the L-system list lsys
    return my_lsys


# def main(argv):
#     # check if there are enough command-line arguments
#     if len(argv) < 2:
#         print("Usage : python3 lsystem.py <lsystem filename>")
#         exit()
#
#     # code to test reading from a file
#     lsys_filename = argv[1]
#     lsys = createLsystemFromFile(lsys_filename)
#     print(lsys)
#
# if __name__ == '__main__':
#     main(sys.argv)


def buildString( lsys, n ):
    """ Return a string generated by applying the L-system rules n times"""
    # assign to a local variable (e.g. nstring) the result of getBase(lsys)
    nstring=getBase(lsys)
    # assign to a local variable (e.g. rule) the result of getRule(lsys, 0)
    rule=getRule(lsys,0)
    # assign to a local variable (e.g. symbol) the first element of rule
    symbol=rule[0]
    # assign to a local variable (e.g. replacement) the second element of rule
    replacement=rule[1]
    # loop n times
    for i in range(n):
        # assign to nstring, the result of nstring.replace( symbol, replacement )
        nstring=nstring.replace(symbol,replacement)
    # return nstring
    return nstring


def main(argv):
    if len(argv) < 3:
        print("Usage : python3 lsystem.py <in_filename> <num_iterations>")
        exit()

    lsys_filename = argv[1]
    lsys = createLsystemFromFile(lsys_filename)
    print(lsys)

    num_iter = int(argv[2])
    s = buildString(lsys, num_iter)
    print(s)

if __name__ == "__main__":
    main(sys.argv)