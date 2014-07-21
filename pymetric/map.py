from base_measure import *

class MAP(BaseMeasure):
  @staticmethod
  def map(obj_truth, obj_pred):
    """mean average precision: 1/|Right| * sum( P@k )
       truth: list of list of int 0/1
       pred: list of list of float [0, 1], trated as positive if >0.5
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = MAP.ap_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def ap_a_line(y_truth, y_pred):
    result = []
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1    
      result.append( (y2_i, y1_i) )
    sort_list = sorted(result, key = lambda d:d[0], reverse=True)
    tot, n_right = 0, 0
    i = 0
    for k, v in sort_list:
      i += 1
      if v > 0.5: 
        n_right += 1.0
        tot += n_right / i 
    if n_right == 0: return 0
    return tot / n_right


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print '<usage> p_truth p_pred'
    exit(-1)

  e, E = MAP.map(sys.argv[1], sys.argv[2])
  print 'map:', e 

