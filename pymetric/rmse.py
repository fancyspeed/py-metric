from base_measure import *

class RMSE(BaseMeasure):
  @staticmethod
  def rmse(obj_truth, obj_pred):
    """sqrt( 1/n * sum(|y_i - y'_i|^2) )
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = RMSE.rmse_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def rmse_a_line(y_truth, y_pred):
    tot = 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
      err = math.pow(y1_i - y2_i, 2) 
      tot += err
    return math.sqrt(tot / i)


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = RMSE.rmse(sys.argv[1], sys.argv[2])
  print 'rmse:', e

