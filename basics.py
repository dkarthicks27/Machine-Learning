# dictionary - school attendance record
# names, id, arrange them alphabetic order
# according to their name

# according to their id
attendance = {'Karthick': 12345, 'Jyo': 21345, 'Sashank': 12435}


def arrangeWithName():
    names = []
    for key in attendance:
        names.append(key)
    names.sort()
    for i in names:
        print(i, attendance[i])


def arrangeWithId():
    pass


arrangeWithName()
arrangeWithId()
