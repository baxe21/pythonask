import math



n=input('Enter the integer you wish to find the prime factors of: ')

n = int(float(n))
L=[]

def too_small():
       
        L.append(n)
        if n>0:
                L.append(1)
        return L

if n < 4: 
        L = too_small()
        print(*L, sep="*")
        exit()

if n == 4: 
        L.append(2)
        L.append(2)
        print(*L, sep="*")
        exit()

def primefactor():
        
        test=True
        b=n
        while(test):
                i=2
                while((b%i!=0)&(i<(b/2))): 
                        i=i+1
                if i>(b/2):
                        L.append(b)
                        L.append(1)
                        test=False
                else: 
                        a=(b/i)
                        L.append(i)
                        b=a
        return L

L = primefactor()

print(L)
print(*L, sep="*")

exit()