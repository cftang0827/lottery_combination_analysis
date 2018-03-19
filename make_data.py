import itertools as iter
import numpy as np
import time
import sys
import os
from compare3 import compare3
from tqdm import tqdm


def compare1(a1,a6_dict):
    for i in a1:
        if a6_dict.get(i) is not None:
            return True
    return False

def compare2(a1,a2,a6_dict):
    for i in a1:
        if a6_dict.get(i) is not None:
            for j in a2:
                if a6_dict.get(j) is not None:
                    return True
    return False


def make_winner_num_dict(winner_num):
    winner_num_dict = dict()
    for num in winner_num:
        winner_num_dict[num] = 1

    return winner_num_dict

def dict_init(overall_dict, number):
    for i in range(0,number):
        overall_dict[i] = 0

def analyse_zero(base_array, target_input, overall_dict, len_array):
    # len_array = len(target_input)
    num = 0
    for i in target_input:
        # print(i)
        if i:
            if overall_dict.get(base_array[num]) is None:
                overall_dict[base_array[num]] = 1
            else:
                overall_dict[base_array[num]] += 1
            base_array[num] = 0
        else:
            base_array[num] += 1
        num += 1

    overall_dict.pop(0,None)
#     print(base_array)
#     print(overall_dict)


def make_winner_dict_list(winner_number):
    winner_num_dict = []
    for ii in winner_number:
        winner_num_dict.append(make_winner_num_dict(ii))

    return winner_num_dict

def make_numpy_file(winner_number_dict, start_name, odd, even):
    com_num = len(odd)*len(even)
    if os.path.isdir('data') == False:
        print('無法存取data資料夾，重新建立data資料夾')
        try:
            os.mkdir('data')
        except:
            print('[錯誤2] 建立data資料夾有誤')
            sys.exit(0)
    # calculate every combination

    for ii in (range(0, len(winner_number_dict))):
        file_name = str(ii+int(start_name)) + '.data'
        print('計算檔案: ' + file_name + ' 中...')
        # combination_data = np.array([False]*com_num,np.bool)
        combination_data = [False] * com_num
        flag = 0
        for i in tqdm(odd, ascii=True):
            for j in even:
                combination_data[flag] = compare3(i, j, winner_number_dict[ii])
                flag += 1
#         print('製作檔案 ' + file_name + '中.....')
        try:
            f = open(os.path.join('data',file_name),'wb')
            combination_data_np = np.array(combination_data)
            # print(combination_data)
            np.save(f,combination_data_np)
#             print('存檔，檔名為: ' + file_name + '，存檔成功')
        except:
            print('[錯誤3] 存檔錯誤，跳過本檔案，請重新操作')
            sys.exit(0)

def get_winner_number_from_file(file_name):
    try:
        f2 = open(file_name, 'r')
        tmp = f2.read().split('\n')
        tmp = tmp[:len(tmp)-1]
        winner_number = [[int(j) for j in (i.split(','))] for i in tmp]
    except:
        print('[錯誤1] 操作異常，輸入檔名或是檔案有誤!')
        print('請重新操作')
        sys.exit(0)
    return winner_number

def get_winner_number_from_input():
    try:
        winner_str = input("請輸入開獎號碼:")
        winner_number_split_str = winner_str.split(',')
        winner_number = [[int(j) for j in winner_number_split_str]]
    except:
        print('[錯誤4] 輸入開獎號碼有誤，無法分析')
        print('請重新操作')
        sys.exit(0)
    return winner_number


def mode_1():
    # odd = list(iter.combinations(range(1,50,2),4))
    # even = list(iter.combinations(range(2,49,2),4))
    odd = list(iter.combinations(range(1,50,2),4))
    even = list(iter.combinations(range(2,49,2),4))
    input_file_name = input('請輸入包含正確格式的開獎號碼檔案名稱: ')
    print('開啟檔案 ' + input_file_name + " ......")
    winner_number = get_winner_number_from_file(input_file_name)
    print('開啟檔案 ' + input_file_name + " 成功......")
    start_name = input('請輸入檔案第一期的期數: ')
    winner_number_dict_list = make_winner_dict_list(winner_number)

    # making combination test of odd and even
    time0 = time.clock()
    make_numpy_file(winner_number_dict_list, start_name, odd, even)
    time2 = time.clock() - time0
    print('本次計算時間: ' + str(time2) + ' 秒')
    ex = input('請按Enter結束')

def mode_2():
    odd = list(iter.combinations(range(1,50,2),4))
    even = list(iter.combinations(range(2,49,2),4))
    winner_number = get_winner_number_from_input()
    winner_number_dict_list = make_winner_dict_list(winner_number)
    start_name = input('請輸入本次輸入的期數: ')
    time0 = time.clock()
    make_numpy_file(winner_number_dict_list, start_name, odd, even)
    time2 = time.clock() - time0
    print('本次計算時間: ' + str(time2) + ' 秒')
    ex = input('請按Enter結束')



def main():

    mode = input("請輸入計算模式(1/2): ")
    if mode == '1':
        mode_1()
    elif mode == '2':
        mode_2()
    else:
        print("輸入錯誤，請重新執行程式！")


    # print('Welcome to the lottery combination system')
    # mode = input('Please enter the calculation mode: ')

    # if mode == '1':

    #     odd = list(iter.combinations(range(1,50,2),4))
    #     even = list(iter.combinations(range(2,49,2),4))
    #     winner_number_raw = input('Please input the winner number: \n').split(',') # make string array to int
    #     file_name = input('Plase enter the file name: ')
    #     winner_number = [int(num) for num in winner_number_raw]

    #     winner_number_dict = make_dict(winner_number)   # make winner number bucket

    #     # making combination test of odd and even
    #     time0 = time.clock()
    #     com_num = len(odd)*len(even)
    #     combination_data = np.array([False]*com_num,np.bool)

    #     flag = 0
    #     for i in odd:
    #         for j in even:
    #             combination_data[flag] = compare2(i, j, winner_number_dict)
    #             flag += 1


    #     time2 = time.clock() - time0

    #     print('The time elasped: ' + str(time2) + ' seconds')
    #     print('Create file ' + file_name + '.....')
    #     f = open(file_name,'wb')

    #     np.save(f,combination_data)
    #     print('The file is saved')

    # elif mode == '2':
    #     # odd = list(iter.combinations(range(1,50,2),4))
    #     # even = list(iter.combinations(range(2,49,2),4))
    #     odd = list(iter.combinations(range(1,10,2),4))
    #     even = list(iter.combinations(range(2,11,2),4))
    #     input_file_name = input('Please input the file including lottery number: ')
    #     print('Open the file ' + input_file_name + " ......")
    #     start_name = input('Please input the start file number: ')

    #     f2 = open(input_file_name,'r')
    #     tmp = f2.read().split('\n')
    #     tmp = tmp[:len(tmp)-1]
    #     winner_number = [[int(j) for j in (i.split(','))] for i in tmp]

    #     # make winner number dictionary array
    #     winner_number_dict = []
    #     for ii in winner_number:
    #         winner_number_dict.append(make_dict(ii))

    #     # making combination test of odd and even
    #     time0 = time.clock()
    #     com_num = len(odd)*len(even)

    #     # calculate every combination

    #     for ii in range(0, len(winner_number_dict)):
    #         file_name = str(ii+int(start_name)) + '.data'
    #         print('Calculating the file: ' + file_name + ' ...')
    #         # combination_data = np.array([False]*com_num,np.bool)
    #         combination_data = [False] * com_num

    #         flag = 0
    #         for i in odd:
    #             for j in even:
    #                 combination_data[flag] = compare2(i, j, winner_number_dict[ii])
    #                 flag += 1

    #         print('Create file ' + file_name + '.....')
    #         f = open(file_name,'wb')
    #         combination_data_np = np.array(combination_data)
    #         np.save(f,combination_data_np)

    #         print('Save file ' + file_name + ' complete!')


    #     time2 = time.clock() - time0
    #     print('The time elasped: ' + str(time2) + ' seconds')

    # elif mode == '3':
    #     load_file_name_first = int(input('Please enter the first file name you want to analyse and load: '))
    #     load_file_name_last = int(input('Please enter the last file name you want to analyse and load: '))

    #     odd = list(iter.combinations(range(1,50,2),4))
    #     even = list(iter.combinations(range(2,49,2),4))
    #     com_num = len(odd)*len(even)

    #     # the bucket array to store the number
    #     # base_array = np.array([0] * com_num, np.int8)
    #     base_array = [0] * com_num
    #     # dict for continuous number
    #     # overall_dict = np.array([0] * 50000, np.int16)
    #     overall_dict = [0] * 50000
    #     # dict initialization
    #     # dict_init(overall_dict,10000)

    #     end_array = np.array([True]*com_num, np.bool)

    #     # make a output file
    #     # f_write = open(str(load_file_name_first) + "_" + str(load_file_name_last) + ".analyse" )
    #     start_time = time.clock()
    #     for ii in range(load_file_name_first,load_file_name_last+1):
    #         print("Analyzing file: " + str(ii) + ".data...")
    #         f_read = open(str(ii) + ".data", "rb")
    #         target_input = (np.load(f_read)).tolist()
    #         analyse_zero(base_array, target_input, overall_dict, com_num)
    #         f_read.close()

    #     last_win_info = base_array.copy()
    #     analyse_zero(base_array, end_array, overall_dict, com_num)
    #     overall_time = time.clock() - start_time

    #     print("The time elpased = " + str(overall_time) + " seconds" )
    #     f_save_chart = open(str(load_file_name_first) + "_" + str(load_file_name_last) + ".analyse",'wb')
    #     np.save(f_save_chart, overall_dict)
    #     f_last_save = open(str(load_file_name_first) + "_" + str(load_file_name_last) + "last_only.analyse",'wb' )
    #     np.save(f_last_save,np.array(base_array,np.int16) - np.array(last_win_info,np.int16))
    #     print("Save file OK")

    # elif mode == '4':
    #     load_old_overall_dict = input('Please enter the analyse file that you want to append:')
    #     load_file_name_first = int(load_old_overall_dict.split('_')[0])
    #     load_file_name_last = int(input('Please enter the last file name you want to analyse and load: '))

    #     odd = list(iter.combinations(range(1,50,2),4))
    #     even = list(iter.combinations(range(2,49,2),4))
    #     com_num = len(odd)*len(even)

    #     # the bucket array to store the number
    #     # base_array = np.array([0] * com_num, np.int8)
    #     base_array = [0] * com_num
    #     # dict for continuous number
    #     # overall_dict = np.array([0] * 50000, np.int16)
    #     overall_dict = np.load(load_old_overall_dict)
    #     # dict initialization
    #     # dict_init(overall_dict,10000)


    #     # make a output file
    #     # f_write = open(str(load_file_name_first) + "_" + str(load_file_name_last) + ".analyse" )
    #     start_time = time.clock()
    #     for ii in range(int(load_old_overall_dict.split('_')[1].split('.')[0])+1,load_file_name_last+1):
    #         print("Analyzing file: " + str(ii) + ".data...")
    #         f_read = open(str(ii) + ".data", "rb")
    #         target_input = (np.load(f_read)).tolist()
    #         analyse_zero(base_array, target_input, overall_dict, com_num)
    #         f_read.close()
    #     overall_time = time.clock() - start_time

    #     print("The time elpased = " + str(overall_time) + " seconds" )
    #     f_save_chart = open(str(load_file_name_first) + "_" + str(load_file_name_last) + ".analyse",'wb')
    #     np.save(f_save_chart, overall_dict)
    #     print("Save file OK")











if __name__ == "__main__":
    main()
