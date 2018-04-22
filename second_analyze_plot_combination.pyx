cimport cython
# @cython.boundscheck(False) 
# @cython.wraparound(False)
# @cython.nonecheck(False)
cimport numpy as np
ctypedef np.long DTYPE_t
def secode_plot(odd, even, target, np.ndarray [long long, ndim=1] chart, np.ndarray [long, ndim=1] npz_data):
    cdef list odd_c = odd
    cdef list even_c = even
    cdef int target_c = target
    cdef np.ndarray [long long, ndim=1] chart_c = chart
    cdef tuple ii
    cdef tuple jj
    cdef int num = 0
    cdef int i
    cdef int j
    for ii in odd_c:
        for jj in even_c:
            if npz_data[num] == target_c:
                for i in ii:
                    chart_c[i-1] += 1
                for j in jj:
                    chart_c[j-1] += 1
            num += 1
    return chart_c