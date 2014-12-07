#!/usr/bin/env python

"""A python script that takes inputted integers and returns the mean, median and mode."""

__author__      = "@RyanDahlke"
__copyright__   = "GNU GPL v2.0"

#   )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\  )\
#  (  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \(  \

lst = []
get_num = True
while get_num:
    lst.append(int(input("Please enter number.\n")))
    check = True
    while check:
        more_num = input("Enter more numbers?(y/n)\n")
        if more_num == 'y':
            check = False
        elif more_num == 'n':
            check = False
            get_num = False
        else:
            print("Invalid Response.")
print("\nRaw data:", lst)
lst.sort()
print("Sorted data:", lst)


def get_mean(list):
    return float(sum(list)/len(list))


def get_median(list):
    median_pos = (len(list)+1)/2
    if median_pos == int(median_pos):
        median_pos = int(median_pos-1)  #-1 for of list indexing
        return list[median_pos]
    else:
        med_avg = []
        med_avg.append(list[int(median_pos-1.5)])  #-1.5 for list indexing
        med_avg.append(list[int(median_pos-.5)])  #-.5 for list indexing
        return get_mean(med_avg)


def get_mode(list):
    mode_lst = []
    highest = 0
    for i in list:
        if list.count(i) > list.count(highest) and list.count(i) != 1:
            highest = i
    for i in list:
        if list.count(i) == list.count(highest) and mode_lst.count(i) < 1:
            mode_lst.append(i)
    return mode_lst


print("Mean:", get_mean(lst))
print("Median:", get_median(lst))
print("Mode:", get_mode(lst))