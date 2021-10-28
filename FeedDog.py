# a) Description:

# b) Implementation: We start with two arrays, hunger_level and biscuit_size. First, we will sort these arrays with
# Python's sort() function.  Then, we need to initialize two variables:  one that will hold the number of dogs that can
# fed and a counter. Initialize both to 0. Then, we will iterate through both arrays to find the current positions of
# both dog and biscuit. If the biscuit size is greater than or equal to the hunger level of the dog, then the dog is
# able to be fed so we increment the number of dogs and continue to the next dog and next biscuit. However, if the
# biscuit_index is at the same index of the hunger_level, we cannot feed any more dogs and we return our completed list
# of dogs we can feed.

def feedDog(hunger_level, biscuit_size):
    """
    This function computes the maximum number of hungry dogs by implementing a Greedy algorithm that finds the number
    of dogs we can satisfy. If a dog has hunger hunger_level[i], it can be satisfied only by taking a biscuit of size
    biscuit_size [j] >= hunger_level [i]
    """

    hunger_level.sort()
    biscuit_size.sort()
    # make sure arrays are sorted

    num_dogs = 0
    num_bisc = 0

    length = len(hunger_level)

    for biscuit_index in biscuit_size:
        for hunger_index in range(num_bisc, length):
            # start to iterate through both of our arrays
            if hunger_level[hunger_index] <= biscuit_index:
                # if dog hunger index in d hunger array is > or = to the num of biscuits increment number of dogs and
                # counter
                num_dogs = num_dogs + 1
                num_bisc = num_bisc + 1
            elif length == hunger_index:
                # end of the index
                return num_dogs

    return num_dogs
# return our final count



################ TESTING PURPOSES #############
# hunger_level =[1, 2, 3]
# biscuit_size =[1, 1]
# test = feedDog(hunger_level, biscuit_size)
# print(test)



# c) Time-Complexity:
# Because I used Python's built in sort() method, the time-complexity is O(nLogn) also known as TimSort. I have included
# citations below for reference:
# https://www.geeksforgeeks.org/timsort/
# https://medium.com/@rylanbauermeister/understanding-timsort-191c758a42f3
