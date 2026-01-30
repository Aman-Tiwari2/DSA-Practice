# Here we print number from 1 TO N using HEAD RECURSION print value in incremental order 

def printNumber(i, n):
    if i > n:
        return
    
    print(i, end=" ")
    printNumber(i+1, n)

printNumber(1, 4)


# Here we print number from 1 TO N using TAIL RECURSION it will reverse the value

def printNumber(i, n):
    if n == 0:
        return
    
    
    printNumber(i+1,n-1 )
    print(n, end=',')

printNumber(1, 5)



