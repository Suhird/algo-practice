#!/usr/local/bin/python3

def insert(result,v):
    elem = v[0]
    pos = v[1]
    result.insert(elem,pos)

def remove(result,v):
    elem = v[0]
    result.remove(elem)

def append(result,v):
    result.append(v[0])

def pop(result):
    result.pop()

def sort(result):
    result.sort()

def reverse(result):
   result.reverse()

def main_func(cmd_dict):
    result = []
    for k in cmd_dict:
        if k[0]=='insert':
            insert(result, k[1])
        elif k[0]=='print':
            print(result)
        elif k[0]=='remove':
            remove(result,k[1])
        elif k[0]=='append':
            append(result,k[1])
        elif k[0]=='sort':
            sort(result)
        elif k[0]=='pop':
            pop(result)
        elif k[0]=='reverse':
            reverse(result)

if __name__ == '__main__':
    N = int(input())
    cmd_dict = []
    for _ in range(N):
        temp = []
        cmds,*lines = input().split()
        args = list(map(int,lines))
        temp = [cmds,args]
        cmd_dict.append(temp)
   # cmd_dict = {'insert': [0, 6], 'print': [], 'remove': [6], 'append': [1], 'sort': [], 'pop': [], 'reverse': []}
    main_func(cmd_dict)
