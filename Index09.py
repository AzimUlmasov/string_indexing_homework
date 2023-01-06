def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    idx = int(s)
    if s.isdigit() and int(s) > 0:
        return idx
    else:
        return -1
print(main('4)) 