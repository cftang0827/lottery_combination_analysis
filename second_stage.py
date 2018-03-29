import os 
import time
import itertools as iter
from analyse_zero import analyse_zero
from tqdm import tqdm
import numpy as np

def main():
    load_file_name_first = int(input('請輸入要進行第二階段分析的開始檔案: '))
    load_file_name_last = int(input('請輸入要進行第二階段分析的最後檔案: '))
    odd = list(iter.combinations(range(1,50,2),4))
    even = list(iter.combinations(range(2,49,2),4))
    com_num = int(len(odd)*len(even))    
    try:
        ba_npz_tmp = np.load(os.path.join('second_stage_data','base_array_{}.npz'.format(str(load_file_name_first-1))) )
        base_array = ba_npz_tmp['data']
        od_npz_tmp = np.load(os.path.join('second_stage_data','overall_dict_{}.npz'.format(str(load_file_name_first-1))) )
        overall_dict = od_npz_tmp['data']
    except:
        print('讀取前期資料錯誤，請檢查second_stage_data資料夾內是否有前一期的npz資料，結束')
        exit()
    end_array = np.array([True]*com_num, dtype=np.int)
    start_time = time.clock()
    for ii in tqdm(range(load_file_name_first,load_file_name_last+1), ascii=True):
        print("正在分析第 {} 期數資料: {}.data...".format(str(ii),str(ii)) )
        try:
            f_read = open(os.path.join('data',str(ii)) + ".data", "rb")
            target_input = (np.load(f_read).astype(np.bool).astype(np.int))
            f_read.close()  
        except:
            print('讀取data資料錯誤，請檢查data資料夾內是否有正確資料，結束')
            exit()
        analyse_zero(base_array, target_input, overall_dict)
        # print(str(ii)+'.data')
        # print(base_array)
        np.savez_compressed(os.path.join('second_stage_data','base_array_{}'.format(str(ii))), data=base_array)
        np.savez_compressed(os.path.join('second_stage_data','overall_dict_{}'.format(str(ii))), data=overall_dict )
        # print(overall_dict[0:9])


    overall_time = time.clock() - start_time
    print("總共花費時間 = " + str(overall_time) + " 秒" )
    print("第二階段完成")

if __name__ == '__main__':
    main()
