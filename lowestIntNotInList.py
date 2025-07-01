def find_lowest_missing_integer(nums):
    len=1
    min = nums[0]
    for n in nums[1:]:
        if n < min:
            min = n
        #endif
        len+=1
    #next n
    if min > 0:
        return 0
    bit_array = [0] * (len+1)
    for n in nums:
        if n < len:
            bit_array[n]=1
        #endif
    #next
    lowest_int = 0
    while bit_array[lowest_int] == 1:
        lowest_int += 1

    return lowest_int

# Main
distinct_integers = [0, 1, 2, 4, 6, 3, 5, 13]
result = find_lowest_missing_integer(distinct_integers)
print("The lowest missing integer is:", result)
