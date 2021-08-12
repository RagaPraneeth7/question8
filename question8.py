t = int(input())                        # read number of test cases                      
for i in range(t):                      # for each element i in range 0 and testcases         
    a,b,N = map(int,input().split())    # read and map inputs a,b,n
    
    if(N%2==0):                         # if n is even, print floor division of max and min of a,b
        print(max(a,b)//min(a,b))       
    else:                               # else, print floor division of max and min of a*2,b
        print(max(a*2,b)//min(a*2,b))   