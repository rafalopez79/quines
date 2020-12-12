from typing import List, NoReturn,Tuple
import re
from collections import Counter


def main() -> NoReturn:
    info: List[Tuple[int,int,str,str]] = read_file("advent2.txt")
    count = 0
    for item in info:
        if (validate2(item)):
            count = count + 1
    print(count)

def validate(input: Tuple[int,int,str,str]) -> bool:
    start: int = input[0]
    end: int = input[1]
    letter = input[2]
    text = input[3]
    counter = Counter(text)
    count: int = counter.get(letter)
    return not count is None and start<=count<=end

def validate2(input: Tuple[int,int,str,str]) -> bool:
    start: int = input[0]
    end: int = input[1]
    letter = input[2]
    text = input[3]
    first: bool = text[start-1] == letter
    second: bool = text[end-1] == letter
    return first != second

def read_file(name:str) -> List[Tuple[int,int,str,str]]:
    r = re.compile("(\d+)-(\d+) (\w): (\w+)")
    out:List[Tuple[int,int,str,str]] = []
    with open(name, "r") as file:
        for line in file:
            m = r.match(line)
            if m and len(m.groups())==4:
                start:int = int(m.group(1))
                end:int = int(m.group(2))
                letter:str = m.group(3)
                word:str = m.group(4)
                out.append((start, end, letter, word))
    return out


if __name__ == "__main__":
    main()