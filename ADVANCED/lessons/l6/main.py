import random
from sys import argv

print(random.uniform(int(argv[1]), int(argv[2])))
print(random.randrange(int(argv[1]), int(argv[2]), int(argv[1])))
print(random.sample(range(int(argv[1]), int(argv[2]), int(argv[1])), 10))

"""
128.02359860636767
470
[360, 270, 400, 750, 250, 950, 740, 390, 800, 980]
"""