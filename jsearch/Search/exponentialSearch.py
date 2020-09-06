def esearch(arr, search_element):
    n = len(arr)
    arr.sort()
    if arr[0] == search_element: 
        return 0
    i = 1
    while i < n and arr[i] <= search_element: 
        i = i * 2
    return binarySearch( arr, i / 2,  
                         min(i, n), search_element) 



def binarySearch( arr, l, r, x): 
    if r >= l: 
        mid = int(l + ( r-l ) // 2)
        if arr[mid] == x: 
            return True 
          
        if arr[mid] > x: 
            return binarySearch(arr, l,  
                                mid - 1, x) 
          
        return binarySearch(arr, mid + 1, r, x) 
          
    return False