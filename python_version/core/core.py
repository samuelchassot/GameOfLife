from functools import reduce
from joblib import Parallel, delayed

class LifeGame(object):
    """docstring for LifeGame."""
    grid_size = 0
    grid=[]
    new_grid = []
    def __init__(self, grid_size):
        super(LifeGame, self).__init__()
        self.grid_size = grid_size
        self.reset()

    def step_line(self,i):
        for j in range(self.grid_size):
            self.new_grid[i][j] = self.update_cell(i,j)

    def step(self):
        self.new_grid = [[0]*self.grid_size for i in range(self.grid_size)]

        Parallel(n_jobs=16, require='sharedmem')(delayed(self.step_line)(i) for i in range(self.grid_size))

        self.grid = self.new_grid.copy()



    def update_cell(self, i, j):
        neighbours = []
        for ix in range(-1, 2) :
            for jx in range(-1, 2):
                if not (ix == 0 and jx == 0) :
                    neighbours.append(self.grid[(i+ix)%self.grid_size][(j+jx)%self.grid_size])

        n_alive = reduce((lambda x,y: x+y), neighbours)
        state = self.grid[i][j]
        next_state = (n_alive==3) or (state == 1 and n_alive==2)


        return next_state

    def change_cell(self, i, j):
        self.grid[i][j] = (self.grid[i][j]+1)%2

    def get_grid(self):
        return self.grid.copy()

    def get_grid_size(self):
        return self.grid_size

    def reset(self):
        self.grid = [[0]*self.grid_size for i in range(self.grid_size)]
