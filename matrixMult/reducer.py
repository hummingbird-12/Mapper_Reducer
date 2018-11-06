#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

inp = stdin.readlines()
reduce = {} # entries for each index

# parse input and separate into index
for line in inp:
    parse = line.strip('\n').split('\t')
    index = parse[0] # index in result matrix
    val = parse[1]

    if index not in reduce:
        reduce[index] = [] # empty list
    reduce[index].append(val) # append entry

# calculate result for each index
for index in reduce:
    match = {} # match multiplication order
    for entry in reduce[index]:
        parse = entry.split(',')
        curMat = parse[0] # matrix character
        curOrd = int(parse[1]) # multiplication order
        curVal = float(parse[2]) # value

        if curOrd not in match:
            match[curOrd] = []
        match[curOrd].append(curVal) # append value

    # calculate result
    result = 0.0
    for entry in match:
        if len(match[entry]) == 1: # no multiplier
            continue
        result += match[entry][0] * match[entry][1]

    stdout.write("%s,%.1f\n" %(index, result))
