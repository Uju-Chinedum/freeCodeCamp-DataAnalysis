import numpy as np

def calculate(l):
  
  if len(l) < 9:
    raise ValueError("List must contain nine numbers.")
  else:
    list_1 = l[0:3]
    list_2 = l[3:6]
    list_3 = l[6:]
    l = [list_1, list_2, list_3]
    arr = np.array(l)

    avr = [list(arr.mean(axis = 0)), list(arr.mean(axis = 1)), arr.mean()]
    var = [list(arr.var(axis = 0)), list(arr.var(axis = 1)), arr.var()]
    std = [list(arr.std(axis = 0)), list(arr.std(axis = 1)), arr.std()]
    maximum = [list(arr.max(axis = 0)), list(arr.max(axis = 1)), arr.max()]
    minimum = [list(arr.min(axis = 0)), list(arr.min(axis = 1)), arr.min()]
    total = [list(arr.sum(axis = 0)), list(arr.sum(axis = 1)), arr.sum()]

    calculations = {
      "mean": avr,
      "variance": var,
      "standard deviation": std,
      "max": maximum,
      "min": minimum,
      "sum": total
    }
    return calculations


print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))