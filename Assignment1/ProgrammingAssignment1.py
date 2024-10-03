#############################################################################################################################################################
####################################### CELIA HOUGH AND KATELYNN ATKINSON WORKED ON THIS PROGRAM ALONE ######################################################
############################################################################################################################################################

import time
import matplotlib.pyplot as plt
import numpy as np


def linear_search(A:list, x:int)->bool:
    if len(A)==0:
        return False
    for i in range(len(A)):
        if A[i]==x:
            return True
    return False


def binary_search(A:list, x:int)->bool:
    if len(A)==0:
        return False
    left = 0
    right = len(A)-1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == x:
            return True
        elif A[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return False

def test_sorted_sequences()->list:
    line_lengths = []
    lin_runtimes = []
    bin_runtimes = []
    with open("sequences_output.txt", "w") as outfile:
        with open("sorted_sequences.txt", "r") as file:
            i=0
            for line in file:
                line = [int(x) for x in line.split()]
                lin_start_time = time.perf_counter()
                lin_result = linear_search(line, 500)
                lin_end_time = time.perf_counter()
                bin_start_time = time.perf_counter()
                bin_result = binary_search(line, 500)
                bin_end_time = time.perf_counter()
                outfile.write(str(lin_result) + " " + str(bin_result) + "\n")
                line_lengths.append(len(line))
                lin_runtimes.append(lin_end_time-lin_start_time)
                bin_runtimes.append(bin_end_time-bin_start_time)
                i += 1
    return [line_lengths, lin_runtimes, bin_runtimes]
    
def plot_times():
    [line_lengths, lin_runtimes, bin_runtimes] = test_sorted_sequences()
    p1 = plt.plot(np.array(line_lengths), np.array(lin_runtimes), label="Linear Runtimes")
    p2 = plt.plot(np.array(line_lengths), np.array(bin_runtimes), label="Binary Runtimes")
    plt.legend(loc="upper left", title="Time Complexity of Algorithms")
    

    plt.show()
            

if __name__=="__main__":
    plot_times()



 
