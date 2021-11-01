import math
import os
import random
import re
import sys

#
# Complete the 'gameOfStones' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER n as parameter.
#

def gameOfStones(n):
    # Write your code here
    ganador=""
    if(jugadaoptima(n)!=0):
        ganador="P1 is the winner"
    else:
        ganador ="P2 is the winner"
    return ganador
def simulacion(n):
    intentos=0
    ganador=""
    while(ganador!="P1 is the winner" and ganador!="P2 is the winner"):
        jugada=jugadaoptima(n)
        if(jugada==0):
            if(n>5):
                jugada=5
            elif(n>3):
                jugada=3
            else:
                jugada=2
        print("Juega P"+str((intentos%2)+1) +" quitando "+ str(jugada)+" piedras")
        n=n-jugada
        if(n==1 or n==0):
            ganador=("P"+str((intentos%2)+1)+" is the winner")
        intentos+=1
    print(ganador)
def jugadaoptima(n):
    jugadabuena=0
    modulo=n%7
    if(modulo>=2 and modulo<=3):
        jugadabuena=2
    elif(modulo==4):
        jugadabuena=3
    elif(modulo>=5 and modulo<=6):
        jugadabuena=5
    return jugadabuena

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion5.txt', 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        result = gameOfStones(n)
        simulacion(n)
        fptr.write(result + '\n')

    fptr.close()