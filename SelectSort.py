
def Select_sort(arr):
    
    for index in range(len(arr)-1,0,-1):
        
        max = 0
        
        for i in range(1,index+1):
            
            if arr[i]>arr[max]:
                max=i
        
        temp=arr[index]
        arr[index]=arr[max]
        arr[max]=temp
                

    return arr

