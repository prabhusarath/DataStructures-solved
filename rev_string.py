
def rev_scratch(str1):
    
    lens = len(str1)
    print(lens)
    i = 0
    sep = [' ']
    returns = []
    while i < lens:
        
        if str1[i] not in sep:
            
            start = i
            print("start",i)
            
            while str1[i] not in sep and i<lens:
                i += 1
                print("end",i)
            
            returns.append(str1[start:i])
        
        i += 1

    

    return ' '.join(returns[::-1])


