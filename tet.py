from random import randint
import os
import time

clear = lambda: os.system('clear')

matrix = [[1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6], [1,2,3,4,5,6]]
array = [1,2,3,4,5,6]
a = [1,2,3,4,5,6]

def sort():
    count = 0
    temp_array = [0,0,0,0,0,0]
    for inx in range(0,6):
        if array[inx] != 0:
            temp_array[count] = array[inx]
            count = count + 1
    for inx in range(0, 6):
        array[inx] = temp_array[inx]
    for inx in range(0,5):
        if array[inx] == 0:
            break
        if array[inx] == array[inx + 1]:
            array[inx] = array[inx] * 2
            array[inx + 1] = 0
            for inx1 in range(inx + 1, 5):
                temp = array[inx1]
                array[inx1] = array[inx1 + 1]
                array[inx1 + 1] = temp

def turnDown():
    for i in range(0, 6):
        for j in range(0, 6):
            a[j] = matrix[j][i]
        t = 0
        for j in reversed(range(0,6)):
            array[t] = a[j]
            t = t + 1
        sort()
        t = 0
        for j in reversed(range(0,6)):
            a[t] = array[j]
            t = t + 1
        for j in range(0, 6):
            matrix[j][i] = a[j]

def turnUp():
    for i in range(0, 6):
        for j in range(0, 6):
            array[j] = matrix[j][i]
        sort()
        for j in range(0, 6):
            matrix[j][i] = array[j]

def turnLeft():
    for i in range(0, 6):
        for j in range(0, 6):
            array[j] = matrix[i][j]
        sort()
        for j in range(0, 6):
            matrix[i][j] = array[j]

def turnRight():
    for i in range(0, 6):
        for j in range(0, 6):
            a[j] = matrix[i][j]
        t = 0
        for j in reversed(range(0, 6)):
            array[t] = a[j]
            t = t + 1
        sort()
        t = 0
        for j in reversed(range(0,6)):
            a[j] = array[t]
            t = t + 1
        for j in range(0, 6):
            matrix[i][j] = a[j]

def makeRand():
    i = randint(0,5)
    j = randint(0,5)
    make = randint(0,1)
    if make == 0:
        matrix[i][j] = 2
    else:
        matrix[i][j] = 4

def Intro():
    print "2048 made by manhdcnguyen."
    print "Press w to turn up, s to turn down, a to turn left, d to turn right."
    print "Keep alive as long as you could."
    time.sleep(2)
    clear()
    print "Are you ready?"
    print "Let start!"
    time.sleep(1)
    clear()

def printMatrix():
    for i in range(0, 6):
        for j in range(0, 6):
            if matrix[i][j] != 0:
                print "%4d" %matrix[i][j],
            else:
                print "   _",
        print

Intro()

for i in range(0, 6):
    for j in range(0, 6):
        matrix[i][j] = 0

for index in range(0, 8):
    makeRand()

clear()
printMatrix()

t = 0
z = 0

def fillRad():
    count = 0
    hor = []
    ver = []
    for i in range(37):
        hor.append(0)
        ver.append(0)
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 0:
                hor[count] = i
                ver[count] = j
                count = count + 1
    x = randint(0,count-1)
    y = randint(0,count-1)
    x = hor[x]
    y = ver[y]
    matrix[x][y] = 2

while t == 0:
    navi = raw_input()
    if navi == "w":
        temp = 0
        turnUp()
    elif navi == "s":
        temp = 0
        turnDown()
    elif navi == "a":
        temp = 0
        turnLeft()
    elif navi == "d":
        temp = 0
        turnRight()
    elif navi == "x":
        break
    clear()
    fillRad()
    printMatrix()
