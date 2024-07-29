def merge_dictionaries(d1, d2):
  d1.update(d2)
  return d1


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 4, 'd': 5, 'e': 6}

md = merge_dictionaries(d1, d2)
print(md)
