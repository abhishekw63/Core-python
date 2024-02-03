def min_val(*nums,low_limit=None):
    if low_limit==None:
        return min(nums)
    else:
        list1=[num for num in nums if num>=low_limit]
        return min(list1)

print(min_val(1,2,3,3,4,-4,6,-345,32,35,-54))