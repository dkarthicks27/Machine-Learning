def arrange():
    attendence = {"karthik": 12345, "jyothsna": 21345, "sasank": 12435}
    values = []
    keys = []
    for key, value in attendence.items():
        keys.append(key)
        values.append(value)
    values.sort()
    for i in values:
        for key, value in attendence.items():
            if value == i:
                print(key, i)


# time complexity - least time complexity
arrange()
