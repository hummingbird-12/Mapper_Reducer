#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

inp = stdin.readlines()
parseList = [] # input parse list

matMap = {} # map matrix char to number
matDim = [] # matrix dimension list
matList = [] # matrix list
matCnt = 0 # matrix count

# parse input and figure out matrix dimensions
for line in inp:
    parse = line.strip('\n').split(',')
    if parse[0] not in matMap: # new matrix found
        matMap[parse[0]] = matCnt
        matCnt += 1
        matDim.append({"rowSize" : 0, "colSize" : 0})

    # parse each field
    curMat = matMap[parse[0]]
    curRow = int(parse[1])
    curCol = int(parse[2])
    curVal = float(parse[3])

    # store parse
    parseList.append({"index" : curMat, "row" : curRow, "col" : curCol, "val" : curVal})

    # figure out matrix dimensions
    if matDim[curMat]["rowSize"] < curRow + 1 :
        matDim[curMat]["rowSize"] = curRow + 1
    if matDim[curMat]["colSize"] < curCol + 1 :
        matDim[curMat]["colSize"] = curCol + 1

# create space for matrix and initialize
for index in range(matCnt):
    matList.append([]) # list for matrix
    for row in range(matDim[index]["rowSize"]):
        matList[index].append([]) # list for row
        for col in range(matDim[index]["colSize"]):
            matList[index][row].append(0.0) # fill with 0

# fill in matrix
for entry in parseList:
    matList[entry["index"]][entry["row"]][entry["col"]] = entry["val"]

# output mapper result
for matIdx in range(len(matList)):
    for rowIdx in range(matDim[matIdx]["rowSize"]):
        for colIdx in range(matDim[matIdx]["colSize"]):
            val = matList[matIdx][rowIdx][colIdx]
            if val == 0: # skip for 0
                continue
            if matIdx == 0: # for first matrix
                for mulTime in range(matDim[1]["colSize"]):
                    stdout.write("%d,%d\t%c,%d,%.1f\n" %(rowIdx, mulTime, 'A', colIdx, val))
            else: # for second matrix
                for mulTime in range(matDim[0]["rowSize"]):
                    stdout.write("%d,%d\t%c,%d,%.1f\n" %(mulTime, colIdx, 'B', rowIdx, val))
