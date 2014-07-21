from base_measure import *

class Cosine(BaseMeasure):
  @staticmethod
  def cos(obj_truth, obj_pred):
    """sum(Y_i*y'_i) / sqrt( sum(y_i*y_i) ) / sqrt( sum(y'_i*y'_i) )
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = Cosine.cos_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def cos_a_line(y_truth, y_pred):
    #m_truth = BaseMeasure.average(y_truth) 
    #m_pred = BaseMeasure.average(y_pred)

    s0, s1, s2 = 0, 0, 0
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
  
      a = y1_i #- m_truth 
      b = y2_i #- m_pred 
      s0 += a * b
      s1 += a * a
      s2 += b * b
    if s1 <= 0 or s2 <= 0:
      return 0
    return s0 / math.sqrt(s1) / math.sqrt(s2)

  
if __name__ == '__main__':
  import sys
  if len(sys.argv) < 3:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = Cosine.cos(sys.argv[1], sys.argv[2])
  print 'r2:', e 

