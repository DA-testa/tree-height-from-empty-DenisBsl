# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    max_height = 0
    print(n)
    return max_height


def main():
    data = input()
    match data[0]:
        case "F":
            data = input()
            with open(data) as f:
                n = f.readline()
                parents = map(int, f.readline().split(" "))
        case "I":
            n = input()
            parents = map(int, input().split(" "))
        case _:
            return
    
    compute_height(n, parents)

    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))