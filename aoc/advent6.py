from typing import List, NoReturn, Tuple, Set


def main() -> NoReturn:
    data: List[List[str]] = read_file("aoc/advent6.txt")
    processed: List[Set[str]] = process2(data)
    count: int = 0
    for s in processed:
        count = count + len(s)
    print(count)

def process1(data: List[List[str]]) -> List[Set[str]]:
    out: List[Set[str]] = []
    for item in data:
        l: List[str] = []
        for elements in item:
            l.extend(elements)
        out.append(set(l))
    return out

def process2(data: List[List[str]]) -> List[Set[str]]:
    out: List[Set[str]] = []
    for item in data:
        l: List[str] = []
        for elements in item:
            l.extend(elements)
        s:Set[str] = set(l)
        for elements in item:
            s = s.intersection(set(elements))
        out.append(s)
    return out

def read_file(name:str) -> List[List[str]]:
    out: List[List[str]] = []
    with open(name, "r") as file:
        record: List[str] = []
        for line in file.readlines():
            if line == '\n':
                out.append(record)
                record = []
            else:
                line = line.rstrip('\n')
                record.append(line)
        if len(record) > 0:
            out.append(record)
    return out


if __name__ == "__main__":
    main()
