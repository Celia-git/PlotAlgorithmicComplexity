############################# ASSIGNMENT COMPLETED BY CELIA HOUGH AND ETHAN KERNLEY ALONE ##########################################

import time
import matplotlib.pyplot as plt
import numpy as np
import sys

def quicksort_lomuto(array, low, high):
    if low < high:
        sec = lomuto(array, low, high)
        quicksort_lomuto(array, low, sec - 1)
        quicksort_lomuto(array, sec + 1, high)
    return array

def quicksort_hoare(array, low, high):

    if low < high:
        sec = hoare(array, low, high)
        quicksort_hoare(array, low, sec - 1)
        quicksort_hoare(array, sec + 1, high)
    return array

def lomuto(array, low, high):

    p = array[low]
    s = low

    for i in range(low + 1, high + 1):
        if array[i] < p:
            s = s + 1
            array[s], array[i] = array[i], array[s]
    array[low], array[s] = array[s], array[low]
    return s


def hoare(array, low, high):

    p = array[low]
    i = low
    j = high + 1

    while True:

        i = i + 1
        while i <= high and array[i] < p:
            i = i + 1
        j = j - 1
        while j >= low and array[j] > p:
            j = j - 1
        if i >= j:
            array[low], array[j] = array[j], array[low]
            return j

        array[i], array[j] = array[j], array[i]


def merge_sort(A):
    n = len(A)
    if n == 1:
        return A 
    mid = n //2
    L = merge_sort(A[0:mid])
    R = merge_sort(A[mid:n])
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
                merge_start_time = time.perf_counter()
                merge_result = str(merge_sort(line))
                merge_end_time = time.perf_counter()
                outfile.write(str(merge_result))
                ms_runtimes.append(merge_end_time-merge_start_time)

    with open(array_outputs[1], "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                lomuto_start_time = time.perf_counter()
                lomuto_result = str(quicksort_lomuto(line, 0, len(line)-1))
                lomuto_end_time = time.perf_counter()
                outfile.write(str(lomuto_result))
                qslomuto_runtimes.append(lomuto_end_time-lomuto_start_time)
    
    with open(array_outputs[2], "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                hoare_start_time = time.perf_counter()
                hoare_result = quicksort_hoare(line, 0, len(line)-1)
                hoare_end_time = time.perf_counter()
                outfile.write(str(hoare_result))
                qshoare_runtimes.append(hoare_end_time-hoare_start_time)
    
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



if __name__=="__main__":
    plot_times()