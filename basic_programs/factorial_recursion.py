def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n *fact_rec(n-1)
n=int(input("ENTER THE NUMBER:"))
print(f"THE FACTORIAL OF {n} is {fact_rec(n)}")
