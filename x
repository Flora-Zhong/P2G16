import mandelbrot
from matplotlib import pyplot as plt

grid = mandelbrot.get_complex_grid(-2+1.25j, 0.5-1.25j, 0.01)
colors = mandelbrot.get_escape_time_color_arr(grid, 30)

plt.imshow(colors, cmap="Greys")
