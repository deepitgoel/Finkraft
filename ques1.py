#Write a Python program that finds the longest common substring between two strings.
def common(A,B):
    m = len(A)
    n=  len(B)
    longest = 0
    cnt = [ [0] * (n+1) for x in range(m+1)]
    common_set = set()
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                c = cnt[i][j] + 1
                cnt[i+1][j+1] = c
                if c > longest:
                    common_set = set()
                    longest = c
                    common_set.add(A[i-c+1:i+1])
                elif c == longest:
                    common_set.add(A[i-c+1:i+1])
    return common_set
