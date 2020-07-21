#!/usr/local/bin/python3


def calc_avg(students,query_name):
    result ='{0:2f}'.format(sum(students[query_name])/3)
    return round


if __name__ == '__main__':
    n = int(input())
    students= {}
    for _ in range(n):
        name,*line = _.split()
        marks = list(map(float,line))
        students[name] = marks
    query_name = input()
    

