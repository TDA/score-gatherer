from collections import OrderedDict

__author__ = 'saipc'
from ass3_score import d

def id_alias_mapper(filename):
    id_alias_map = dict()
    with open(filename, 'r') as f:
        for line in f:
            id, alias = line.rstrip("\n").split(" ")
            id_alias_map[id] = alias
    return id_alias_map


if __name__ == '__main__':
    id_alias_map = id_alias_mapper("id_alias_score")
    # print(id_alias_map)
    id_list_sorted = sorted(id_alias_map.keys())
    # print(id_list_sorted)
    ordered_score = OrderedDict()
    for id in id_list_sorted:
        alias = id_alias_map.get(id)
        score = d.get(alias)
        print(score)
        ordered_score[id] = score





