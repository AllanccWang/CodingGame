#https://www.codingame.com/training/medium/plague-jr
#concept: BFS; n-ary-tree
import sys
import math
from collections import deque

class Graph:
    # Initialisation of graph
    def __init__(self, vertices):
        # No. of vertices
        self.vertices = vertices
        # adjacency list
        self.adj = {i: [] for i in range(self.vertices)}
    def addEdge(self, u, v):
        # add u to v's list
        self.adj[u].append(v)
        # since the graph is undirected
        self.adj[v].append(u)
    # method return farthest node and its distance from node u
    def BFS(self, u):
        # marking all nodes as unvisited
        visited = [False for i in range(self.vertices + 1)]
        # mark all distance with -1
        distance = [-1 for i in range(self.vertices + 1)]
        # distance of u from u will be 0
        distance[u] = 0
        # in-built library for queue which performs fast operations on both the ends
        queue = deque()
        queue.append(u)
        # mark node u as visited
        visited[u] = True
        while queue:
            # pop the front of the queue(0th element)
            front = queue.popleft()
            # loop for all adjacent nodes of node front
            for i in self.adj[front]:
                if not visited[i]:
                    # mark the ith node as visited
                    visited[i] = True
                    # make distance of i , one more than distance of front
                    distance[i] = distance[front]+1
                    # Push node into the stack only if it is not visited already
                    queue.append(i)
        maxDis = 0
        # get farthest node distance and its index
        for i in range(self.vertices):
            if distance[i] > maxDis:
                maxDis = distance[i]
                nodeIdx = i
        return nodeIdx, maxDis
    # method prints longest path of given tree
    def LongestPathLength(self):
        # first DFS to find one end point of longest path
        node, Dis = self.BFS(0)
        # second DFS to find the actual longest path
        node_2, LongDis = self.BFS(node)
        #print('Longest path is from', node, 'to', node_2, 'of length', LongDis)
        return LongDis
n=int(input())
G=Graph(n+1)
for i in range(n):
    a,b=[int(j) for j in input().split()]
    G.addEdge(a,b)
    G.addEdge(b,a)
#longest distance between nodes -> LongDis
print(math.ceil(G.LongestPathLength()*0.5))
