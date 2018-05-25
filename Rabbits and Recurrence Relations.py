# Rosalid
# Bioinformatics Stronghold
# ID: FIB

# Given: Positive integers n≤40 and k≤5.

# Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each
# generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).

# n = month k = rabbit pairs
def recurrence(n,k):

    f1 = 1
    f2 = 1

    i = 3

    while i <= n:
        fn = f2 + (f1*k)
        f1 = f2
        f2 = fn
        i+=1

    return fn


print(recurrence(34, 4))
