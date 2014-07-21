#!/usr/bin/env python
#coding: utf-8
#author: liuzuotao@snda.com
#modified: 2013-8-27

"""Python module for several evaluation methods.

.. pymetric implements common evaluation methods,
.. such as RMSE, MAP, NDCG, AUC.

.. input::
.. y_truth: [list1, list2 ...], each list contains multiple float scores. 
             For classification task, >0.5 means positive.
.. y_pred: [list1', list2' ...]

.. return:: 
.. e: a score corresponding to the method.
.. E: a list contains all scores of each line.
"""

from pymetric.all_in_one import AllMetrics 
from pymetric.base_exceptions import PyMetricException, LengthNotEqual, IllegalInput 

from pymetric.abs_error import AbsError
from pymetric.rmse import RMSE
from pymetric.r2 import R2
from pymetric.ndcg import NDCG
from pymetric.cosine import Cosine

from pymetric.pr import PR
from pymetric.map import MAP
from pymetric.auc import AUC

