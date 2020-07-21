#!/usr/local/bin/python3

def nested_list(students):
    second_highest =sorted(list(set([marks for name,marks in students])))[1]
    return ('\n'.join([a for a,b in students if b==second_highest]))

if __name__ =='__main__':
    students = [['Harhs', 20], ['beria', 20], ['Varun', 19], ['kakunami', 19], ['Vikas', 21]]
   
    #students = [['Harry', 37.21], ['Berry', 37.21]]
    print(nested_list(students))

