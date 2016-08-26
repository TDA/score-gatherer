__author__ = 'saipc'

from score_gatherer import generate_scores
from score_gatherer import calc_score
from score_gatherer import days

# this maps like so:
# person -> [day1, day2, ...]
people_matrix = dict()

if __name__ == '__main__':
    for i in xrange(5):
        scores_tuples = generate_scores(days[i])
        for tuple in scores_tuples:
            # get the level and the ppl in that level
            new_level, people = tuple
            new_level = int(new_level) - 1
            # get the list of ppl in that level
            ppl_list = str(people).strip().split(" ")
            for ppl in ppl_list:
                # create a list if not present already
                current_list = people_matrix.get(ppl, [])
                current_list.append(new_level)
                people_matrix[ppl] = current_list
    for ppl, level in people_matrix.items():
        # easy csv format
        print (ppl) + ',' + ','.join(str(l) for l in level)
