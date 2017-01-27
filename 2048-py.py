#python2
#author: manhdcnguyen

from random import randint
import os, sys
import time

clear = lambda: os.system('clear')

def addMore():
    a = []
    b = []
    for i in range(0,37):
        a.append(0)
        b.append(0)
    size = 0
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] == 0:
                a[size] = i
                b[size] = j
                size += 1
    x = randint(0,size-1)
    y = randint(1,2)
    matrix[a[x]][b[x]] = 2 ** y

def printMatrix():
    for i in range(0,5):
        for j in range(0,5):
            if matrix[i][j] != 0:
                print "%4d" %matrix[i][j],
            else:
                print "   _",
        print

def sort(array):
    global point
    new_array = []
    for i in range(0,6):
        new_array.append(0)
    new_array_size = 0
    for i in range(0,5):
        if array[i] != 0:
            new_array[new_array_size] = array[i]
            new_array_size += 1
    for i in range(0,5):
        array[i] = new_array[i]
    for i in range(0,4):
        if array[i] == 0:
            break
        else:
            if array[i] == array[i + 1]:
                array[i] = array[i] * 2
                array[i + 1] = 0
                point += array[i] / 2
                for j in range(i + 1, 4):
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
    return array

def turnDown():
    for i in range(0,5):
        array_size = 0
        array = []
        for j in range(6):
            array.append(0)
        for j in reversed(range(0,5)):
            array[array_size] = matrix[j][i]
            array_size += 1
        array = sort(array)
        array_size = 0
        for j in reversed(range(0,5)):
            matrix[j][i] = array[array_size]
            array_size += 1

def turnUp():
    for i in range(0,5):
        array_size = 0
        array = []
        for j in range(0,5):
            array.append(0)
            array_size = 0
        for j in range(0,5):
            array[array_size] = matrix[j][i]
            array_size += 1
        array = sort(array)
        array_size = 0
        for j in range(0,5):
            matrix[j][i] = array[array_size]
            array_size += 1

def turnLeft():
    for i in range(0,5):
        array = []
        for j in range(0,5):
            array.append(0) #gan 0 cho toan bo mang.
        array_size = 0
        for j in range(0,5): #doc nguoc tu 5 ve 0.
            array[array_size] = matrix[i][j]
            array_size += 1
        array = sort(array)
        array_size = 0
        for j in range(0,5):
            matrix[i][j] = array[array_size]
            array_size += 1

def turnRight():
    for i in range(0,5):
        array = []
        for j in range(0,5):
            array.append(0)
        array_size = 0
        for j in reversed(range(0,5)):
            array[array_size] = matrix[i][j]
            array_size += 1
        array = sort(array)
        array_size = 0
        for j in reversed(range(0,5)):
            matrix[i][j] = array[array_size]
            array_size += 1

def setRandom():
    x = randint(0,4)
    y = randint(0,4)
    z = randint(1,3)
    matrix[x][y] = 2 ** z

weight, height = 5, 5 # chieu cao, chieu rong cua mang
matrix = [[0 for x in range(weight)] for y in range(height)] #khai bao mang.

for i in range(0,3):
    setRandom()

t = 0
point = 0
printMatrix()

while t == 0:
    navi = raw_input() #bien dieu khien huong
    if navi == "s":
        turnDown()
    elif navi == "w":
        turnUp()
    elif navi == "a":
        turnLeft()
    elif navi == "d":
        turnRight()
    elif navi == "x":
        break
    addMore()
    clear()
    printMatrix()
    print "Your point: %d"%point
