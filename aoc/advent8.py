from typing import List, NoReturn, Tuple, Dict
import re
from enum import Enum

class Op(Enum):
    NOP='nop',
    ACC='acc',
    JMP='jmp'

Ins = Tuple[Op, int]

def main() -> NoReturn:
    exercise2()


def exercise2() -> NoReturn:
    rules: List[Ins] = read_file("aoc/advent8.txt")
    for i in range(len(rules)):
        rule = rules[i]
        if rule[0] == Op.NOP:
            r = (Op.JMP, rule[1])
            rules[i] = r
            (end, acc) = run(rules)
            rules[i] = rule
            if end:
                print(acc)
                return
        elif rule[0] == Op.JMP:
            r = (Op.NOP, rule[1])
            rules[i] = r
            (end, acc) = run(rules)
            rules[i] = rule
            if end:
                print(acc)
                return


def exercise1() -> NoReturn:
    rules: List[Ins] = read_file("aoc/advent8.txt")
    (end, acc) = run(rules)
    print(acc)

def run(rules: List[Ins]) -> Tuple[bool, int]:
    status: List[bool] = [False for x in rules]
    acc: int = 0
    pc:  int = 0
    l: int = len(rules)
    while pc != l and not status[pc]:
        ins: Ins = rules[pc]
        status[pc] = True
        op = ins[0]
        addr = ins[1]
        if op == Op.NOP:
            pc = pc + 1
        elif op == Op.JMP:
            pc = pc + addr
        elif op == Op.ACC:
            acc = acc + addr
            pc = pc + 1
    if pc == l:
        return (True, acc)
    else:
        return (False, acc)


def read_file(name:str) -> List[str]:
    with open(name, "r") as file:
        l: List[str] = [line.rstrip('\n') for line in file.readlines()]
        return parse(l)

def parse(lines: List[str]) -> List[Ins]:
    rnop = re.compile("^nop (\+\d+|\-\d+)$")
    racc = re.compile("^acc (\+\d+|\-\d+)$")
    rjmp = re.compile("^jmp (\+\d+|\-\d+)$")
    out: List[Ins] = []
    for line in lines:
        mnop = rnop.match(line)
        if mnop:
            out.append((Op.NOP, offset(mnop.group(1))))
        else:
            macc = racc.match(line)
            if macc:
                out.append((Op.ACC, offset(macc.group(1))))
            else:
                mjmp = rjmp.match(line)
                if mjmp:
                    out.append((Op.JMP, offset(mjmp.group(1))))
    return out

def offset(s: str) -> int:
    return int(s)

if __name__ == "__main__":
    main()
