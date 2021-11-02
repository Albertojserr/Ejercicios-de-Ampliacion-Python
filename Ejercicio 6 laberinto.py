import math
import os
import random
import re
import sys


def exploracion(Casillax, Casillay, laberinto, n , m):
    num=0
    den=0
    probabilidad=0.0
    if(Casillax>0 and laberinto[Casillax-1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax-1][Casillay]=="%"):
            num+=1
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]!="#"):
        den +=1
        if(laberinto[Casillax+1][Casillay]=="%"):
            num+=1
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay+1]=="%"):
            num+=1
    if(Casillay>0 and laberinto[Casillax][Casillay-1]!="#"):
        den +=1
        if(laberinto[Casillax][Casillay-1]=="%"):
            num+=1
    if(den==0):
        return probabilidad
    probabilidad=num/den
    if(Casillax>0 and laberinto[Casillax-1][Casillay]=="$"):
        laberintocopia=laberinto
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(Casillax-1,Casillay, laberintocopia, n , m)/den
    if(Casillax<n-1 and laberinto[Casillax+1][Casillay]=="$"):
        laberintocopia=laberinto
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(Casillax+1,Casillay, laberintocopia, n , m)/den
    if(Casillay<m-1 and laberinto[Casillax][Casillay+1]=="$"):
        laberintocopia=laberinto
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=exploracion(Casillax,Casillay+1, laberintocopia, n , m)/den
    if(Casillay>0 and laberinto[Casillax][Casillay-1]=="$"):
        laberintocopia=laberinto
        laberintocopia[Casillax][Casillay]="#"
        probabilidad+=(exploracion(Casillax,Casillay-1, laberintocopia, n , m)/den)
    return probabilidad

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])
    laberinto=[]
    for n_itr in range(n):
        row = input()
        laberinto.append(list(row))
        # Write your code here


    probabilidad= exploracion(1,5,laberinto,n,m)
    print(probabilidad)
'''     for k_itr in range(k):
        second_multiple_input = input().rstrip().split()

        i1 = int(second_multiple_input[0])

        j1 = int(second_multiple_input[1])

        i2 = int(second_multiple_input[2])

        j2 = int(second_multiple_input[3]) '''

        # Write your code here
        # Write your code here

