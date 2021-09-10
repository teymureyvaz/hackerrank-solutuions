def jumpingOnClouds(c):
    step_counter = 0
    step = 0
    c.append(2)
    while step < len(c) - 2:
        if c[step + 2] != 1:
            step_counter += 1
            step += 2
        else:
            step_counter += 1
            step += 1
    return step_counter
