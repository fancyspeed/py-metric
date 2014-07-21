from base_measure import *

from abs_error import AbsError
from rmse import RMSE
from r2 import R2
from ndcg import NDCG
from cosine import Cosine

from pr import PR
from map import MAP
from auc import AUC

class AllMetrics(BaseMeasure):
  """
    docs are in corresponding classes: AbsError, RMSE, R2, NDCG, Cosine, PR, MAP, AUC...
  """

  @staticmethod
  def measure(y_truth, y_pred, method='abs_error'):
    """this function integrates several metric methods
       abs_error, rmse, r2, ndcg, cos
       precision, recall, f1_score, auc, map
    """
    if method == 'abs_error':
      return AbsError.abs_error(y_truth, y_pred)
    elif method == 'rmse':
      return RMSE.rmse(y_truth, y_pred)
    elif method == 'r2':
      return R2.r2(y_truth, y_pred)
    elif method == 'ndcg':
      return NDCG.ndcg(y_truth, y_pred)
    elif method == 'cos':
      return Cosine.cos(y_truth, y_pred)
    elif method == 'precision':
      return PR.precision(y_truth, y_pred)
    elif method == 'recall':
      return PR.recall(y_truth, y_pred)
    elif method == 'f1_score':
      return PR.f1_score(y_truth, y_pred)
    elif method == 'auc':
      return AUC.auc(y_truth, y_pred)
    elif method == 'map':
      return MAP.map(y_truth, y_pred)

    raise IllegalInput('no such method!')
     

if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  print repr(AllMetrics)

  A = [[1,2]]
  B = [[2,3]]

  e, E = AllMetrics.measure(A, B, 'rmse')
  print 'rmse:', e, E

