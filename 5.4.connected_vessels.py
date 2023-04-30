def interleave(*iterables):
    """
    Interleaves the items of multiple iterables into a single list.
    :param iterables: unknown number of iterable objects.
    :return: A list of items interleaved from the input iterables
    """
    result_list = []
    for zip_item in list(zip(*iterables)):
        result_list.extend(zip_item)
    return result_list


def generator_interleave(*iterables):
    """
    A generator function that interleaves the items of multiple iterables.
    :param iterables: unknown number of iterable objects.
    :return: A list of items interleaved from the input iterables
    """
    result_list = []
    zipped_iterables = list(zip(*iterables))
    for iterable in zipped_iterables:
        for item in iterable:
            result_list.append(item)
            yield result_list


if __name__ == "__main__":
    print(f"interleave example:\n{interleave('abc', [1, 2, 3], ('!', '@', '#'))}")
    print("generator_interleave example:")
    for intermediate_list in generator_interleave('abc', [1, 2, 3], ('!', '@', '#')):
        print(intermediate_list)
