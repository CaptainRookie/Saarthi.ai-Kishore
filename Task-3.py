# Input dict_list=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415},
#                 {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
# Output=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415},
#        {'name': 'inform', 'confidence': 0.9842240810394287}]


dict_list = [{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {
    'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]

seen = set()

dict = []
for d in dict_list:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        dict.append(d)

print(dict)
