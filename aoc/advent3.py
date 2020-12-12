from typing import List, NoReturn
from collections import Counter


def main() -> NoReturn:
    info: List[List[str]] = read_file("advent3.txt")
    count1 = execute(1,1,info)
    count2 = execute(3,1,info)
    count3 = execute(5,1,info)
    count4 = execute(7,1,info)
    count5 = execute(1,2,info)
    print(count1*count2*count3*count4*count5)

def execute(r:int, d:int, info: List[List[str]]) -> int:
    posr:int = 0
    posd:int = 0
    count:int = 0
    size: int = len(info)
    width: int = len(info[0])
    while posd < size:
        if info[posd][posr] == '#':
            count = count + 1
        posd = posd + d
        posr = (posr + r) % width
    return count



def read_file(name:str) -> List[List[str]]:
    out:List[List[str]] = []
    with open(name, "r") as file:
        for line in file:
            lline: List[str] = []
            for letter in line:
                if letter != '\n':
                    lline.append(letter)
            out.append(lline)
    return out


if __name__ == "__main__":
    main()