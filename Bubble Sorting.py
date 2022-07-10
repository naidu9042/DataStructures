def bubbleSort(L):
   Sorted = 0
   for i in range(len(L)):
       for j in range(len(L)-1):
           if L[j]>L[j+1]:
               L[j],L[j + 1]=L[j+1],L[j]
               Sorted=1
       if Sorted!=1:
           return L
   return L

L=list(map(int,input().split()))
print(bubbleSort(L))
