import itertools as iter
import numpy as np

def compare(a1,a2,a6_dict):
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

if __name__ == "__main__":
    main()


def main():
    odd = list(iter.combinations(range(1,50,2),4))
    even = list(iter.combinations(range(2,49,2),4))
    winner_number_raw = input('Please input the winner number: \n').split(',') # make string array to int 
    winner_number = [int(num) for num in winner_number_raw]

    winner_number_dict = make_dict(winner_number)   # make winner number bucket 

    # making combination test of odd and even

    combination_data = np.array([],np.bool)

    for i in odd:
        for j in even:
            combination_data = np.append(combination_data,compare(i,j,winner_number_dict))
    


