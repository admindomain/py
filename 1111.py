import string
import random

a=string.ascii_uppercase
b=string.digits
c=list(a+b)

def activation_code(place):
    s=""
    i=0
    while i < place:
        s=s+random.choice(c)
        i=i+1
    print (s)

for i in range(10):
    activation_code(20)



import string
import random

a=string.ascii_uppercase
b=string.digits
c=list(a+b)

def ctivation_code(num,place):
    s=""
    i=0
    j=0
    code=set()
    while j < num:
        s=""
        i=0
        while i < place: #for i in range(place):
            s=s+random.choice(c)
            i=i+1
        if s not in code:
            code = code | {s}
            print (s)
            j=j+1

ctivation_code(5,10)
