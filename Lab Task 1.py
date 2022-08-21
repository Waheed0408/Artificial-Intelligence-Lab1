inp = open("input.txt", "r")
inp = inp.read() #input from txt file

b = inp.splitlines() #linewise split
list1 = []

for i in b:
    list1.append(i.split()) #appending to 2D list



def Deepening(list1, i, j):
    c = 1
    for r in range(i-1, i+2): #neighbour check
        for col in range(j-1, j+2):
            if r<0 or col<0 or r>=(len(list1)) or col>=(len(list1[0])): #check in range
                continue
            if list1[r][col] == 'Y':
                list1[r][col] = 'X' #not repetetive check
                c += Deepening(list1, r, col)  

    return c

def searchY(list1):
    maximum = []
    for i in range(len(list1)): #row iteration
        for j in range(len(list1[0])): #col iteration
            if list1[i][j] == 'Y':
                list1[i][j] = 'X' #not repetetive check
                an=Deepening(list1, i, j)
                maximum.append(an)
    return maximum


a = searchY(list1)
a.sort()
print(a[-1])

#task2

inp = open('Question2 input1.txt','r')
a = inp.read().splitlines()
r = int(a[0])
c = int(a[1])
a = a[2:]
b = []

for i in a:
    temp = i.split()
    b.append(temp)

from collections import deque
 
 
# possiblity of 8 moves
# diagonals, up down left right
row = [0,0,1,-1]
col = [1,-1,0,0]
 
 
# safe checking to go to x,y
 
def isSafe(mat, x, y, processed):
    return (x >= 0 and x < len(processed)) and (y >= 0 and y < len(processed[0])) and mat[x][y] == 'H' and not processed[x][y]
 
 
def BFS(mat, processed, i, j):
 
    # empty queue
    q = deque()
    q.append((i, j))
 
 
    # iterate
    while q:
        x, y = q.popleft()
 
        #check all possible movements
        for k in range(len(row)):
            # skip invalid location
            
            if isSafe(mat, x + row[k], y + col[k], processed):       
                processed[x + row[k]][y + col[k]] = processed[x][y] +1
                q.append((x + row[k], y + col[k]))
                mat[x + row[k]][y + col[k]] = 'A' 
 
def time_survive(mat):
 
    if not mat or not len(mat):
        return 0
 #basecase
    
    (M, N) = (len(mat), len(mat[0]))
 
    # store processed
    processed = [[0 for x in range(N)] for y in range(M)]
 
    for i in range(M):
        for j in range(N):
            #  BFS
            if mat[i][j] == 'A' and  processed[i][j]==0:
                BFS(mat, processed, i, j)

    maxT=0
    for i in processed:
        maxT=max(max(i),maxT)
    print('Time: '+str(maxT)+' minutes')

    survi=0
    for i in mat:
      for j in i:
        if j=='H':
          survi=survi+1
    print(str(survi)+' survived')

time_survive(b)
