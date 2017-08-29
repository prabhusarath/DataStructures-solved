
# coding: utf-8

# In[127]:

def medians(arr1,st1,en1,arr2,st2,en2):
    
    if  (en1-st1) == 2 and (en2-st2) == 2:
        return (max(arr1[st1],arr2[st2]) + min(arr1[en1],arr2[en2]))/2
         
    mm1 = st1+en1//2
    mm2 = st2+en2//2
    
    m1 = arr1[mm1]
    m2 = arr2[mm2]
    
    if m1 == m2:
        return m2
    
    if m1 < m2:
        st1= mm1
        en2 = mm2
        return medians(arr1,st1,en1,arr2,st2,en2)    
    
    else:
        st2= mm2
        en1 = mm1
        
        return medians(arr1,st1,en1,arr2,st2,en2)

