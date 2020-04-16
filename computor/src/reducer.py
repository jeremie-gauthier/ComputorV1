from typing import List
from itertools import takewhile
from .verbose import mid_steps_reducer


def merge_dict_coefs(dicts: List[dict], verbose: bool) -> dict:
    new_dict = {**dicts[0]}
    mid_steps = []
    if verbose:
        right_dict = {**dicts[1]}
        mid_steps.append(mid_steps_reducer(new_dict, right_dict))
    for key, value in dicts[1].items():
        if key in new_dict:
            new_dict[key] -= value
        else:
            new_dict[key] = -value
        if verbose:
            right_dict.pop(key, None)
            mid_steps.append(mid_steps_reducer(new_dict, right_dict))
    return (new_dict, mid_steps)


# To keep the expr as reduced as possible,
# we remove all consecutive biggest coefs that are = 0
def remove_nullish_coefs(dict_coefs: dict) -> dict:
    keys = sorted(dict_coefs.keys(), reverse=True)
    new_dict = {**dict_coefs}
    null_keys = takewhile(lambda key: new_dict[key] == 0 and key != 0, keys)
    for key in null_keys:
        new_dict.pop(key, None)
    return new_dict


def expression(coefs: map, verbose: bool) -> List[float]:
    dict_coefs, mid_steps = merge_dict_coefs(tuple(coefs), verbose)
    reduced = remove_nullish_coefs(dict_coefs)
    return (reduced, mid_steps)
