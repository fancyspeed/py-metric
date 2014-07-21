cd $(dirname $0)

regress_truth=./data/regress_truth.txt
regress_pred=./data/regress_pred.txt

python ./pymetric/abs_error.py ${regress_truth} ${regress_pred}
python ./pymetric/rmse.py ${regress_truth} ${regress_pred}
python ./pymetric/r2.py ${regress_truth} ${regress_pred}
python ./pymetric/ndcg.py ${regress_truth} ${regress_pred}
python ./pymetric/cosine.py ${regress_truth} ${regress_pred}

classify_truth=./data/classify_truth.txt
classify_pred=./data/classify_pred.txt

python ./pymetric/pr.py ${classify_truth} ${classify_pred}
python ./pymetric/auc.py ${classify_truth} ${classify_pred}
python ./pymetric/map.py ${classify_truth} ${classify_pred}

