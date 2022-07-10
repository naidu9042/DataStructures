def selectionSort(L):
    for i in range(len(L)-1):
        min=L[i]
        flag = 0
        for j in range(i+1,len(L)):
            if(min>L[j]):
                min=L[j]
                temp=j
                flag=1
        if flag==1:
            L[i],L[temp]=min,L[i]
    return L
L=[-2, 45, 0, 11, -9]
print(selectionSort(L))