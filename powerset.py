# Citations
# I used CS 325: Week 4 - Dynamic Programming and Backtracking Exploration pseudocode to solve this problem

import copy


def powerset(input):
    """
    When given a set of n distinct numbers, this function will return its powerset.
    :param input: int
    :return: int
    """

    result = []
    powerset_helper(len(input) - 1, [], input, result)
    return result


def powerset_helper(pointer, choices_made, input, result):
    """
    Helper function for powerset function.
    :param pointer: int
    :param choices_made: int
    :param input: int
    :param result: int
    :return:
    """

    if pointer < 0:
        # index out of bounds
        result.append(copy.deepcopy(choices_made))
        # copy current choice to result array and backtrack to last choice
        return

    choices_made.append(input[pointer])
    # add current element pointer is pointing at to the list of choices made
    powerset_helper(pointer - 1, choices_made, input, result)

    # now we can backtrack and remove last element we added to choices made
    del choices_made[-1]
    powerset_helper(pointer - 1, choices_made, input, result)


################### TESTING ##################

# if __name__ == "__main__":
#
#     print(powerset([1, 2]))



