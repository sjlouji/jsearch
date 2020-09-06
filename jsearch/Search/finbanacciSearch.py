
def fsearch(arr, search_element):
    arr.sort()
    m = 0 
    while generateFibonacci(m) < len(arr): # 
        m = m + 1 
    offset = -1    
    while (generateFibonacci(m) > 1):
        i = min( offset + generateFibonacci(m - 2) , len(arr) - 1)
        if (search_element > arr[i]):
            m = m - 1
            offset = i
        elif (search_element < arr[i]):
            m = m - 2
        else:
            return True       
    if(generateFibonacci(m - 1) and arr[offset + 1] == search_element):
        return offset + 1
    return False


def generateFibonacci(val):
    if val < 1:
        return 0
    elif val == 1:
        return 1
    else:
        return generateFibonacci(val - 1) + generateFibonacci(val - 2)