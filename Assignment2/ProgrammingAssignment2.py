#############################################################################################################################################################
####################################### CELIA HOUGH AND ETHAN KERLEY WORKED ON THIS PROGRAM ALONE ######################################################
############################################################################################################################################################

import time
import matplotlib.pyplot as plt
import numpy as np


def selection_sort(A:list, n:int)->list:
    
    for i in  range(n-1):
        c_min=i
        for j in range(i+1, n):
            if A[j] < A[c_min]:
                c_min = j
        A[i], A[c_min] = A[c_min], A[i]

    return A


def bubble_sort(A:list, n:int)->list:

    for i in range(1, n):
        for j in range(0, n-i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

    return A


def test_unsorted_sequences()->list:
    line_lengths = []
    sel_runtimes = []
    bub_runtimes = []
    def_runtimes = []
    with open("SelSortOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                sel_start_time = time.perf_counter()
                sel_result = str(selection_sort(line, len(line)))
                sel_end_time = time.perf_counter()
                outfile.write(sel_result)
                line_lengths.append(len(line))
                sel_runtimes.append(sel_end_time-sel_start_time)

    with open("BubSortOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                bub_start_time = time.perf_counter()
                bub_result = str(bubble_sort(line, len(line)))
                bub_end_time = time.perf_counter()
                outfile.write(bub_result)
                bub_runtimes.append(bub_end_time-bub_start_time)
    
    with open("DefSortOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                def_start_time = time.perf_counter()
                def_result = str(sorted(line))
                def_end_time = time.perf_counter()
                outfile.write(def_result)
                def_runtimes.append(def_end_time-def_start_time)
    
    with open("clocktimes.txt", "w") as outfile:
        for i in range(len(line_lengths)):
            outfile.write(str((sel_runtimes[i], bub_runtimes[i], def_runtimes[i])))                    

    return [line_lengths, sel_runtimes, bub_runtimes, def_runtimes]
    

def plot_times():
    [line_lengths, sel_runtimes, bub_runtimes, def_runtimes] = test_unsorted_sequences()
    p1 = plt.plot(np.array(line_lengths), np.array(sel_runtimes), label="Selection Runtimes")
    p2 = plt.plot(np.array(line_lengths), np.array(bub_runtimes), label="Bubble Runtimes")
    p3 = plt.plot(np.array(line_lengths), np.array(def_runtimes), label="Built in Default Runtimes")
    plt.legend(loc="upper left", title="Time Complexity of Algorithms")

    plt.show()
            

if __name__=="__main__":
    plot_times()



 
