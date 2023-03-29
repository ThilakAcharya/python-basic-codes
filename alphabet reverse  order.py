n = 64
i =1
j =1
while i <= n:
    while j<= n-i:
        print((chr)(n-j+i+64)+" ")
        j+=1
    i+=1
    
'''for i in range(1,n):
    for j in range(1, n-i):
        print((chr)(n-i+j+64)+ " ")
'''
        
