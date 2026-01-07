#2.pyramid pattern of letter 'A'
for i in range(1, 6):
    print("A" * i)

#3.pyramid pattern of letter 'A' in reverse
for i in range(6, 0, -1):
    print("A" * i)

#4.pyramid pattern of first 5 letters()
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()
#
for i in range(5):
    print("ABCDE"[:i+1])
    
#5.pyramid pattern of first 5 letters(A,BB,CCC..)
n=5
p=65
for i in range(n):
    for j in range(i+1):
        print(chr(p), end="")
    p+=1
    print()

#6.pyramid pattern of first 5 letters(A,ABA,ABCBA..)
n=5
p=65
for i in range(n):
    for j in range(i,n):
        print(" ",end="")

    for j in range(i+1):
        print(chr(p+j),end="")
    
    for j in range(i-1,-1,-1):
        print(chr(p+j),end="")
    print()
