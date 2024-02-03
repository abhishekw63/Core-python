

D = dict()

for x in enumerate(range(2)): #(0,0) (1,1)

    D[x[0]] = x[1]

    D[x[1]+7] = x[0]

print(D)
#{0:0,7:0,1:1,8:1}