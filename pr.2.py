import math
a=int(input('Introduceti un numar: '))
if len(str(a))<=70:
    n=math.sqrt(a)
    m=int(n)
    print(m)
    print(a-(m**2))
else:
    print ('eroare')
