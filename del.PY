
n=int(input('enter the terms:'))

fib_series=[0,1]

for i in range(1,n-1):
    temp=fib_series[-1]+fib_series[-2]
    fib_series.append(temp)

print(fib_series)
    