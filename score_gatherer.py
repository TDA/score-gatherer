__author__ = 'saipc'
import sys
import re

def generate_scores(file):
    with open(file, 'r') as f:
        score_string = f.read()
        # print("%r" % score_string)
        r = re.compile("\n-+(.*)-+\n")
        levels = r.split(score_string)
        print(levels)


if __name__ == '__main__':
    generate_scores(sys.argv[1])