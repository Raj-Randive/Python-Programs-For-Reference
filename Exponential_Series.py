import math
x=int(input('Input any number: '))
a=int(input('No. of terms?: '))
z=0
for i in range(a):
    z+=x**i/math.factorial(i)
print(z)



