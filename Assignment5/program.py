############################# ASSIGNMENT COMPLETED BY CELIA HOUGH AND ETHAN KERNLEY ALONE ##########################################

import time
import matplotlib.pyplot as plt
import numpy as np
import sys



def DFSRecur(Graph, Nodes):

    visited = [0] * 50
    ConCom = 0
    for x in Nodes:
        if visited[x - 1] == 0:
            ConCom += 1
            dfs(x, Graph, visited)

    return ConCom



def dfs(Node, Graph, visited):

    visited[Node - 1] = 1
    for x in Graph[Node - 1]:
        if visited[x - 1] == 0:
            dfs(x, Graph, visited)



def DFSStack(Graph, Nodes):

    visited = [0] * 50
    ConCom = 0
    stack = []

    for x in Nodes:

        if visited[x - 1] == 0:
            ConCom += 1
            stack.append(x)
            while len(stack) != 0:
                cur = stack.pop()
                if visited[cur - 1] == 0:
                    visited[cur - 1] = 1
                    for y in Graph[cur - 1]:
                        if visited [y - 1] == 0:
                            stack.append(y)

    return ConCom

def BFS(Graph, Nodes):

    visited = [0] * 50

    ConCom = 0

    for x in Nodes:

        if visited[x - 1] == 0:

            ConCom += 1

            bfs(x, Graph, visited)

    return ConCom

    

def bfs(Node, Graph, visited):

    visited[Node - 1] = 1

    queue = [Node]

    while len(queue) != 0:

        cur = queue.pop()

        for y in Graph[cur - 1]:

            if visited[y - 1] == 0:

                visited[y - 1] = 1

                queue = [y] + queue


# Runs the three algo
def test_sort_sequences()->list:
    sys.setrecursionlimit(2000)
    dfs_stack_runtimes = []
    dfs_rec_runtimes = []
    bfs_runtimes = []
    array_outputs = ["DFSRecOutputs.txt", "DFSStackOutputs.txt", "BFSOutputs.txt"]
    all_graphs=[]
    all_nodes=[]
    graph_indices=[]
    with open("random_graphs.txt", "r") as file:
        adjacency_list=[]
        nodes=[]
        for line in file:
            if line == "\n":
                all_graphs.append(adjacency_list)
                all_nodes.append(nodes)
                adjacency_list=[]
                nodes=[]
                continue
            nums = line.split(": ")[1]
            adjacency_list.append([int(x) for x in nums.split()])
            nodes.append(int(line.split(": ")[0]))
    
    with open(array_outputs[0], "a") as dfs_rec_outfile, open(array_outputs[1], "a") as dfs_stack_outfile, open(array_outputs[2], "a") as bfs_outfile:
        for i in range(len(all_nodes)):
            dfsr_start_time = time.perf_counter()
            dfsr_result = str(DFSRecur(all_graphs[i], all_nodes[i]))
            dfsr_end_time = time.perf_counter()
            dfs_rec_outfile.write(str(dfsr_result)+"\n")
            dfs_rec_runtimes.append(dfsr_end_time-dfsr_start_time)

            dfss_start_time = time.perf_counter()
            dfss_result = str(DFSStack(all_graphs[i], all_nodes[i]))
            dfss_end_time = time.perf_counter()
            dfs_stack_outfile.write(str(dfss_result)+"\n")
            dfs_stack_runtimes.append(dfss_end_time-dfss_start_time)
            
            bfs_start_time = time.perf_counter()
            bfs_result = str(BFS(all_graphs[i], all_nodes[i]))
            bfs_end_time = time.perf_counter()
            bfs_outfile.write(str(bfs_result)+"\n")
            bfs_runtimes.append(bfs_end_time-bfs_start_time)

    with open("runtimes.txt", "a") as outfile:
        for i in range(len(bfs_runtimes)):
            outfile.write(str((dfs_rec_runtimes[i], dfs_stack_runtimes[i], bfs_runtimes[i])))
            outfile.write("\n")
            graph_indices.append(i)                    

    return [graph_indices, dfs_rec_runtimes, dfs_stack_runtimes, bfs_runtimes]
    
def plot_times():
    [graph_idx, dfs_rec_runtimes, dfs_stack_runtimes, bfs_runtimes] = test_sort_sequences()
    p1 = plt.plot(np.array(graph_idx), np.array(dfs_rec_runtimes), label="Depth First Recursive Time")
    p2 = plt.plot(np.array(graph_idx), np.array(dfs_stack_runtimes), label="Depth First Stack Time")
    p3 = plt.plot(np.array(graph_idx), np.array(bfs_runtimes), label="Breadth First time")
    plt.legend(loc="upper left", title="Time Complexity of Algorithms")

    plt.show()



if __name__=="__main__":
    plot_times()