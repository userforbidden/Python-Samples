from itertools import combinations, product

substitutions={'s':['$'], 'a': ['4'], 'l': ['1'], 'e': ['3'], 't': ['7'], 'i': ['1'], 'o': ['0'], 'b': ['8'], 'g': ['9']}
word = 'accompanying'
# print(*substitutions.get('a',[]))
# print([word[0], *substitutions.get(word[0], [])])
# for key in substitutions.keys():
#     if key not in substitutions[key]:
#         substitutions[key].append(key)
wordPossibilities = []
def get_subs(d, c = []):
  if not d:
     yield ''.join(c)
  else:
     for i in [d[0], *substitutions.get(d[0], [])]:
        yield from get_subs(d[1:], c+[i])
        
# for substitute in [zip(substitutions.keys(),ch) for ch in product(*substitutions.values())]:
#   temp=word
#   for replacement in substitute:
#     temp=temp.replace(*replacement)
#   wordPossibilities.append(temp)
print(list(get_subs(word)))

