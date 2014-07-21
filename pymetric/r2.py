from base_measure import *

class R2(BaseMeasure):
  @staticmethod
  def r2(obj_truth, obj_pred):
    """sum(Y_i*y'_i)^2 / sum(y_i*y_i) / sum(y'_i*y'_i)
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = R2.r2_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def r2_a_line(y_truth, y_pred):
    m_truth = BaseMeasure.average(y_truth) 
    m_pred = BaseMeasure.average(y_pred)

    s0, s1, s2 = 0, 0, 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
  
      a = y1_i - m_truth 
      b = y2_i - m_pred 
      s0 += a * b
      s1 += a * a
      s2 += b * b
    if s1 <= 0 or s2 <= 0:
      return 0
    return s0 * s0 / s1 / s2

  
if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = R2.r2(sys.argv[1], sys.argv[2])
  print 'r2:', e 

