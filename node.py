from random import choice
    
class Node:
    def __init__(self,x,y,num):
        self.x = x
        self.y = y
        self.num = num
        
    def display(self):
        fill(0)
        ellipse(self.x,self.y,10,10)
        
    def connect(self,other):
        strokeWeight(1)
        line(self.x,self.y,
             other.x,other.y)
        
nodes = ['placeholder']#so the first node will be 1
mirrornodes = ['placeholder']
#list for connections between nodes
connections = [[1,2],[1,4],
               [2,3],[2,4],[2,5],
               [3,5],[3,7],
               [4,5],[4,6],
               [5,6],[5,7],
               [6,7],[6,8],
               [7,8],[7,9],
               [8,9]]
    
class Grid:
    
    def __init__(self,sz):
        #create the nodes in the grid
        nodes.append(Node(0,0,1))
        nodes.append(Node(0,-sz,2))
        nodes.append(Node(0,-2*sz,3))
        nodes.append(Node(sz/2.0,-sz/2.0,4))
        nodes.append(Node(0.5*sz,-1.5*sz,5))
        nodes.append(Node(sz,-sz,6))
        nodes.append(Node(sz,-2*sz,7))
        nodes.append(Node(1.5*sz,-1.5*sz,8))
        nodes.append(Node(2*sz,-2*sz,9))
        #create the nodes which mirror over the diagonal line
        mirrornodes.append(Node(0,0,1))
        mirrornodes.append(Node(sz,0,2))
        mirrornodes.append(Node(2*sz,0,3))
        mirrornodes.append(Node(sz/2.0,-sz/2.0,4))
        mirrornodes.append(Node(1.5*sz,-0.5*sz,5))
        mirrornodes.append(Node(sz,-sz,6))
        mirrornodes.append(Node(2*sz,-sz,7))
        mirrornodes.append(Node(1.5*sz,-1.5*sz,8))
        mirrornodes.append(Node(2*sz,-2*sz,9))
        #randomly choose which nodes are connecting
        self.connectChoice = [choice([0,1]) for x in range(15)]
        
    def connect(self):
        #for every node that's connecting:
        for i,c in enumerate(self.connectChoice):
            if c == 1: #if the connection is active
                #connect the first node in the 2-list with the second
                nodes[connections[i][0]].connect(nodes[connections[i][1]])
                #also connect the reflections of those nodes
                mirrornodes[connections[i][0]].connect(mirrornodes[connections[i][1]])
    
    def display(self):
        #copy the upper right quadrant 
        # to all 4 quadrants by rotating
        for i in range(4):
            rotate(radians(90*i))
            self.connect()
            