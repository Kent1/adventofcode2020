import re 

REQUIRED_FIELDS = {
    'byr': r'^(19[2-9]\d|200[0-2])$',
    'iyr': r'^(201\d|2020)$',
    'eyr': r'^(202\d|2030)$',
    'hgt': r'^(1[5-8]\dcm|19[0-3]cm|19[0-3]cm|19[0-3]cm|59in|6\din|7[0-6]in)$',
    'hcl': r'^#[0-9a-fA-F]{6}$',
    'ecl': r'^amb|blu|brn|gry|grn|hzl|oth$',
    'pid': r'^\d{9}$',
}
OPTIONAL_FIELDS = [
    'cid',
]

def valid(passport):
    for field in REQUIRED_FIELDS:
        if field not in passport or not re.match(REQUIRED_FIELDS[field], passport[field]):
            return False
    return True

with open("input.txt", 'r') as f:
    l = map(str.split, f.read().split("\n\n"))
    passports = [dict(keyvalue.split(":") for keyvalue in passport) for passport in l]
    print(sum([valid(passport) for passport in passports]))
