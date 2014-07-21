from base_measure import *

class PR(BaseMeasure):
  @staticmethod
  def precision(obj_truth, obj_pred):
    """|Right| / |Pred|
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = PR.precision_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def precision_a_line(y_truth, y_pred):
    n_right, n_pred = 0, 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
      if y1_i > 0.5 and y2_i > 0.5:
        n_right += 1
      if y2_i > 0.5:
        n_pred += 1
    if n_right == 0:
      return 0
    return n_right / float(n_pred)


  @staticmethod
  def recall(obj_truth, obj_pred):
    """|Right| / |Truth|
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = PR.recall_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def recall_a_line(y_truth, y_pred):
    n_right, n_truth = 0, 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
      if y1_i > 0.5 and y2_i > 0.5:
        n_right += 1
      if y1_i > 0.5:
        n_truth += 1
    if n_right == 0:
      return 0
    return n_right / float(n_truth)


  @staticmethod
  def f1_score(obj_truth, obj_pred):
    """2 * P * R / (P + R) 
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = PR.f1_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def f1_a_line(y_truth, y_pred):
    p = PR.precision_a_line(y_truth, y_pred)
    r = PR.recall_a_line(y_truth, y_pred)

    if p <= 0 or r <= 0:
      return 0
    return 2 * p * r / (p + r)


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = PR.precision(sys.argv[1], sys.argv[2])
  print 'precision:', e
  e, E = PR.recall(sys.argv[1], sys.argv[2])
  print 'recall:', e
  e, E = PR.f1_score(sys.argv[1], sys.argv[2])
  print 'f1_score:', e

