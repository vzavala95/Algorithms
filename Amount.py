# Citations used:
# https://www.youtube.com/watch?v=PFkUl_rW3_w
# https://stackoverflow.com/questions/4632322/finding-all-possible-combinations-of-numbers-to-reach-a-given-sum

# Since we need to find all possible results, and not best result we can use backtracking instead of dynamic
# programming for this problem. To solve, we would need to iterate through each element in the array, starting from the
# beginning of the array, storing as we go. When we see that the target value is less than the sum of the combination of
# the choices, we backtrack to the previous selection by using pop() and try a different path to find the solution.


# b) implementation of solution

def amount(A, S):
    """
     Given a collection of amount values (A) and a S sum (S), this function will find all unique combinations in A where
    the amount values sum up to S.
    """
    A.sort()
    result = []
    combination = []
    amount_helper(result, combination, A, 0, S)
    return result


def amount_helper(result, combination, A, start, S):
    """
    This function is a helper function for amount. It implements a backtracking algorithm to find a combination of
    integers that will add up to S sum S
    """
    if S < 0:
        return
    # check to see if sum exceeded the target

    if S == 0:
        # we have found a result
        result.append(list(combination))
        return
    # above are base cased needed to stop recursion

    previous_num = -1
    # make sure we don't have duplicates
    length = len(A)
    for i in range(start, length):
        # iterate through array
        # find result by making the choice of keeping each number in array
        if A[i] != previous_num:
            combination.append(A[i])
            # store results in combination
            amount_helper(result, combination, A, i + 1, S - A[i])  # we pass 'i + 1' and not 'i' as duplicates NOT allowed
            previous_num = A[i]
            # backtrack to remove last selection in the array
            combination.pop()

############### TESTING #################
# if __name__ == '__main__':
#     print(amount([11, 1, 3, 2, 6, 1, 5], 8))


# c) Time-Complexity: Exponential Complexity - O(2^n)



