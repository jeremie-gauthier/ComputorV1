from typing import List
from itertools import takewhile


def merge_dict_coefs(d1: dict, d2: dict) -> dict:
    new_dict = {0: 0, **d1}
    for key, value in d2.items():
        if key in new_dict:
            new_dict[key] -= value
        else:
            new_dict[key] = -value
    return new_dict


# To keep the expr as reduced as possible,
# we remove all consecutive biggest coefs that are = 0
def remove_nullish_coefs(dict_coefs: dict) -> dict:
    keys = sorted(dict_coefs.keys(), reverse=True)
    new_dict = {**dict_coefs}
    null_keys = takewhile(lambda key: new_dict[key] == 0 and key != 0, keys)
    for key in null_keys:
        new_dict.pop(key, None)
    return new_dict


def expression(coefs: map) -> List[float]:
    dict_coefs = merge_dict_coefs(*coefs)
    reduced = remove_nullish_coefs(dict_coefs)
    return reduced
