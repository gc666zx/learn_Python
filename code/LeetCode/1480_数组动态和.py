def runningSum1(nums):
    result = []
    for i in range(len(nums)):
        result.append(0)
        for j in range(i+1):
            result[i] += nums[j]
    return result


def runningSum2(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums




if __name__ == "__main__":
    nums = [1,2,3,4]
    result = runningSum1(nums)
    print(result)