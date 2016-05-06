from collections import OrderedDict

__author__ = 'saipc'
import sys
import re

def generate_scores(file):
    with open(file, 'r') as f:
        score_string = f.read()
        # print("%r" % score_string)
        r = re.compile("\n-+\[ Level (\d+).*\]-+\n(.*)\n")
        m = r.findall(score_string)
        return m


def calc_score(level, current_level):
    score = 0
    if (level > 10 and current_level > 10):
        score = (level - current_level) * 1
    elif (level > 10):
        # different scoring
        score = (10 - current_level) * 10 + (level - 10) * 1
    else:
        score = (level - current_level) * 10
    return score


if __name__ == '__main__':
    days = ['mon4_score', 'tue5_score', 'wed6_score', 'thu7_score', 'fri8_score']
    score_map = dict()
    hm = OrderedDict()
    for i in xrange(5):
        scores_tuples = generate_scores(days[i])
        penalty = 1.00 - (0.2 * i)
        print("Penalty is %s for %s")%(penalty, days[i])
        for tuple in scores_tuples:
            level, people = tuple
            level = int(level) - 1
            ppl_list = str(people).split(" ")
            for ppl in ppl_list:
                current_level = int(hm.get(ppl, 0))
                if (current_level < level):
                    # print("Changed levels")
                    hm[ppl] = level
                    new_score = calc_score(level, current_level) * penalty
                    score_map[ppl] = float(score_map.get(ppl, 0)) + float(new_score)
        # print(hm)
    for key in score_map.keys():
        print("%s : %s") % (key, score_map.get(key))
    # print(score_map.keys())

