cimport cython
cimport numpy as np
ctypedef np.long DTYPE_t


def analyze_second(ii, jj, npz_data, data, num):
    cdef tuple ii_c = ii
    cdef tuple jj_c = jj
    cdef list npz_data_c = npz_data
    cdef list data_c = data
    
    cdef int num_c = num 
    
    cdef int i = 0
    cdef int j = 0
    
    for i in ii_c:
        data_c[i-1] += npz_data_c[num_c]
    for j in jj_c:
        data_c[j-1] += npz_data_c[num_c]
    data = data_c