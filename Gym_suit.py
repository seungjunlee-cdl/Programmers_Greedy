def solution(n, lost, reserve):
    reserve_set = list(set(reserve)-set(lost))
    lost_set = list(set(lost)-set(reserve))
    
    num_aud = n-len(lost_set)
    
    for i in lost_set:
        if i-1 in reserve_set:
            num_aud += 1
            reserve_set.remove(i-1)
        elif i+1 in reserve_set:
            num_aud += 1
            reserve_set.remove(i+1)
            
    return num_aud
