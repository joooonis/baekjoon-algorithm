import sys

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline()))    
    
def merge(S1,S2,S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort(S):
    n = len(S)
    if n < 2:
        return
    # divide
    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]
    # qonquer (with recursion)
    merge_sort(S1)
    merge_sort(S2)
    # merge results
    merge(S1,S2,S)


merge_sort(lst)
for i in lst:
    print(i)
