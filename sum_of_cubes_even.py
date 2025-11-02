def sum_of_cubes_even(n):

    
    if n < 0 or type(n) != int:
        return -1
    
    if n >= 2000:
        print("WARNING")
    
    sum =0
    for a in range(0,n + 1):
        if a % 2 == 0:
            sum = a**3 + sum
    return float(sum)



   
