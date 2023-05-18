def Un(n):
    a=6
    b=1
    if n==0:
        return 1
    else: 
        return a*Un(n-1) + a+b 

print(f'u10={Un(10)}')
print(f'u5={Un(5)}')
