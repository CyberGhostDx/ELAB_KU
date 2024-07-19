def checkSubset(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
