import os

__author__ = 'saipc'

from score_gatherer import generate_scores
from score_gatherer import calc_score
from score_gatherer import days

# this maps like so:
# person -> [day1, day2, ...]
people_matrix = dict()

def get_files(folder):
    files = os.listdir(folder)
    # remove that stupid .ds_store
    files = files[1:]
    # this complicated looking lambda is doing something simple:
    # for each file, append the full path, then use that to get
    # the time of creation of that, then sort using that time.
    files.sort(key=lambda x: os.path.getmtime(os.path.join(os.curdir, folder, x)))
    return files

def generate_level_sorting(files):
    for f in files:
        scores_tuples = generate_scores(f)
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
    with open('csv-out-every5', 'w') as of:
        for ppl, level in people_matrix.items():
            # easy csv format
            print (ppl) + ',' + ','.join(str(l) for l in level)
            of.write((ppl) + ',' + ','.join(str(l) for l in level) + '\n')

if __name__ == '__main__':
    files = get_files('scores')
    os.chdir('scores')
    generate_level_sorting(files)