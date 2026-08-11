A = int(input())
B = int(input())
C = int(input())

if (A+B) < B:
    print(1)

elif A < B < C:
    print(1)

else:
    if A < B or B < C:
     print(2)
    else:
       print(3)

