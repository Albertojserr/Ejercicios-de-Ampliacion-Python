
#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(0,n):
        linea=""
        for k in range(0,n-1-i):
            linea=linea + " "
        for j in range(0,i+1):
            linea = linea + "# "
        print(linea)

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)