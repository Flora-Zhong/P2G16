import numpy as np

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