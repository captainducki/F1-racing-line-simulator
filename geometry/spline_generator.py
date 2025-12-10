import numpy as np
import scipy.interpolate as sci

def generate_spline(x, y):

  distance_x = np.diff(x)
  distance_y = np.diff(y)
  distance = np.sqrt(distance_x**2 + distance_y**2)

  t = np.concatenate(([0], np.cumsum(distance)))
  t /= t[-1]

  spline_x = sci.CubicSpline(t, x)
  spline_y = sci.CubicSpline(t, y)

  return spline_x, spline_y, t

def evaluate_spline(spline_x, spline_y, num_points=1000):
  t_values = np.linspace(0, 1, num_points)

  x_values = spline_x(t_values)
  y_values = spline_y(t_values)

  return x_values, y_values, t_values


