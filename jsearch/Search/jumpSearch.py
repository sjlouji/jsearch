import math
import time

def jsearch(arr, search_element):
    low = 0
    arr.sort()
    interval = int(math.sqrt(len(arr)))
    for i in range(0,len(arr),interval):
        if arr[i] < search_element:
            low = i
        elif arr[i] == search_element:
            return True
        else:
            break
    c=low
    for j in arr[low:]:
        if j==search_element:
            return True
        c+=1
    return False