from matplotlib import pyplot as plt
import itertools as iter
import numpy as np
import time
import sys
import os
from tqdm import tqdm
import analyze_second


data = list(np.array([0]*49, dtype=np.int8))
num2analyze = input('請輸入您想要分析第幾期的資料: ')
try:
    print('讀取資料中...')
    npz_data = list(np.load(os.path.join('second_stage_data/','base_array_{}.npz'.format(str(num2analyze))))['data'])

    odd = (list(iter.combinations(range(1,50,2),4)))
    even = (list(iter.combinations(range(2,49,2),4)))

    num = 0
    for ii in tqdm(odd):
        for jj in even:
            analyze_second(ii,jj,npz_data, data,num)
    #         for i in ii:
    #             data[i-1] += npz_data[num]
    #         for j in jj:
    #             data[j-1] += npz_data[num]
            num += 1
    plt.bar(np.arange(1,50), data)
    plt.show()
except:
    print('操作錯誤，請檢察是否有正確npz檔案在second_stage_data資料夾中')
        
        
        