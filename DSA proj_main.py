from tkinter import *
import tkinter as tk
import random as r
import time
from collections import deque
import heapq

def tksleep(t=1):
    ms = int(t*1000)
    root = tk._get_default_root('sleep')
    var = tk.IntVar(root)
    root.after(ms, var.set, 1)
    root.wait_variable(var)
def main_screen():
    main=Tk()
    main.geometry("500x200")
    main.title("MAZE SOLVER")
    Label(main, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
    Label(main,text='MAZE SOLVER',font=("Goudy Old Style", 30),bg='white').place(x=100,y=10)

     
    '''maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '.', '#'],
        ['#', '.', '#', '.', '#', '.', '#', '.', '#'],
        ['#', '.', '#', '.', '.', '.', '#', '.', '#'],
        ['#', '.', '#', '#', '#', '.', '#', '.', '#'],
        ['#', '.', '.', '.', '#', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]'''

    
    Button(main, text='GENERATE MAZE',font=("Goudy Old Style", 20),
           bg='white',bd=0,activebackground='white',command=lambda:generate_maze()).place(x=10,y=100)

def generate_maze():
    global maze
    maze = [
        ['#', '#', '#', '#', '#', '#', '#', '#', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '.', '.', '.', '.', '.', '.', '.', '#'],
        ['#', '#', '#', '#', '#', '#', '#', '#', '#']
    ]
    global l1
    l1=['#','.']
    solve=Tk()
    solve.geometry("1000x700")
    solve.title("MAZE SOLVER")
    Label(solve, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
    #Label(solve,text='MAZE GENERATED',font=("Goudy Old Style", 25),bg='white').place(x=160,y=10)
    a=100
    for i in range(0,9):
        Label(solve,text=i,font=("Goudy Old Style", 25),bg='white').place(x=a,y=10)
        a=a+50
    b=50
    for i in range(0,7):
        Label(solve,text=i,font=("Goudy Old Style", 25),bg='white').place(x=50,y=b)
        b=b+50
    b=50
    for row in range(len(maze)):
        a=100
        for col in range(len(maze[row])):
            #tksleep(0.1)
            if maze[row][col]=='#':
                
                Label(solve,text=maze[row][col],font=("Goudy Old Style", 30),bg='white',fg='red',borderwidth=2,relief='raised').place(x=a,y=b)
            elif maze[row][col]=='.':
                c=r.choice(l1)
                maze[row][col]=c
                if c=='#':
                    Label(solve,text=c,font=("Goudy Old Style", 30),bg='white',fg='red',borderwidth=2,relief='raised').place(x=a,y=b)
                else :
                    Label(solve,text=c,font=("Goudy Old Style", 30),bg='white',fg='blue').place(x=a,y=b)
                #Label(solve,text=j,font=("Goudy Old Style", 30),bg='white',fg='blue').place(x=a,y=b)
            a=a+50
            
        b=b+50

    Button(solve, text='GENERATE MAZE AGAIN',font=("Goudy Old Style", 20),
           bg='white',bd=2,activebackground='white',command=lambda:generate_maze()).place(x=600,y=50)

    Label(solve, text="START COORDINATES: ", font=("calibre",15),bg='white').place(x=600,y=120)
    Label(solve, text="ROW: ", font=("calibre",15),bg='white').place(x=600,y=190)
    x1=Entry(solve ,  font=("calibre",15),bg='#F2F2F2')
    x1.place(x=700,y=190)
    Label(solve, text="COLUMN: ", font=("calibre",15),bg='white').place(x=600,y=240)
    y1=Entry(solve ,  font=("calibre",15),bg='#F2F2F2')
    y1.place(x=700,y=240)
    
    Label(solve, text="END COORDINATES: ", font=("calibre",15),bg='white').place(x=600,y=310)
    Label(solve, text="ROW: ", font=("calibre",15),bg='white').place(x=600,y=360)
    x2=Entry(solve ,  font=("calibre",15),bg='#F2F2F2')
    x2.place(x=700,y=360)
    Label(solve, text="COLUMN: ", font=("calibre",15),bg='white').place(x=600,y=410)
    y2=Entry(solve ,  font=("calibre",15),bg='#F2F2F2')
    y2.place(x=700,y=410)
    
    Button(solve, text='SAVE',font=("Goudy Old Style", 12),
           bg='white',bd=2,activebackground='white',command=lambda:store_coordinates()).place(x=750,y=460)
    
    def store_coordinates():
        global s1
        s1=(int(x1.get()),int(y1.get()))
        global e1
        e1=(int(x2.get()),int(y2.get()))
        
        tksleep(0.1)
        Label(solve,text="SOLVE THE MAZE USING:",font=("Goudy Old Style", 20),bg='white').place(x=10,y=b+20)
        bfs_path=bfs(maze,s1,e1)
        dfs_path=dfs(maze,s1,e1)
        dij_path=dijkstra(maze,s1,e1)
        Button(solve, text='BFS',font=("Goudy Old Style", 20),
               bg='white',bd=2,activebackground='white',command=lambda:display_maze(maze,s1,e1,bfs_path,'SOLVED USING BFS')).place(x=10,y=b+70)
        Button(solve, text='DFS',font=("Goudy Old Style", 20),
               bg='white',bd=2,activebackground='white',command=lambda:display_maze(maze,s1,e1,dfs_path,'SOLVED USING DFS')).place(x=110,y=b+70)
        Button(solve, text='DIJKSTRA',font=("Goudy Old Style", 20),
               bg='white',bd=2,activebackground='white',command=lambda:display_maze(maze,s1,e1,dij_path,'SOLVED USING DIJKSTRA')).place(x=210,y=b+70)

    



def bfs(maze, start, end):
    
    #Label(solve,text='MAZE GENERATED',font=("Goudy Old Style", 25),bg='white').place(x=160,y=10)
    queue = deque([start])
    visited = set([start])
    parent = {}
    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            row, col = neighbor
            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                continue
            if maze[row][col] == '#' or neighbor in visited:
                continue
            queue.append(neighbor)
            visited.add(neighbor)
            parent[neighbor] = current
            
    return []

def dfs(maze, start, end):
    stack = [start]
    visited = set([start])
    parent = {}
    while stack:
        current = stack.pop()
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            row, col = neighbor
            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                continue
            if maze[row][col] == '#' or neighbor in visited:
                continue
            stack.append(neighbor)
            visited.add(neighbor)
            parent[neighbor] = current
    return []

def dijkstra(maze, start, end):
    distances = {start: 0}
    queue = [(0, start)]
    parent = {}
    while queue:
        (dist, current) = heapq.heappop(queue)
        if current == end:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        row, col = current
        neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            row, col = neighbor
            if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
                continue
            if maze[row][col] == '#':
                continue
            distance = distances[current] + 1
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                priority = distance
                heapq.heappush(queue, (priority, neighbor))
                parent[neighbor] = current
    return []

def display_maze( maze, start, end, found_path,k):
    BFS=Tk()
    BFS.geometry("600x500")
    BFS.title("MAZE SOLVER")
    Label(BFS, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
    Label(BFS,text=k,font=("Goudy Old Style", 20),bg='white').place(x=170,y=10)
    b= 50
    for row in range(len(maze)):
        a=100
        for col in range(len(maze[row])):
            tksleep(0.1)
            if (row, col) == start:
                Label(BFS, text='S', font=("Goudy Old Style", 30), bg='white', fg='blue').place(x=a, y=b)
            elif (row, col) == end:
                Label(BFS, text='E', font=("Goudy Old Style", 30), bg='white', fg='blue').place(x=a, y=b)
            elif (row, col) in found_path:
                Label(BFS, text='*', font=("Goudy Old Style", 30), bg='white', fg='green').place(x=a, y=b)
            else:
                if maze[row][col]=='#':
                    Label(BFS, text=maze[row][col], font=("Goudy Old Style", 30), bg='white', fg='red',borderwidth=2,relief='raised').place(x=a, y=b)
                else:
                    Label(BFS, text='.', font=("Goudy Old Style", 30), bg='white', fg='black').place(x=a, y=b)
                    
            a=a+50
        b=b+50




main_screen()


