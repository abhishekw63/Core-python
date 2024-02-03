'''oprators upon set:
|
&
-
^
<   <=
>   >=
==  !-
in not in
'''
s1={1,2,3,4,5,6,7,8,9,10}
s2={1,2,3,4,5}
s3={4,5,6,7,8,11}
s4={1,2}

print('union',s1 | s3)
print('intersection',s2 & s3)

print('difference s2-s3',s2-s3)
print('difference s3-s2',s3 - s2)

print('symmmetric difference',s2^s3)

print('proper subset',s2<s1)
print('proper subset',s3<s1)

print('<= ',s4<=s1)

print('proper superset',s4>s1)
print('proper superset',s2<s1)

print('>=',s2>=s4)

print('==',s1==s1)
print('!=',s1!=s1)

print(2 not in s1)
print (101 not in s1)

# a=a|b a|=b
# a=a&b a&=bs