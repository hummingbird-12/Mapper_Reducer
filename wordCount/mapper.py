#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout
line = stdin.readline()

while line != "":
    for word in line.strip("\n\r").replace("\t", " ").split(" "):
        stdout.write("%s\t1\n" % word)
    line = stdin.readline()
