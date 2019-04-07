from core.interface import *
import sys

canvas_size = int(float(sys.argv[1]))
grid_size = int(float(sys.argv[2]))
geometry = ""
geometry += str(canvas_size+10)
geometry += 'x'
geometry += str(canvas_size+100)
app = App(geometry, canvas_size, grid_size)
app.mainloop()
