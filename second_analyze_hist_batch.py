# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import itertools as iter
import numpy as np
import time
import sys
import os
from tqdm import tqdm

from second_analyze_plot_combination import secode_plot as sa

odd = (list(iter.combinations(range(1,50,2),4)))
even = (list(iter.combinations(range(2,49,2),4)))



'''
def to_combination_actual_tuple(target_combination_number):
    flag = 0
    for i in odd:
        for j in even:
            if target_combination_number == flag:
                return str([str(t) for t in i]), str([str(t) for t in j])
            else:
                flag += 1
'''
def to_combination_actual_tuple(target_combination_number, cc):
    i_index = target_combination_number // 10626 # len(even)
    j_index = target_combination_number % 10626
    i = odd[i_index]
    j = even[j_index]
    return str([str(t) for t in i]), str([str(t) for t in j])
    

data = list(np.array([0]*49, dtype=np.int8))
num2analyze_start = input('請輸入您想要分析的第一筆資料: ')
num2analyze_end = input('請輸入您想要分析的最後一筆資料: ')
four_four_threshold = input('請輸入4/4分析的最高組合數: ')
if int(four_four_threshold) != 0:
    flag = 0
    cc = list(range(len(odd)))
    for index, i in enumerate(odd):
        cc[index] = flag
        for j in even:
            flag += 1
else:
    cc = list()

chart_list = {}
# try:
for num2analyze in range(int(num2analyze_start), int(num2analyze_end) + 1):
    print('讀取資料中...')
    print('分析從第 {} 期資料往前看連續沒開的組合總數......'.format(num2analyze))
    npz_data = (np.load(os.path.join('second_stage_data/','base_array_{}.npz'.format(str(num2analyze))))['data'])

    hist_data = np.histogram(npz_data, bins=range(0, int(num2analyze)+2))

    if os.path.isdir('second_output') is False:
        print('找不到 second_output 資料夾, 建立新資料夾..')
        os.mkdir('second_output')
    f = open(os.path.join('second_output','second_analyze_data_{}.dat'.format(num2analyze)) ,'w', 1)
    f.write('#1 First part\n\n\n')
    for index, dat in enumerate(tqdm(hist_data[0], ascii=True)):
        chart_input = np.zeros(49, dtype=np.int64)
        
        if dat > 0:
            chart = sa(odd, even, index, chart_input, npz_data)
            chart_list[index] = chart
            non_zero = np.transpose(np.argwhere(chart>0))+1
        else:
            non_zero = [[]]
        
        if len(non_zero[0]) != 0:
            f.write('{} --> {}\n'.format(index, dat))
            f.write('The total number count: {}\n'.format(len(non_zero[0])))
            f.write('The including number: ')
            f.write(str([str(t) for t in non_zero[0]]))
            f.write('\n')
            if dat < int(four_four_threshold):
                f.write('The 4/4 combination: \n')
                combination_number_target = np.where(npz_data == index)[0]
                for ii in combination_number_target:
                    odd_combination_str, even_combination_str = to_combination_actual_tuple(ii, cc)
                    f.write(odd_combination_str)
                    f.write(' , ')
                    f.write(even_combination_str)
                    f.write('\n')
            f.write('\n\n')
            f.flush()
        else:
            continue

    f.write('End \n\n\n\n\n')
    f.close()
# except:
#     print('發生錯誤，請檢查輸入是否正確或是重新執行')