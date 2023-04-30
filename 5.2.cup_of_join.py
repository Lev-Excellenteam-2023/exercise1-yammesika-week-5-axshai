def join(*lists, sep="-"):
    """
    Concatenates any number of lists into a single list with each element separated by a specified separator string.
    :param lists: Any number of lists to be concatenated.
    :param sep: The separator string to be placed between each element of the concatenated list. Defaults to "-".
    :return: A new list containing all of the elements from the input lists, separated by the specified
    separator string.
    """
    if not lists:
        return None
    result_list = []
    for lst in lists:
        result_list += lst
        result_list.append(sep)
    return result_list[:-1]


if __name__ == "__main__":
    print(join([1, 2, 3], [4, 5, 6], [7, 8, 9]))
