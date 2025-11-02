def is_strictly_increasing_digits(n):

    if n < 0 or type(n) != int:
        return -1
    
    n_string = str(n)

    for i in range(0, len(n_string) - 1):
        if n_string[i+1] <= n_string[i]:
            return False
    
    return True 

    #GIT COMMIT WHOLE FOLDER SUBMIT
    ### Replace with your own code (end)   ###
