#!/usr/bin/env python
#coding: utf-8
#author: liuzuotao@snda.com
#modified: 2013-8-27

import math
from base_exceptions import *

class BaseMeasure(object):
  @staticmethod
  def parse_args(obj_truth, obj_pred):
    Y_truth = BaseMeasure.parse_arg(obj_truth)
    Y_pred = BaseMeasure.parse_arg(obj_pred)
    if len(Y_truth) != len(Y_pred):
      raise IllegalInput('lens of Y_truth and Y_pred are not equal!')
    i = 0
    for y_truth in Y_truth:
      y_pred, i = Y_pred[i], i+1
      if len(y_truth) != len(y_pred):
        raise IllegalInput('line %d: lens of y_truth and y_pred are not equal!' % i)
      if len(y_truth) == 0:
        raise IllegalInput('line %d: lens of y_truth and y_pred are 0!' % i)
    return Y_truth, Y_pred


  @staticmethod
  def parse_arg(obj_in):
    if type(obj_in) == type([[]]):  #[list1, list2...] 
      return obj_in
    elif type(obj_in) == type(''):  #filename, each line is a list 
      matrix_in = []
      try:
        for line in open(obj_in):
          slist_in = line.strip().replace(', ', ',').replace(',', ' ').split(' ')
          list_in = [float(score) for score in slist_in]
          matrix_in.append( list_in )
      except Exception as e:
        raise IllegalInput(repr(e)) 
      return matrix_in
    else:
      raise IllegalInput('input type error') 
        

  @staticmethod
  def int_cmp(y1, y2):
    return int(y1 + 0.1) == int(y2 + 0.1)


  @staticmethod
  def average(list_in):
    return sum(list_in) / float(len(list_in))

