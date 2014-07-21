from base_measure import *

class AUC(BaseMeasure):
  @staticmethod
  def auc(obj_truth, obj_pred):
    """Area under the curve
       truth: list of int 0/1
       pred: list of float [0, 1]
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = AUC.auc_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def auc_a_line(y_truth, y_pred):
    result = []
    n_truth, n_false = 0, 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1

      if y1_i < 0.5: n_false += 1
      else:          n_truth += 1
      result.append( (y2_i, y1_i) )
    sort_list = sorted(result, key = lambda d:d[0], reverse=True)
    idx, tot = n_false, 0
    for k, v in sort_list:
      if v > 0.5: tot += idx
      else:       idx -= 1
    return float(tot) / n_truth / n_false 


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print '<usage> p_truth p_pred'
    exit(-1)

  e, E = AUC.auc(sys.argv[1], sys.argv[2])
  print 'AUC:', e 

