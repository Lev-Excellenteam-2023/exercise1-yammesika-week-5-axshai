import re

MESSAGE_TEMPLATE = "[a-z]{5}[a-z]*!"
LOGO_PATH = "logo.jpg"


def find_all_messages():
    """
    A generator function that reads the logo file line by line,
    searches for messages that match the MESSAGE_TEMPLATE regular expression,
    and yields each message found.
    """
    with open(LOGO_PATH, 'rb') as logo_file:
        line = logo_file.readline()
        while line:
            for message in re.findall(MESSAGE_TEMPLATE, str(line)):
                yield message
            line = logo_file.readline()


def main():
    for message in find_all_messages():
        print(message)


if __name__ == "__main__":
    main()
