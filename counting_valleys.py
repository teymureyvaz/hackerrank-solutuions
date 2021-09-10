def countingValleys(steps, path):
    sea_level = 0
    sea_level_counter = 0
    for step in path:
        if step == "D":
            sea_level -= 1
        else:
            sea_level += 1

        if sea_level == 0 and step == "U":
            sea_level_counter += 1
    return sea_level_counter
