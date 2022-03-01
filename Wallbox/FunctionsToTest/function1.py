def findFirstDuplicate(vector1, vector2):
    if (len(vector1) == 0 or len(vector2) == 0):
        raise Exception("One of the vectors is empty")
    for i in range(len(vector2)):
        if vector2[i] in vector1:
            return "Duplicate integer: " + str(vector2[i])
        else:
            return "No duplicates found"