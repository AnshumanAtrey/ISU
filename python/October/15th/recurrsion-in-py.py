def recursive_function(n):
    """
    This is a recursive function that calls itself with a smaller value of n until n is 0.
    
    Parameters:
    n (int): The number to be decremented.
    
    Returns:
    None
    """
    if n > 0:
        print(n)
        recursive_function(n-1)
    else:
        print("Done!")
