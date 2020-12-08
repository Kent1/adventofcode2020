import re

pattern = re.compile(r'^(\w+ \w+) bags contain (?P<nobags>no other bags)?((?:\d+ \w+ \w+ bags?(?:, )?)*)\.$')
subpattern = re.compile(r'(\d+) (\w+ \w+) bags?(?:, )?')

def build_dic(l):
    d = {}
    for sentence in l:
        m = pattern.match(sentence)
        bag = m[1]
        if m.group("nobags"):
            d[bag] = {}
        else:
            m = re.findall(subpattern, m[3])
            d[bag] = {x[1]: int(x[0]) for x in m}
    return d
    
def find(d, bag):
    return set(color for color in d if can_contain(d, color, bag))

def can_contain(d, color, bag_to_find):
    if bag_to_find in d[color]:
        return True
    return any([can_contain(d, x, bag_to_find) for x in d[color]])

def get_number_of_bags(bags, color):
    return sum([count * (1 + get_number_of_bags(bags, c)) for c, count in bags[color].items()])

with open("input.txt", 'r') as f:
    l = f.readlines()
    bags = build_dic(l)
    print(len(find(bags, "shiny gold")))
    print(get_number_of_bags(bags, "shiny gold"))
