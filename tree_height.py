# python3
# #221RDB188 Deniss Buslajevs 8. grupa

import sys
import threading

def mx_height(node, max_height, parents):
    nd = None
    for i in range(len(parents)):
        if parents[i] == node:
            if nd == node:
                max_height = max_height - 1
            nd = node
            max_height = max(mx_height(i, max_height+1, parents), max_height)
    return max_height

def compute_height(n, parents):
    rootnode = 0
    for i in range(n):
        if parents[i] == -1:
            rootnode = i

    max_height = mx_height(rootnode, 1, parents)
    return max_height


def main():
    text = input().strip().upper()
    if text == "I":
        n = int(input())
        parents_str = input().strip()
        parents = list(map(int, parents_str.split()))
        height = compute_height(n, parents)
    elif text == "F":
        file_name = "test/" + input().strip()
        if "a" in file_name:
            return
        try:
            with open(file_name, 'r') as file:
                n = int(file.readline().strip())
                parents_str = file.readline().strip()
                parents = list(map(int, parents_str.split()))
                height = compute_height(n, parents)
        except FileNotFoundError:
            return
    else:
        return

    print(height)


    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))