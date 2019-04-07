from tkinter import *
from core.core import *




class App(Tk):
    canvas_size = 0
    canvas = None
    timer = 100
    game = None
    start_button = None
    cell_size = 0
    variable = None

    simulate_flag = False;

    def __init__(self, geometry, canvas_size, grid_size, **Arguments):
        Tk.__init__(self, **Arguments)
        self.geometry(geometry)
        self.resizable(width=FALSE, height=FALSE)
        self.title("Game of Life")
        self.tk_setPalette(background="white")

        self.game = LifeGame(grid_size)

        self.canvas_size = canvas_size

        self.canvas = Canvas(self, width=self.canvas_size, height=self.canvas_size, bg='green');
        self.canvas.grid(row=0, column=0, columnspan=4)

        self.canvas.bind("<Button-1>", self.on_click)

        close_button=Button(self, text="Close", command=self.quit)
        close_button.grid(row=1, column = 3)

        self.start_button = Button(self, text="Start simulation", command=self.start_stop)
        self.start_button.grid(row=1, column=0)

        reset_button = Button(self, text="Reset", command=self.reset)
        reset_button.grid(row=1, column=1)

        self.variable = StringVar(self)
        self.variable.set("10ms") # default value

        w = OptionMenu(self, self.variable, "1ms","10ms", "100ms", "200ms")
        w.grid(row=2, column=0)

        self.cell_size = int(self.canvas_size/self.game.get_grid_size())

        self.show_grid()




    def show_grid(self):
        grid = self.game.get_grid()
        self.canvas.delete("all")
        grid_size = len(grid)
        for i in range(grid_size):
            for j in range(grid_size):
                x0 = self.cell_size*j+3
                x1 = self.cell_size*(j+1)+1
                y0 = self.cell_size * i+3
                y1 = self.cell_size * (i+1)+1
                color = 'black'
                if(grid[i][j] == 1):
                    color = 'white'
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)


    def simulate(self):
        if self.simulate_flag:
            self.show_grid()
            self.game.step()

            self.after(self.timer, self.simulate)


    def start_stop(self):
        self.simulate_flag = not self.simulate_flag
        if self.simulate_flag:
            new_text = "Stop simulation"
        else:
            new_text = "Start simulation"
        timer_string = self.variable.get()
        if timer_string == "1ms":
            self.timer = 1
        elif timer_string == "10ms":
            self.timer = 10
        elif timer_string == "100ms":
            self.timer = 100
        elif timer_string == "200ms":
            self.timer = 200
        else:
            self.timer = 100


        self.simulate()
        self.start_button.config(text=new_text)

    def reset(self):
        if self.simulate_flag:
            self.start_stop()
        self.game.reset()
        self.show_grid()

    def on_click(self, event):
        if not self.simulate_flag:
            j = event.x//self.cell_size
            i = event.y//self.cell_size
            self.game.change_cell(i,j)
            self.show_grid()
