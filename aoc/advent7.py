from typing import List, NoReturn, Tuple, Dict
import re


def main() -> NoReturn:
    exercise2()

def exercise2() -> NoReturn:
    rules: List[str] = read_file("aoc/advent7.txt")
    processed: Dict[str, List[Tuple[int, str]]] = parse_rules(rules)
    mybag = 'shiny gold'
    count = explore(processed, mybag)
    print(count - 1)

def explore(rules: Dict[str, List[Tuple[int, str]]], key: str) -> int:
    values: List[Tuple[int, str]] = rules.get(key)
    if values:
        total = 1
        for t in values:
            num: int = t[0]
            content: str = t[1]
            total = total + num * explore(rules, content)
        return total
    else:
        return 1

def exercise1() -> NoReturn:
    rules: List[str] = read_file("aoc/advent7.txt")
    processed: Dict[str, List[Tuple[int, str]]] = parse_rules(rules)
    mybag = 'shiny gold'
    count = 0
    for key in processed:
        if bear(processed, key, mybag):
            count = count + 1
    print(count)

def contains(data: List[Tuple[int, str]], item: str) -> bool:
    for x in data:
        if x[1] == item:
            return True
    return False

def bear(rules: Dict[str, List[Tuple[int, str]]], key: str, item:str) -> bool:
    values = rules.get(key)
    if not values is None:
        if contains(values, item):
            return True
        else:
            for v in values:
                if bear(rules, v[1], item):
                    return True
    return False



def parse_rules(rules: List[str]) -> Dict[str, List[Tuple[int, str]]]:
    r = re.compile("^(\w+) (\w+) bags contain ([\w\d\s.,]+).$")
    out = {}
    for rule in rules:
        m = r.match(rule)
        if m:
            color: str = m.group(1)+' '+m.group(2)
            children: List[Tuple[int, str]] = process_children(m.group(3))
            out[color] = children
    return out


def process_children(text: str) -> List[Tuple[int, str]]:
    r = re.compile("^(\d+) (\w+) (\w+) bags?$")
    splitted = text.split(',')
    out = []
    for item in splitted:
        item = item.strip()
        if item == 'no other bags.':
           continue
        else:
            m = r.match(item)
            if m:
                number: int = int(m.group(1))
                color: str = m.group(2)+' '+m.group(3)
                out.append((number, color))
    return out


def read_file(name:str) -> List[str]:
    with open(name, "r") as file:
        return [line.rstrip('\n') for line in file.readlines()]


if __name__ == "__main__":
    main()
