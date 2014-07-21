from base_measure import *

class AbsError(BaseMeasure):
  @staticmethod
  def abs_error(obj_truth, obj_pred):
    """1/n * sum(|y_i - y'_i|)
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = AbsError.abs_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def abs_a_line(y_truth, y_pred):
    tot = 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
      err = math.fabs(y1_i - y2_i) 
      tot += err
    return tot / i 


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = AbsError.abs_error(sys.argv[1], sys.argv[2])
  print 'abs_error:', e

