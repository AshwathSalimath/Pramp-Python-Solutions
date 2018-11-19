def index_equals_value_search(arr):
  st = 0
  ed = len(arr)
  
  while st<=ed:
    mid = (st+ed)/2
    if(arr[mid] == mid):      
      if(arr[mid-1] == (mid -1)):
        ed = mid - 1        
      else:
        return mid
    elif (mid > arr[mid]):
      st = mid + 1 ## Going right
    else: 
      ed = mid - 1 ## Going left
        
  return -1  
