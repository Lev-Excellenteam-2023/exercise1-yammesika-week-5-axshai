def interleave(*iterables):
    """
    Interleaves the items of multiple iterables into a single list.
    :param iterables: unknown number of iterable objects.
    :return: A list of items interleaved from the input iterables
    """
    result_list = []
    [result_list.extend(zip_item) for zip_item in list(zip(*iterables))]
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
