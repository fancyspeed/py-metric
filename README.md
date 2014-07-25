## pymetric

The Python module to common measurement methods.

## Installation

    $ sudo python setup.py install

or alternatively building module

    $ python setup.py build

## Getting Started

    >>> from pymetric import AllMetrics
    >>> A = [1, 0, 1]
    >>> B = [1, 0, 0]
    >>> AllMetrics.measure(A, B, 'rmse')
    0.57735026918962573
    >>> AllMetrics.measure(A, B, 'ap')
    0.83333333333333326

## API Reference

The all_in_one interface of pymetric is AllMetrics.measure(y_truth, y_pred, method).

* y_truth : a list of int/float, or filename that contains a value each line.
* y_pred : a list of float, or filename that contains a value each line.
* method : several options as follows:

### Group 1

Group 1 is for regression task. Inputs of y_truth should be a list of floats.

*  abs_error : AbsError.abs_error
*  rmse : RMSE.rmse
*  r2 : R2.r2
*  ndcg : NDCG.ndcg
*  cos : Cosine.cos

### Group 2

Group 2 is for classification task. Inputs of y_truth should be a list of 0-1 values.

*  precision : PR.precision
*  recall : PR.recall
*  f1_score : PR.f1_score
*  ap : MAP.ap
*  auc : AUC.auc
*  ndcg : NDCG.ndcg

## TODO list: 

* [AMS] (https://www.kaggle.com/c/higgs-boson/details/evaluation)

##Author

pymetric is developed and maintained by Zuotao Liu (zuotaoliu@126.com).


