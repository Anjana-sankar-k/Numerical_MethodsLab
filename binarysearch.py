def binary_search(arr,target):
  low, high = 0, len(arr) - 1 
  while low <= high:
    mid = (low +high) // 2
    if(arr[mid] == target):
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1 
  return -1
  

arr = [1, 3, 5, 7, 9, 11]
target = 7

result = binary_search(arr, target)
print(f"Element found at index: {result}" if result != -1 else "Element not found")