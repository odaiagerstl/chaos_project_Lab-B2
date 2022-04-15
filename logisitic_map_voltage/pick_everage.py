import copy

Delta = 0.05


def arrange_L_data(L):
    """
    this function arrange the L list
    :param L:
    :return: 2D list arrange with gropes of maximum
    """
    sorted_L = copy.deepcopy(L)
    sorted_L.sort()
    data = []
    index = 0
    while index < len(sorted_L) - 1:
        data.append([])
        while index < len(sorted_L) - 1 and sorted_L[index + 1] - sorted_L[index] < Delta:
            data[-1].append(sorted_L[index])
            index += 1
        data[-1].append(sorted_L[index])
        index += 1
    # print(data)
    return data


def Average(lst):
    return sum(lst) / len(lst)


def maximum_filtering(lst):
    data = arrange_L_data(lst)
    maximum = []
    for lst in data:
        maximum.append(Average(lst))

    return maximum


def maximum_save_order(lst):
    """

    :return:
    """
    maximum = maximum_filtering(lst)
    maxi_in_order = []
    for i in lst:
        for value in maximum:
            if abs(i - value) < Delta:
                maxi_in_order.append(value)
    return maxi_in_order

if __name__ == '__main__':
    L = [1.5999999, 3.93999982, 1.5999999, 3.93999982, 1.5799999, 3.9599998, 1.5999999, 3.93999982, 1.62, 3.93999982,
         1.5999999, 3.93999982, 1.62, 3.93999982, 1.5999999, 3.93999982, 1.5999999, 3.93999982, 1.5999999]

    print(maximum_filtering(L))
    print(maximum_save_order(L))