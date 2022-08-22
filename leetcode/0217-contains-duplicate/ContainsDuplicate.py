from ast import List

# import sys, types, array
class Leet:
    def containsDuplicateRaw(nums) -> bool:
        length = len(nums)
        for i, num in enumerate(nums):
            if i == length - 1:
                return False
            for n in nums[i+1:length]:
                if num == n:
                    return True
        return False

    def containsDuplicateViaDict(nums) -> bool:
        mdict = dict()
        for num in nums:
            if mdict.get(num) != None:
                return True
            mdict[num] = True
        return False