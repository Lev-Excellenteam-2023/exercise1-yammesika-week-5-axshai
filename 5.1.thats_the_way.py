import os

DEEP_STR = "deep"


def find_deep_files(path):
    """
    Find files in a directory that start with 'deep'
    :param path: The directory to search in.
    :return: A list of filenames that start with 'deep' in the specified directory.
    """
    return [item for item in os.listdir(path) if os.path.isfile(os.path.join(path, item)) and item.startswith(DEEP_STR)]


if __name__ == "__main__":
    input_path = input("enter the path")
    find_deep_files(input_path)
