def puissance (x,n):
    if n>0:
        return x * puissance (x,n-1)
    else: 
        return 1

print(puissance(8,8))