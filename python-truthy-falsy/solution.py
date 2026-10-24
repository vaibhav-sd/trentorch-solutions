def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    if type(value) == int:
        return value != 0
    elif type(value) == bool:
        return value
    elif type(value) in [set, dict, list, tuple, str]:
        return len(value) != 0
    else:
        return False

def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for i in values:
        if bool(i) == True:
            return i
    return None
    pass
