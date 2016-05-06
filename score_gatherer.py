__author__ = 'saipc'
import re

def generate_scores(file):
    with open(file, 'r') as f:
        score_string = f.read()
        # read the file and extract the people
        # in each level, regex matches:
        # ----------[ Level xx ]------------\n
        # p1 p2 p3 p4 p5 p6\n
        r = re.compile("\n-+\[ Level (\d+).*\]-+\n(.*)\n")
        m = r.findall(score_string)
        return m


def calc_score(level, current_level):
    score = 0
    if (level > 10 and current_level > 10):
        # e.g., if the person moved from 11 to 13
        score = (level - current_level) * 1
    elif (level > 10):
        # different scoring
        # e.g., if the person moved from 8 to 12
        score = (10 - current_level) * 10 + (level - 10) * 1
    else:
        # e.g., if the person moved from 4 to 7
        score = (level - current_level) * 10
    return score


if __name__ == '__main__':
    # give the score files here
    days = ['mon4_score', 'tue5_score', 'wed6_score', 'thu7_score', 'fri8_score']
    # hold the score maps
    score_map = dict()
    # holds the level maps
    hm = dict()
    for i in xrange(5):
        scores_tuples = generate_scores(days[i])
        # calc the penalty for each day
        penalty = 1.00 - (0.2 * i)
        print("Penalty is %s for %s")%(penalty, days[i])
        for tuple in scores_tuples:
            # get the level and the ppl in that level
            level, people = tuple
            level = int(level) - 1
            # get the list of ppl in that level
            ppl_list = str(people).split(" ")
            for ppl in ppl_list:
                current_level = int(hm.get(ppl, 0))
                # see if person has moved, else do nothing
                if (current_level < level):
                    # Changed levels
                    # update level map to indicate new level
                    hm[ppl] = level
                    # calc the score to be updated to, depending
                    # on the level change
                    new_score = calc_score(level, current_level) * penalty
                    # update score in score map, needs a float here
                    score_map[ppl] = float(score_map.get(ppl, 0)) + float(new_score)
    # print stuff out nicely
    for key in score_map.keys():
        print("%s : %s") % (key, score_map.get(key))
