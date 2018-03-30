# -*- coding: UTF-8 -*-

from matplotlib import pyplot as plt
import itertools as iter
import numpy as np
import time
import sys
import os
from tqdm import tqdm


data = list(np.array([0]*49, dtype=np.int8))
num2analyze = input('請輸入您想要分析第幾期的資料: ')
try:
    print('讀取資料中...')
    npz_data = (np.load(os.path.join('second_stage_data/','base_array_{}.npz'.format(str(num2analyze))))['data'])

    hist_data = np.histogram(npz_data, bins=range(0, int(num2analyze)+2))
    while True:
        analyse_range = input('請輸入想要分析的範圍: (min-max: {}-{})/離開請按q  '.format(0, int(num2analyze))).split('-')
        if analyse_range == ['q']:
            print('離開繪圖模式')
            break
        else:
            if len(analyse_range) != 2:
                print('輸入錯誤，請檢查範圍輸入是否正確')
                continue
            else:
                try:
                    range_front = int(analyse_range[0])
                    range_back = int(analyse_range[1])+1

                    fig, ax = plt.subplots() 
                    plt.xlabel('Range {}-{}'.format(range_front, range_back-1))
                    plt.ylabel('Combination number count')   
                    plt.bar(np.arange(range_front,range_back), hist_data[0][range_front:range_back])
                    for i, v in enumerate(hist_data[0][range_front:range_back]):
                        ax.text(i, v + 5, '{}'.format(i), color='blue', fontweight='bold')
                    plt.show()
                    # plt.cla()
                    # plt.clf()
                except ValueError:
                    print('請檢查您輸入的範圍是否超過總期數, again')
                    continue
    odd = (list(iter.combinations(range(1,50,2),4)))
    even = (list(iter.combinations(range(2,49,2),4)))
    while True:
        analyse_vacancy = input('請輸入想要分析的連續未開數: (min: {}/ max: {})/離開請按q  '.format(0, int(num2analyze)))
        
        if analyse_vacancy == 'q':
            break

        if (int(analyse_vacancy) < 0) or (int(analyse_vacancy) > int(num2analyze)):
            print('請檢查您輸入的範圍, again')
            continue

        num = 0
        chart = np.zeros(49, dtype=np.int64)
        target = int(analyse_vacancy)
        for ii in tqdm(odd, ascii=True):
            for jj in even:
                if npz_data[num] == target:
                    for i in ii:
                        chart[i-1] += 1
                    for j in jj:
                        chart[j-1] += 1
                num += 1
        print('Complete')
        fig, ax = plt.subplots() 
        plt.xlabel('Lotter number {}-{}'.format(1, 49))
        plt.ylabel('Combination number count')   
        plt.bar(np.arange(1,50), chart)
        for i, v in enumerate(chart):
            ax.text(i, v + 5, '{}'.format(i), color='blue', fontweight='bold')
        plt.show()        



except IOError:
    print('操作錯誤，請檢察是否有正確npz檔案在second_stage_data資料夾中')

except IndexError:
    print('操作錯誤，請檢查輸入')        

except ValueError:
    print('請檢查您輸入的範圍是否超過總期數')