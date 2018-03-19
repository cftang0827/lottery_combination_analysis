cimport cython
cimport numpy as np

def analyse_zero(np.ndarray [long, ndim=1] base_array_c,np.ndarray [long, ndim=1] target_input_c,np.ndarray [long, ndim=1] overall_dict_c):
    cdef int num = 0
    cdef int i
    cdef np.ndarray [long, ndim=1] dd
  
    for i in target_input_c:
        if i == 1:
            overall_dict_c[base_array_c[num]] += 1            
            base_array_c[num] = 0
        else:
            base_array_c[num] += 1
        num += 1
    
    overall_dict_c[0] = 0
