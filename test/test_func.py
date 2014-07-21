import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pymetric
from pymetric import AllMetrics 

def test_module():
  print pymetric.__doc__

def test_func():
  A = [[1, 2, 2, 5]]
  B = [[0.7, -0.3, 0, 4]]
  for method in ['abs_error', 'rmse', 'r2', 'ndcg', 'cos']:
    print method, AllMetrics.measure(A, B, method)

  A = [[1, 2, 2, 5]]
  B = [[0.7, 1.5, 1.8, 2.7]]
  for method in ['abs_error', 'rmse', 'r2', 'ndcg', 'cos']:
    print method, AllMetrics.measure(A, B, method)

  A = [[1, 2, 2, 5], [0.5, 0.1, 0.2, -0.3]]
  B = [[0.7, 1.5, 1.8, 2.7], [0.1, 0.3, 0.7, 0.11]]
  for method in ['map', 'ndcg']:
    print method, AllMetrics.measure(A, B, method)

if __name__ == '__main__':
  test_module()
  test_func()

