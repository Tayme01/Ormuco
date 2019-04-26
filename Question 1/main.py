def does_it_overlap(first, second):
    """
        :param first: the coordinates of the first line.
        :param second: the coordinates of the second line.
        :return: True, False or Invalid Input.
    """
    try:
        # format inputs
        first = list(map(float, first.strip(' ').split(' ')))
        second = list(map(float, second.strip(' ').split(' ')))

        # input validation
        if (first[0] >= first[1]) or (second[0] >= second[1]):
            return 'Invalid Input'

        if (first[0] < second[0] < first[1]) or (second[0] < first[0] < second[1]):
            return True
        else:
            return False

    except (TypeError, IndexError, ValueError) as err:
        return 'Error: {0}'.format(err)


line1 = input('Input the coordinates of the first line in the following format - x1 x2: ')
line2 = input('Input the coordinates of the second line in the following format - x1 x2: ')

print(does_it_overlap(line1, line2))


