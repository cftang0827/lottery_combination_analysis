import numpy as np
import itertools as iter
import os


def main():
	print('初始化...')
	odd = list(iter.combinations(range(1,11,2),4))
	even = list(iter.combinations(range(2,10,2),4))
	com_num = int(len(odd)*len(even))  
	base_array = np.array([0]*com_num)
	overall_dict = np.array([0]*com_num)
	np.savez_compressed(os.path.join('./','base_array_{}'.format(str(0))), data=base_array)
	np.savez_compressed(os.path.join('./','overall_dict_{}'.format(str(0))), data=overall_dict )
	print('初始化完成')
	input('任意鍵結束')



if __name__ == '__main__':
	main()