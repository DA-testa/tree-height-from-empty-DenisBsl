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
    input_type = input()

    if 'I' in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)
        print(height)
    elif 'F' in input_type:
        filename = input()
        with open("test/" + filename, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            height = compute_height(n, parents)
            print(height)
    else:
        print("Invalids")
        exit()

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))