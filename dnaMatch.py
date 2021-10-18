# def dna_match_topdown(DNA1, DNA2):
#     """
#       Function that uses a top-down approach to find the longest common subsequence between two strings
#       :param DNA1: str
#       :param DNA2: str
#       :return: int
#       """
#
#     # Helper function for recursion
#     def dna_helper(string1, string2, dnaMemo):
#         """
#         Helper function for dna_match_topdown. Scans strings for a match between the two and stops recursion once we
#         reach the base case in which the string has no more characters and is empty.
#
#         :param string1: int
#         :param string2: int
#         :param dnaMemo: int
#         :return:
#         """
#
#         if string1 == 0 or string2 == 0:
#             # this is the base case we want to return to. No more comparisons are made if the base case has been reached
#             return 0
#
#         # if we have already computed, stops further recursion and avoids unnecessary repetition
#         if not dnaMemo[string1 - 1][string2 - 1] == -1:
#             return dnaMemo[string1 - 1][string2 - 1]
#
#         # if there is a match between characters. If looking at a DP table, we would see that this subproblem answer =
#         # 1 + the answer to the subproblem with no match in characters
#         if DNA1[string1 - 1] == DNA2[string2 - 1]:
#             dnaMemo[string1 - 1][string2 - 1] = 1 + dna_helper(string1 - 1, string2 - 1, dnaMemo)
#
#         # if characters in string do not match, we have to answer subproblems and compare between answers.
#         # Whichever one becomes the new answer to the subproblem
#         else:
#             dnaMemo[string1 - 1][string2 - 1] = max(dna_helper(string1 - 1, string2, dnaMemo), dna_helper(string1, string2 - 1, dnaMemo))
#
#         return dnaMemo[string1 - 1][string2 - 1]
#     # winner of subproblem comparison, new answer and new count of sequence
#
#     # Initialize memo array and test
#     dnaMemo = [[-1 for j in range(len(DNA2))] for i in range(len(DNA1))]
#     return dna_helper(len(DNA1), len(DNA2), dnaMemo)
#
# DNA1 = "adqufhfff"
# DNA2 = "fkafhdjfn"
#
# print("The longest common subsequence is:", dna_match_topdown(DNA1, DNA2))

def dna_match_bottomup(DNA1, DNA2):
    """
    Function that uses a top-down approach to find the longest common subsequence between two strings
    :param DNA1: str
    :param DNA2: str
    :return: int
    """

    # visualizing as a table with DNA1 as columns and DNA2 as rows

    string1 = len(DNA1)
    # store for comparison
    string2 = len(DNA2)

    # base case: empty array so no more comparisons made and we are finished
    # initialize the 2d array by creating rows and columns with extra space + 1 to fill out the array
    table_arr = [[0 for i in range(0, string1 + 1)] for i in range(0, string2 + 1)]























