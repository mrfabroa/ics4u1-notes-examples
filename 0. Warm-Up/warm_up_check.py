def bigdiff(numlist):
    '''Given a list, return the difference between the largest and smallest values in the list

    :param numlist: a list of integers
    :return: the difference between the largest and smallest values in the list
    '''

    # set the largest and smallest to default
    largest = numlist[0]
    smallest = numlist[0]

    # iterate throught the list to find the largest and smallest
    for i in range(1,len(numlist)):
        largest = max(largest, numlist[i])
        smallest = min(smallest, numlist[i])

    # return the difference between the largest and smallest
    return largest - smallest


# test out the function
print(bigdiff([3,6,2,4,7]))


