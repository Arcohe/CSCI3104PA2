from __future__ import print_function
# in case you wish to use python2, but I strongly prefer that you use python3
import sys
import random

# NAME: Thomas Trieu
# STUDENT ID NUMBER: 103013414
# On my honor as a University of Colorado Boulder student, I have not received any unauthorized help.
# I also realize that plagiarizing code defeats the purpose of an assignment like this and that the
# instructors and TAs have very sophisticated approaches to finding such plagiarism that can defeat
# things like renaming variables or rearranging statements.
#
# Acknowledged By: Thomas Trieu


def free_time_intervals(interval_lst, T):
    sortedLst = sorted(interval_lst, key=lambda x:x[0])
    freetime = []
    start = 0;
    end = 0;
    #Processes each tuple, finding 'blocks' during which there are users logged in
    for i in range(len(interval_lst)):
        #If u_i is greater than or equal to T
        if (start >= T or end >= T):
            break
        if (end < sortedLst[i][0]):
            if (sortedLst[i][0] < T):
                freetime.append((end, sortedLst[i][0]))
            else:
                freetime.append((end, T))
        start = sortedLst[i][0]
        if (end < sortedLst[i][1]):
            end = sortedLst[i][1]
    if (end < T):
        freetime.append((end, T))
    return freetime

def max_logged_in(interval_lst,T):
    count = 0
    maxNum = 0
    maxTime = 0
    DecoupledLst = []
    for i in range(len(interval_lst)):
        DecoupledLst.append(('i', interval_lst[i][0]))
        DecoupledLst.append(('d', interval_lst[i][1]))
    DecoupledLst.sort(key=lambda x:x[1])
    for j in range(len(DecoupledLst)):
        if (DecoupledLst[j][1] > T):
            break
        if (DecoupledLst[j][0] == 'i'):
            count += 1
        else:
            count -= 1
        if (count > maxNum):
            maxNum = count
            maxTime = DecoupledLst[j][1]
    return (maxNum, maxTime)


if __name__ == '__main__':
    #Test Cases

    lst1 = [(5,15)]
    print('Input:', lst1)
    print(free_time_intervals(lst1,30))
    print(max_logged_in(lst1,30))

    lst2 = [(1,3), (2,8),(3,6), (2,6), (10,15), (12,17), (19,23), (27,35)]
    print('Input (corner-case):', lst2)
    print(free_time_intervals(lst2,30))
    print(max_logged_in(lst2,30))

    lst3 = [(5,15), (18,25), (3,12), (4, 11), (1,15), (18,19)]
    print('Input:', lst3)
    print(free_time_intervals(lst3,30))
    print(max_logged_in(lst3,30))
