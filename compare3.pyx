cimport cython
# @cython.boundscheck(False) 
# @cython.wraparound(False)
# @cython.nonecheck(False)
cimport numpy as np
ctypedef np.long DTYPE_t
def compare3(a1, a2, a6_dict):
    cdef dict a6_cython = a6_dict
    cdef tuple a1_cython = a1
    cdef tuple a2_cython = a2

    for i in a1_cython:
        if a6_cython.get(i) is not None:
            for j in a2_cython:
                if a6_cython.get(j) is not None:
                    return True
    return False