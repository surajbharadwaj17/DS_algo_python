
def mergeSort(nums):
    n = len(nums)
    mid = n//2
    left = nums[:mid]
    right = nums[mid+1:]

    mergeSort(left)
    mergeSort(right)

    i,j,k = 0,0,0

    while(i<len(left) and j < len(right)):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
    
        k += 1

    while(i < len(left)):
        nums[k] = left[i]
        i += 1
        k += 1

    while(j < len(right)):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums


nums = [4,5,7,35,6,78]

print(mergeSort(nums))

