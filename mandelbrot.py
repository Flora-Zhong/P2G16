import numpy as np

"""PART 1"""
def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """finding the max amount of times c has to go through the mandelbrot set before it escapes"""
    z = c  # Start at c (as given in assignment)
    if abs(z) > 2:
        return 0  # Escape immediately if magnitude exceeds 2

    for i in range(1, max_iterations + 1):  # Start count from 1 to match expected output
        z = z ** 2 + c  # Mandelbrot iteration
        if abs(z) > 2:
            return i  # Return number of iterations until escape

    return None  # Did not escape within max_iterations


"""PART 2"""

def get_complex_grid(top_left: complex, bottom_right: complex, step: float) -> np.ndarray:
    """

    Returns the gird of complex number range from the top left value to the bottom right value.

    Parameters
    ----------
    top_left : complex
        The top left corner of the coordinate of this grid.
    bottom_right : complex
        The bottom right corner of the coordinate of this grid.
    step : float
        The unit distance for this grid.

    Returns
    -------
    np.ndarray, The coordinates of the point.

    """
    top_left_real = np.real(top_left)
    top_left_imag = np.imag(top_left)
    bottom_right_real = np.real(bottom_right)
    bottom_right_imag = np.imag(bottom_right)
    if (top_left_real > bottom_right_real) or (top_left_imag < bottom_right_imag):
        return np.array([])
    real = np.arange(top_left_real, bottom_right_real, step)
    imag = np.arange(top_left_imag, bottom_right_imag, -step)
    real_coordinate = real.reshape(1, -1)
    imag_coordinate = imag.reshape(-1, 1)
    grid = real_coordinate + imag_coordinate * 1j
    return grid

"""PART 3"""
def get_escape_time_color_arr(c_arr: np.ndarray,max_iterations: int) -> np.ndarray:
    """

    Returns an array of the same shape with color values in [0,1] according to the escape time of each c-value.

    Parameters
    ----------
    c_arr: np.ndarray
        The top left corner of the coordinate of this grid.
    max_iterations: int
        The bottom right corner of the coordinate of this grid.

    Returns
    -------
    np.ndarray, The coordinates of the point.

    """
    escape_time = np.zeros(c_arr.shape, dtype=int)
    for i in range(c_arr.shape[0]):
        for j in range(c_arr.shape[1]):
            c = c_arr[i, j]
            x = 0 + 0j
            t = 0
            while abs(x) <= 2 and t < max_iterations:
                x = x * x + c
                t += 1
            if t == max_iterations:
                escape_time[i, j] = max_iterations + 1
            else:
                escape_time[i, j] = t
    result = (max_iterations - escape_time + 1) / (max_iterations + 1)
    return result
