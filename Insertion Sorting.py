def InsertionSort(L):
    i=1
    while(i<len(L) ):
        if L[i-1]>L[i]:
            L[i],L[i-1]=L[i-1],L[i]
            for j in range(i-1,-1,-1):
                if(j>=1):
                    if (L[j - 1] > L[j]):
                        L[j], L[j - 1] = L[j - 1], L[j]
                    else:
                        break
                else:
                    break
            i+=1
        else:
            i+=1
    return L
L=list(map(int,input().split()))
print(InsertionSort(L))



