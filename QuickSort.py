def QuickSort(arr):
    QuickSort_rec(arr, 0 ,len(arr)-1)


def QuickSort_rec(arr, arr_start ,arr_end):
    
    if arr_start < arr_end:
        
        parts = index_part(arr, arr_start ,arr_end);
        
        QuickSort_rec(arr, arr_start ,parts-1);
        QuickSort_rec(arr, parts+1 ,arr_end);


def index_part(arr,start,end):
    
    pivot = arr[start]
    
    left = start+1
    right= end
    
    index_found = False;
    
    while not index_found:
        
        while left <= right and arr[left] <= pivot:
            left = left + 1
            
        while right >= left and arr[right] >= pivot:
            right = right - 1
            
        if right < left:
            index_found = True;
        else:
            temp=arr[left];
            arr[left]=arr[right];
            arr[right]=temp;
            
    temp1 = arr[start]
    arr[start] = arr[right]
    arr[right] = temp1
    
    return right
