from base_measure import * 

class NDCG(BaseMeasure):
  @staticmethod
  def ndcg(obj_truth, obj_pred):
    """normalized discounted cumulative gain
       dcg = sum( (2^r - 1) / log(2, i+1) )
       ndcg = dcg / ideal_dcg
       truth: list of list of int 0/1
       pred: list of list of float [0, 1], trated as positive if >0.5
    """
    Y_truth, Y_pred = BaseMeasure.parse_args(obj_truth, obj_pred)
    
    E = []
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      e = NDCG.ndcg_a_line(y_truth, y_pred)
      E.append( e )
    return sum(E)/len(E), E


  @staticmethod
  def ndcg_a_line(y_truth, y_pred):
    result = []
    i = 0
    for y1_i in y_truth:
      y2_i, i = y_pred[i], i+1
      result.append( (y2_i, y1_i) )
    sort_list = sorted(result, key = lambda d:d[0], reverse=True)
    dcg, i = 0, 0
    for y2_i, y1_i in sort_list:
      i += 1
      dcg += (math.pow(2, y1_i) - 1) / math.log(i+1, 2) 
    sort_list = sorted(result, key = lambda d:d[1], reverse=True)
    idcg, i = 0, 0
    for y2_i, y1_i in sort_list:
      i += 1
      idcg += (math.pow(2, y1_i) - 1) / math.log(i+1, 2)
    #if idcg <= 0: return 0
    return dcg / idcg


if __name__ == '__main__':
  import sys
  if len(sys.argv) < 2:
    print 'usage: p_truth p_pred'
    exit(-1)

  e, E = NDCG.ndcg(sys.argv[1], sys.argv[2])
  print 'ndcg:', e

