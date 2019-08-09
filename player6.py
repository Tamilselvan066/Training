from collections import Counter
def is_isomorphic(y,s):
    t_counts = list(Counter(y).values())
    t_counts.sort()
    s_counts = list(Counter(s).values())
    s_counts.sort()
    if t_counts == s_counts:
        return 'yes'
    return 'no'
t,s=input().split()
print(is_isomorphic(t,s))
