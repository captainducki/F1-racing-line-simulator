import numpy as np
import os

def load_track(name):
  path = f"data/tracks/{name}.csv"

  if not os.path.exists(path):
    raise FileNotFoundError(f"Track file '{path}' does not exist.")
  
  data = np.loadtxt(path, delimiter=",", skiprows=1)

  if data.ndim != 2 or data.shape[1] != 2:
    raise ValueError(f"Track file '{path}' must have exactly two columns for x and y coordinates.")
  
  x = data[:, 0]
  y = data[:, 1]

  return x, y