import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

#import pymetric import PyMetricException, LengthNotEqual, IllegalInput
from pymetric import AllMetrics 

def example_1():
  """for regression task
  """
  A = [[0.1, 0.2, 0.2, 0.6], [0.5, 0.1, 0.2, 0.3]]
  B = [[0.7, 0.5, 0.8, 0.7], [0.1, 0.3, 0.7, 0.1]]
  print 'Y_truth', A
  print 'Y_pred ', B
  for method in ['abs_error', 'rmse', 'r2', 'ndcg', 'cos']:
    try:
      print method, AllMetrics.measure(A, B, method)
    except Exception as e:
      print 'Exception: %s' % repr(e)

def example_2():
  """for classification task
  """
  A = [[1, 0, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1]]
  B = [[0, 1, 1, 0, 1, 0], [0.2, 0.3, 0.7, 0.1, 0.3, 0.8]]
  print 'Y_truth', A
  print 'Y_pred ', B
  for method in ['precision', 'recall', 'f1_score', 'auc', 'map']:
    try:
      print method, AllMetrics.measure(A, B, method)
    except Exception as e:
      print 'Exception: %s' % repr(e)


if __name__ == '__main__':
  example_1()
  example_2()

