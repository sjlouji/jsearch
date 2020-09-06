def isearch(arr, search_element): 
    arr.sort()
    lo = 0
    n = len(arr)
    hi = (n - 1) 
    while lo <= hi and search_element >= arr[lo] and search_element <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == search_element:  
                return lo
            return True
          
        pos  = lo + int(((float(hi - lo) / ( arr[hi] - arr[lo])) * ( search_element - arr[lo]))) 
  
        if arr[pos] == search_element: 
            return pos 
   
        if arr[pos] < search_element: 
            lo = pos + 1
   
        else: 
            hi = pos - 1
      
    return False