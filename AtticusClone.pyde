'''Atticus Clone
https://twitter.com/AtticusBones/status/880081178178576384
June 28, 2017'''

from node import Grid
sz = 5
grids = [] #list for grids Grid(sz)


def setup():
    global grids,sz
    size(600,600)
    #fill the grids list with unique grids
    for i in range(22**2):
        grids.append(Grid(sz))
    
def draw():
    global grids
    background(255) #white
    #add the grid to rows and columns
    for j in range(22):
        for k in range(22):
            pushMatrix()
            #go to the location
            translate(j*6*sz, k*6*sz)
            #display 1 grid
            grids[k+22*j].display()
            popMatrix()
            