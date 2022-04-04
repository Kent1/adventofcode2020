import math

def validate_rules(rules, number):
    for rule in rules:
        if validate_rule(rule, number):
            return True
    return False

def validate_rule(rule, number):
    for or_component in rule:
        if or_component[0] <= number <= or_component[1]:
            return True
    return False

with open('input.txt', 'r') as f:
    rules, my_ticket, other_tickets = f.read().split('\n\n')

rules = { (y := rule.split(': '))[0] : [list(map(int, component.split('-'))) for component in y[1].split(' or ')] for rule in rules.split('\n') }
my_ticket = list(map(int, my_ticket.split('\n')[1].split(',')))
other_tickets = [list(map(int, ticket.split(','))) for ticket in other_tickets.split('\n')[1:]]

invalid_tickets = []

rate = 0
for ticket in other_tickets:
    for number in ticket:
        if not validate_rules(rules.values(), number):
            rate += number
            invalid_tickets += [ticket]
print(rate)

# Part 2
def validate_tickets(rules, tickets):
    for ticket in tickets:
        if not all([validate_rule(rule, number) for rule, number in zip(rules, ticket)]):
            return False
    return True

valid_tickets = [ticket for ticket in other_tickets if ticket not in invalid_tickets]
orders = {rule_name : [True] * len(rules) for rule_name in rules.keys()}

for ticket in valid_tickets:
    for i, number in enumerate(ticket):
        for rule_name, rule in rules.items():
            if not validate_rule(rule, number):
                orders[rule_name][i] = False

order = [''] * len(orders)
orders = {name : possibility for name, possibility in sorted(orders.items(), key=lambda item: sum(item[1]))}
for name, possibilities in orders.items():
    for id, possibility in enumerate(possibilities):
        if possibility:
            for possibilities in orders.values():
                possibilities[id] = False
            order[id] = name

assert len(order) == len(rules)
# print(order)

print(math.prod([my_ticket[i] for i, name in enumerate(order) if name.startswith("departure")]))