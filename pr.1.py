s=str(input('Introduceti un sir de caractere: '))
a,b=s.split()
print(a)
print(b)
x=a.title()
y=b.title()
if ((x==a) and (y==b)):
    print('numele este corect')
else:
    print('numele nu este corect')
