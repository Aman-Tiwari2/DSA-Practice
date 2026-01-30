n = [1, 2, 3, 4, 5] 
m = [1, 2, 3, 6, 7]
e = []

i, j = 0, 0

while i < len(n) and j < len(m):
    if n[i] <= m[j]:
        if len(e) == 0 or e[-1] != n[i]:
            e.append(n[i])
        i += 1
    else:
        if len(e) == 0 or e[-1] != m[j]:
            e.append(m[j])
        j += 1
        
        
while i < len(n):
    if len(e) == 0 or e[-1] != n[i]:
        e.append(n[i])
    i += 1
    
while j < len(m):
    if len(e) == 0 or e[-1] != m[j]:
        e.append(m[j])
    j += 1
    



print(e)
        