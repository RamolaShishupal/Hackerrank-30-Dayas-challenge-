
n=int(input())
for j in range(n):
    j=input()
    def king(j):
        k=""
        d=""
        for i in range(len(j)):
            if i%2==0:
                k=k+j[i]
            else:
                d=d+j[i] 
        print(k+" "+d)
    king(j)
