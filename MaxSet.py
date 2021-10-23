
# Citations:
# https://www.youtube.com/watch?v=n9F9wQD3Mhc
# https://backtobackswe.com/platform/content/max-contiguous-subarray-sum/video?utm_source=youtube&utm_medium=video
from typing import List


def max_independent_set(nums):
    """
    This function returns a subset of non-consecutive numbers in the form of a list that would have the maximum sum.
    :param nums: int
    :return: int
    """
    length = len(nums)
    result: List[int] = [0] * length

    cache_memo = {}
    # store the results of each subproblem we have created
    for i in range(length):
        # start iterating through array

        while length == 1:
            # this is only if there is 1 element in the array
            if nums[i] < 0:
                # if there is 1 number in the array AND it's a negative number
                nums[i] = 0
            return nums

        if nums[i] + result[i - 2] > result[i - 1]:
            result[i] = nums[i] + result[i - 2]
            cache_memo[result[i]] = nums[i]

        else:
            result[i] = result[i - 1]

    # get optimal solution set which create max sum of nums
    solution_set = []
    n = result[length - 1]

    while n > 0:
        solution_set.append(cache_memo[n])
        # we have found a sum, now add choice to cache for storage
        n = n - cache_memo[n]
        # since we have found an optimal sum, we can keep going

    solution_set.reverse()
    # sort in descending order
    return solution_set


############## TESTING ##################

# set = [7, 2, 5, 8, 6]
# print(max_independent_set(set))
#
# set = [-1, -1, 0]
# print(max_independent_set(set))
#
# set = [1]
# print(max_independent_set(set))
#
# set = [-1, -1, -10, -34]
# print(max_independent_set(set))


set = [10, 5, 3, -7, -55, -1, 22, 25]
print(max_independent_set(set))

