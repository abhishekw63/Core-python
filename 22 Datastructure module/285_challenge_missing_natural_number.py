import array

def find_missing(ar1):
    start=ar1[0]
    end=ar1[-1]
    expected_sum=sum(list(range(start,end+1)))

    actual_sum=sum(ar1)
    print(expected_sum,actual_sum)
    num=expected_sum-actual_sum
    
    if num>0:
        return  num
    else:
        return f'no element is missing'



ar1=array.array('i',[1,2,3,4,5,6,7,8,9,10])
print('missing element:',find_missing(ar1))