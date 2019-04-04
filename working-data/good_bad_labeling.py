import sys

pred_fn = sys.argv[1]
gold_fn = sys.argv[2]

with open(pred_fn, 'r', encoding="utf-8") as f_pred, \
     open(gold_fn, 'r', encoding="utf-8") as f_gold:
    
    predicted_lines_ordered = [line.rstrip() for line in f_pred]
    predicted_lines = set(predicted_lines_ordered)
    gold_lines = set([line.rstrip() for line in f_gold])

    correct_lines = predicted_lines.intersection(gold_lines)
    wrong_lines = predicted_lines.difference(correct_lines)

for line in predicted_lines_ordered:
    prefix = "correct" if line in correct_lines else "wrong"
    
    print(prefix+'\t'+line) 