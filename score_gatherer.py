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
    if (level > 10):
        # different scoring

    else:
        score = (level - current_level) * 10
    return score


if __name__ == '__main__':
    scores_tuples = generate_scores(sys.argv[1])
    hm = dict()
    score_map = dict()

    penalty = 1
    for tuple in scores_tuples:
        level, people = tuple
        level = int(level) - 1
        ppl_list = str(people).split(" ")
        for ppl in ppl_list:
            current_level = int(hm.get(ppl, 0))
            if (current_level < level):
                print("Changed levels")
                hm[ppl] = level
                new_score = calc_score(level, current_level) * penalty
                score_map[ppl] = int(score_map.get(ppl, 0)) + new_score
    # print(hm)
    print(score_map)

