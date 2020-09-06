import time


def bsearch(arr, search_element):
    start = time.time()
    l = 0
    u = len(arr)-1
    arr.sort()
    while l <= u:
        mid = (l+u) // 2
        if arr[mid] == search_element:
            end = time.time()
            print(end - start)
            return True
        else:
            if arr[mid] < search_element:
                l = mid+1
            else:
                u = mid-1
    end = time.time()
    print(end - start)
    return False


