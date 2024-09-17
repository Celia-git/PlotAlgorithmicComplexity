import time
import matplotlib.pyplot as plt
import numpy as np


def linear_search(A:list, x:int)->bool:
    for i in range(len(A)):
        if A[i]==x:
            return True
    return False


def binary_search(A:list, x:int)->bool:
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

def test_sorted_sequences()->dict:
    runtimes = {}
    with open("sequences_output.txt", "a") as outfile:
        with open("sorted_sequences.txt", "r") as file:
            for line in file:
                line = [int(x) for x in line.split()]
                lin_start_time = time.time()
                lin_result = linear_search(line, 500)
                lin_end_time = time.time()
                bin_start_time = time.time()
                bin_result = binary_search(line, 500)
                bin_end_time = time.time()
                outfile.write(str(lin_result) + " " + str(bin_result) + "\n")
                runtimes[len(line)] = (lin_end_time-lin_start_time, bin_end_time-bin_start_time)
    return runtimes
    
def plot_times():
    runtimes = test_sorted_sequences()
    x = np.array(runtimes.keys())
    y = np.array(runtimes.values())
    plt.plot(x, y)
    plt.show()
            
plot_times()



 
