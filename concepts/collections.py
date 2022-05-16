from collections import Counter
from collections import namedtuple

a = "aaaabbbbbbbccccc"
# counters
my_counter = Counter(a).keys()
print(my_counter)

# named tuple

Point = namedtuple('Point', 'x,y')

pt = Point(1, -4)
print(pt)