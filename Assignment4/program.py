############################# ASSIGNMENT COMPLETED BY CELIA HOUGH AND ETHAN KERNLEY ALONE ##########################################

import time
import matplotlib.pyplot as plt
import numpy as np
import sys


def merge_sort(A):
    n = len(A)
    if n == 1:
        return A 
    mid = n //2
    L = merge_sort(A[0:mid])
    R = merge_sort(A[mid+1:n])
    return merge(L, R)

def merge(A, B):
    p = len(A)
    q = len(B)
    C = [None]*(p+q)
    i, j, k = 0, 0, 0

    while (i < p) and (j < q):
        if A[i] < B[j]:
            C[k] = A[i]
            i += 1
        else:
            C[k] = B[j]
            j += 1
        k += 1
    
    if i > p:
        C[k:p+q] = B[j:q]
    else:
        C[k:p+q] = A[i:p]
    return C

def quicksort_lomuto(A):
    pass

def quicksort_hoare(A):
    pass

# Runs the three algo
def test_sort_sequences()->list:
    sys.setrecursionlimit(2000)
    line_lengths = []
    ms_runtimes = []
    qslomuto_runtimes = []
    qshoare_runtimes = []
    array_outputs = ["MSOutputs.txt", "QSLomutoOutputs.txt", "QSHoareOutputs.txt"]
    with open(array_outputs[0], "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line_lengths.append(len(line))
                line = [int(x) for x in line.split()]
                lin_start_time = time.perf_counter()
                lin_result = str(merge_sort(line))
                lin_end_time = time.perf_counter()
                outfile.write(lin_result)
                ms_runtimes.append(lin_end_time-lin_start_time)

    with open(array_outputs[1], "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                bin_start_time = time.perf_counter()
                bin_result = str(quicksort_lomuto(line))
                bin_end_time = time.perf_counter()
                outfile.write(bin_result)
                qslomuto_runtimes.append(bin_end_time-bin_start_time)
    
    with open(array_outputs[2], "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                doub_start_time = time.perf_counter()
                doub_result = quicksort_hoare(line)
                doub_end_time = time.perf_counter()
                outfile.write(doub_result)
                qshoare_runtimes.append(doub_end_time-doub_start_time)
    
    with open("runtimes.txt", "w") as outfile:
        for i in range(len(qslomuto_runtimes)):
            outfile.write(str((ms_runtimes[i], qslomuto_runtimes[i], qshoare_runtimes[i])))                    

    return [line_lengths, ms_runtimes, qslomuto_runtimes, qshoare_runtimes]
    
def plot_times():
    [line_lengths, ms_runtimes, qslomuto_runtimes, qshoare_runtimes] = test_sort_sequences()
    p1 = plt.plot(np.array(line_lengths), np.array(ms_runtimes), label="Merge Sort Time")
    p2 = plt.plot(np.array(line_lengths), np.array(qslomuto_runtimes), label="QS Lomuto Time")
    p3 = plt.plot(np.array(line_lengths), np.array(qshoare_runtimes), label="QS Hoare time")
    plt.legend(loc="upper left", title="Time Complexity of Algorithms")

    plt.show()


def debug():
    print(merge_sort([3, 1, 5,6, 7, 2,1]))

if __name__=="__main__":
    debug()
    #plot_times()