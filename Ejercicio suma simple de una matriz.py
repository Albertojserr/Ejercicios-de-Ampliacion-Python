import math
import os
import random
import re
import sys
#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    # Write your code here
    suma=0
    for i in ar:
        suma= suma+i
    return suma

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'] + 'solucion1.txt', 'w')
    print("Escribe el tamaño")
    ar_count = int(input().strip())
    print("Escribe los números separados por espacio")
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()

