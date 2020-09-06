import time

def lsearch(arr, search_element):
    start = time.time()
    for i in range( 0 , len(arr) ):
        if(arr[i] == search_element):
            end = time.time()
            print(end - start)
            return True
    end = time.time()
    print(end - start)
    return False