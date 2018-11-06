#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

res = {}
entry = stdin.readline()

while entry != "":
    word = entry.strip("\t1\n")
    if word not in res:
        res[word] = 0
    res[word] += 1
    entry = stdin.readline()

for key in res:
    stdout.write("%s\t%d\n" %(key, res[key]))
