def main(s):
    """
    A string of length five is given. Return the index of the "*" character, return False if not present.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    idx = s.find('*')
    if idx != -1:
        return idx
    else:    
        return False

print(main('2*44')) 
        