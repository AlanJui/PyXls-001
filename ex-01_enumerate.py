colors = ['red', 'green', 'blue', 'yellow']

for i, color in enumerate(colors):
    print(i, '-->', color)

#============================================
import itertools

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

for name, color in itertools.zip_longest(names, colors):
    print(name, '-->', color)