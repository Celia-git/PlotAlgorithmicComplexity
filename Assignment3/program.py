############################# ASSIGNMENT COMPLETED BY CELIA HOUGH AND ETHAN KERNLEY ALONE ##########################################

import time
import matplotlib.pyplot as plt
import numpy as np


# Sorts input array, A, using linear insertion
# Returns A
def linear_insertion_sort(A):
    n = len(A)
    for i in range(1, n):
        temp = A[i]
        j = i-1
        while(j>=0) and temp<A[j]:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = temp
    return A

# Sorts input array, A, using binary recursive insertion
# Returns A
def binary_insertion_sort(A):
    n = len(A)
    if n==1:
        return A
    B = binary_insertion_sort(A[:n-2])
    temp = A[n]
    while j >= 0 and temp < B[j]:
        B[j+1] = B[j]
        j = j-1
    B[j+1] = temp
    return A

# Sorts input doubly-linked list, doubly_linked, using linear_insertion_sort
# Return doubly_linked
def doubly_linked_sort(doubly_linked):
    return doubly_linked


# Runs the three algo
def test_sort_sequences()->list:
    lin_runtimes = []
    bin_runtimes = []
    doub_runtimes = []
    with open("NonRecOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                lin_start_time = time.perf_counter()
                lin_result = str(linear_insertion_sort(line, len(line)))
                lin_end_time = time.perf_counter()
                outfile.write(lin_result)
                lin_runtimes.append(lin_end_time-lin_start_time)

    with open("BinInsOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                bin_start_time = time.perf_counter()
                bin_result = str(binary_insertion_sort(line, len(line)))
                bin_end_time = time.perf_counter()
                outfile.write(bin_result)
                bin_runtimes.append(bin_end_time-bin_start_time)
    
    with open("LinkedListOutputs.txt", "w") as outfile:
        with open("unsorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                doub_start_time = time.perf_counter()
                doub_result = str(sorted(line))
                doub_end_time = time.perf_counter()
                outfile.write(doub_result)
                doub_runtimes.append(doub_end_time-doub_start_time)
    
    with open("clocktimes.txt", "w") as outfile:
        for i in range(len(bin_runtimes)):
            outfile.write(str((lin_runtimes[i], bin_runtimes[i], doub_runtimes[i])))                    

    return [lin_runtimes, bin_runtimes, doub_runtimes]
    
def plot_times():
    [line_lengths, lin_runtimes, bin_runtimes, doub_runtimes] = test_sort_sequences()
    p1 = plt.plot(np.array(line_lengths), np.array(lin_runtimes), label="Selection Runtimes")
    p2 = plt.plot(np.array(line_lengths), np.array(bin_runtimes), label="Bubble Runtimes")
    p3 = plt.plot(np.array(line_lengths), np.array(doub_runtimes), label="Built in Default Runtimes")
    plt.legend(loc="upper left", title="Time Complexity of Algorithms")

    plt.show()
            

if __name__=="__main__":
    plot_times()
