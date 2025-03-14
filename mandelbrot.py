import numpy as np

"""PART 1"""
def get_escape_time(c: complex, max_iterations: int) -> int | None:
    """

    Finding the max amount of times c has to go through the mandelbrot set before it escapes.

    Parameters
    ----------
    c : complex
        The complex number to calculate the escape time.
    max_iterations: int
        The maximum number of iterations.

    Returns
    -------
    np.ndarray, The coordinates of the point.

    """
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

    Returns an array of the same shape with color values in [0, 1] according to the escape time of each c-value.

    Parameters
    ----------
    c_arr: np.ndarray
        An array with c-values.
    max_iterations: int
        The maximum number of iterations.

    Returns
    -------
    np.ndarray, An array of the same shape with color values in [0, 1] according to the escape time of each c-value.

    """
    escape_time = np.zeros(c_arr.shape, dtype = int)
    current_value = np.zeros(c_arr.shape, dtype = complex)
    num_iterations = np.zeros(c_arr.shape, dtype = int)
    for i in range(c_arr.shape[0]):
        for j in range(c_arr.shape[1]):
            c = c_arr[i, j]
            current_value[i,j] = 0 + 0j
            num_iterations[i,j] = 0
            while np.abs(current_value[i,j]) <= 2 and num_iterations[i,j] < max_iterations:
                current_value[i,j] = current_value[i,j] * current_value[i,j] + c
                num_iterations[i,j] += 1
            if num_iterations[i,j] == max_iterations:
                escape_time[i, j] = max_iterations + 1
            else:
                escape_time[i, j] = num_iterations[i,j]
    result = (max_iterations - escape_time + 1) / (max_iterations + 1)
    return result

"""PART 4"""
def get_julia_color_arr(grid: np.ndarray, c: complex, max_iterations: int) -> np.ndarray:
    """

    Compute escape times for the Julia set of P_c(z) = z^2 + c.

    Parameters:
        grid: np.ndarray
            A 2D array of complex numbers representing the grid.
        c: complex
            The parameter c for the Julia set.
        max_iterations: int
            The maximum number of iterations.

    Returns:
        np.ndarray: A 2D array of escape times.

    """
    z = grid.copy()
    escape_times = np.zeros(grid.shape, dtype=int)  # Default to max iterations
    escape_radius = np.maximum(abs(c), 2)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            current_value = z[i, j]
            num_iterations = 0
            while num_iterations < max_iterations and np.abs(current_value) < escape_radius:
                current_value = current_value ** 2 + c
                num_iterations += 1
                if num_iterations < max_iterations:
                    escape_times[i, j] = num_iterations
                else:
                    escape_times[i, j] = max_iterations + 1
    result = (max_iterations - escape_times + 1) / (max_iterations + 1)
    return result