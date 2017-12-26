import itertools as iter
import numpy as np
import time



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

def make_dict(a6):
    a6_dict = dict()
    for i in a6:
        a6_dict[i] = 1
    return a6_dict


def analyse_zero(base_array, target_input, overall_dict):
    len_array = len(target_input)
    for i in range(0,len_array):
        if target_input[i] == True:
            base_array[]




def main():
    

    print('Welcome to the lottery combination system')
    mode = input('Please enter the calculation mode: ')

    if mode == '1':

        odd = list(iter.combinations(range(1,50,2),4))
        even = list(iter.combinations(range(2,49,2),4))
        winner_number_raw = input('Please input the winner number: \n').split(',') # make string array to int 
        file_name = input('Plase enter the file name: ')
        winner_number = [int(num) for num in winner_number_raw]

        winner_number_dict = make_dict(winner_number)   # make winner number bucket 

        # making combination test of odd and even
        time0 = time.clock()
        com_num = len(odd)*len(even)
        combination_data = np.array([False]*com_num,np.bool)

        flag = 0
        for i in odd:
            for j in even:
                combination_data[flag] = compare2(i, j, winner_number_dict)
                flag += 1


        time2 = time.clock() - time0

        print('The time elasped: ' + str(time2) + ' seconds')
        print('Create file ' + file_name + '.....')
        f = open(file_name,'wb')

        np.save(f,combination_data)
        print('The file is saved')

    elif mode == '2':
        odd = list(iter.combinations(range(1,50,2),4))
        even = list(iter.combinations(range(2,49,2),4))
        input_file_name = input('Please input the file including lottery number: ')
        print('Open the file ' + input_file_name + " ......")

        f2 = open(input_file_name,'r')
        tmp = f2.read().split('\n')
        winner_number = [i.split() for i in tmp]

        # make winner number dictionary array
        winner_number_dict = []
        for ii in winner_number:
            winner_number_dict.append(make_dict(ii))
        
        # making combination test of odd and even
        time0 = time.clock()
        com_num = len(odd)*len(even)

        # calculate every combination

        for ii in range(0, len(winner_number_dict)):
            file_name = str(ii) + '.data'
            print('Calculating the file: ' + file_name + ' ...')
            combination_data = np.array([False]*com_num,np.bool)

            flag = 0
            for i in odd:
                for j in even:
                    combination_data[flag] = compare2(i, j, winner_number_dict[ii])
                    flag += 1            

            print('Create file ' + file_name + '.....')
            f = open(file_name,'wb')

            np.save(f,combination_data)            

            print('Save file ' + file_name + ' complete!')

        
        time2 = time.clock() - time0
        print('The time elasped: ' + str(time2) + ' seconds')

    elif mode == '3':
        load_file_name_first = int(input('Please enter the first file name you want to analyse and load: '))
        load_file_name_last = int(input('Please enter the last file name you want to analyse and load: '))

        odd = list(iter.combinations(range(1,50,2),4))
        even = list(iter.combinations(range(2,49,2),4))
        com_num = len(odd)*len(even)

        # the bucket array to store the number
        base_array = np.array([0] * com_num, np.int8)



        f_write = open(str(load_file_name_first) + "_" + str(load_file_name_last) + ".analyse" )

        for ii in range(load_file_name_first,load_file_name_last+1):









if __name__ == "__main__":
    main()