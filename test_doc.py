def sum_repeats(input_list):
    """
    Given a list of numbers, return the sum of all numbers that are the same as the 
    next number in the list.

    In this example, there are two 1's next to each other and two 6's next to each 
    other, so the function should return 7.

    >>> sum_repeats([1, 1, 5, 1, 2, 6, 6])
    7

    """
    sum = 0
    ex_list =[]

    input_list.sort()

    for index, digit in enumerate(input_list):
        if index != (len(input_list) - 1):
            if (input_list[index] == input_list[index + 1]):
                if digit not in ex_list:
                    ex_list.append(digit)
                    sum += digit

    # for index in range(len(input_list) -1):
    #     # print(sum)
    #     if input_list[index] == input_list[index + 1]:
    #         sum += input_list[index]
         
    return sum

input_list = [1, 1, 1, 1, 1, 1, 1, 1, 5, 1, 2, 6, 6]
print(sum_repeats(input_list))
#expected 7