from typing import List, NoReturn,Dict
import re
from collections import Counter



def main() -> NoReturn:
    info: List[Dict[str, str]] = read_file("advent4.txt")
    count = 0
    for item in info:
        if valid(item): 
            count = count +1
    print(count)

def valid(record: Dict[str, str]) -> bool:
    ks = list(record.keys())
    allk    = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]
    allplus = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    ok:bool = eq(ks, allk) or eq(ks, allplus)
    if ok :
        ok = revalid(record)
        if ok:
            print(dict(sorted(record.items())))
        return ok
    return False

def revalid(record: Dict[str, str]) -> bool:
    byr = record.get("byr")
    if not validate_year(byr, 1920,2002):
        #print('byr')
        return False
    iyr = record.get("iyr")
    if not validate_year(iyr, 2010,2020):
        #print('iyr')
        return False
    eyr = record.get("eyr")
    if not validate_year(eyr, 2020,2030):
        #print('eyr')
        return False
    hgt = record.get("hgt")
    if not validate_height(hgt):
        #print('hgt')
        return False 
    hcl = record.get("hcl")
    if not validate_haircolor(hcl):
        #print('hcl')
        return False
    ecl = record.get("ecl")
    if not validate_eyecolor(ecl):
        #print('ecl')
        return False
    pid = record.get("pid")
    if not validate_passport(pid):
        #print('pid')
        return False
    return True

def validate_height(year:str) -> bool:
    if year.endswith("cm"):
        cm:int = int(year[0:-2])
        return 150 <=cm <=193
    elif year.endswith("in"):
        inch:int = int(year[0:-2])
        return 59<=inch<=76
    else:
        return False

def validate_haircolor(color:str) -> bool:
    if len(color) != 7 or color[0] != '#':
        return False
    for c in color[1:]:
        if not ('0'<=c<='9' or 'a'<=c<='f'):
            return False
    return True

def validate_eyecolor(color:str) -> bool:
    return color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_passport(year:str) -> bool:
    reg = re.compile("^\d\d\d\d\d\d\d\d\d$")
    return reg.match(year) and 0<=int(year)<=999999999

def validate_year(year:str, min:int, max:int) -> bool:
    reg = re.compile("\d\d\d\d")
    m = reg.match(year)
    return (m and min<=int(year)<=max)

def eq(a:List[str], b:List[str]) -> bool:
    return Counter(a) == Counter(b)

def read_file(name:str) -> List[Dict[str, str]]:
    out:List[Dict[str, str]] = []
    with open(name, "r") as file:
        record:Dict[str,str] = {}
        for line in file:
            if line == '\n':
                out.append(record)
                record = {}
            else:
                chunks:List[str] = line.rstrip().split(' ')
                for chunk in chunks:
                    pair:List[str] = chunk.split(':')
                    record[pair[0]]=pair[1]
    if len(record) > 0:
         out.append(record)
    return out


if __name__ == "__main__":
    main()