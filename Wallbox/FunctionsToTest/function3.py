from copy import copy

def minimumConversionsToBeInterspersed(theArray):
    if len(theArray) == 0:
        raise Exception("Array connot be ampty")

    best = float('inf')
    for j in range(1, len(theArray)-1):
        forward = theArray[j:]
        back = theArray[:j+1][::-1]

        fwd_count = sequenceParser(forward, theArray[j], 0)
        bwd_count = sequenceParser(back, theArray[j], 0)

        if (fwd_count + bwd_count) < best:
            best = fwd_count + bwd_count
    return best


def sequenceParser(arrOri, preVal, count):
    arr = arrOri.copy()
    for i in range(1, len(arr)):
        if arr[i] != preVal:
            preVal = arr[i]
            continue
        else:
            count += 1
            arr[i] = int(not bool(arr[i]))
            preVal = arr[i]
    return count