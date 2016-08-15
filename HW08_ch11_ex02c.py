#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    key_list = []
    for k in d:
    	if str(d[k]) == v:
    		key_list.append(k)
    return key_list


###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_new(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt', 'r') as f:
        pledge_list = f.read().split()
    return pledge_list

pledge_histogram = histogram_new(get_pledge_list())

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
    print(reverse_lookup_new(pledge_histogram, "1"))
    print(reverse_lookup_new(pledge_histogram, "9"))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
