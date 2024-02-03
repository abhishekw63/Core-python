print(dir(set))
'''
add
clear
discard
copy
union
difference - difference_update
intersection-intersection_update
symmetric_difference - symmetric_diffrence_updates
isdisjoint
issubset
issuperset
'''
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print('union',s1.union(s2))
print('union ',s2.union(s1))

print(f'difference s1-s2:{s1.difference(s2)}')
print(f'difference s2-s1:{s2.difference(s1)}')

print(f'intersection s1-s2:{s1.intersection(s2)}')
print(f'intersection s2-s1:{s2.intersection(s1)}')

print(f'symmetric difference s1^s2:{s1.symmetric_difference(s2)}')
print(f'symmetric difference s2^s1:{s2.symmetric_difference(s1)}')

s1.intersection_update(s2)
print(f'intersection update (s1<-s2):{s1}')

s1={1,2,3,4,5}
s2={4,5,6,7,8}

s2.difference_update(s1)
print(f'difference update s1->s2:{s2}')

s1={1,2,3,4,5}
s2={4,5,6,7,8}

s1.symmetric_difference_update(s2)
print(f'symmetric difference update s1<-s2:{s1}')

s0={1,2,3,4,5,6,7,8}
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s3={10,11,12,13}

print(f'is subset? {s1.issubset(s2)}')
print(f'is subset? {s1.issubset(s0)}')

print(f'is superset? {s0.issuperset(s1)}')
print(f'is superset? {s3.issuperset(s2)}')

print(f'is disjoint? {s2.isdisjoint(s3)}')
print(f'is disjoint {s1.isdisjoint(s0)}')

