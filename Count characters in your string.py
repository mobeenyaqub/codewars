def count(s):
    return {i: s.count(i) for i in sorted(set(s))}