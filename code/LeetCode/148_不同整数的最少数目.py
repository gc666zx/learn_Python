def findLeastNumOfUniqueInts(arr, k):
    arr.sort()
    nums = []
    num = 1
    arr.append(None)
    for i in range(1, len(arr)):
        if arr[i-1] == arr[i]:
            num += 1
        else:
            nums.append(num)
            num = 1
    nums.sort()
    for i in range(len(nums)):
        k -= nums[i]
        if k == 0:
            return len(nums) - i - 1
        elif k < 0:
            return len(nums) - i


if __name__ == "__main__":
    nums = [1]
    k = 0
    result = findLeastNumOfUniqueInts(nums, k)
    print(result)