from typing import List, NoReturn, Tuple, Set, Dict


def main() -> None:
    exercise2()

def exercise2() -> None:
    nums: List[int] = read_file("aoc/advent10.txt")
    nums.sort(reverse=True)
    nums.append(0)
    end = max(nums)
    value = process_all(nums, 0, end)
    print(value)

def eval( s: Set[int], record: Dict[int, int], val: int):
    count = 0
    if val+1 in s:
        count = count + record.get(val+1,0)
    if val+2 in s:
        count = count + record.get(val+2,0)
    if val+3 in s:
        count = count + record.get(val+3,0)
    return count

def process_all(nums: List[int], start: int, end: int) ->int:
    values:  Set[int] = set(nums)
    records: Dict[int,int] = {}
    records[end] = 1
    for i in nums:
        v = eval(values, records, i)
        records[i] = v + records.get(i, 0)
    return records[0]

    

def next(input: Set[int], value: int) -> List[int]:
    out: List[int] = []
    for n in range(1,4):
        v = value + n
        if v in input:
            out.append(v)
    return out

def exercise1() -> NoReturn:
    nums: List[int] = read_file("aoc/advent10.txt")
    myjoltage = max(nums) 
    start = 0
    (ones, threes) = process(nums, start, myjoltage)
    print(ones * threes)

def process(nums: Set[int], start: int, end: int) -> Tuple[int,int]:
    current = start
    out = [start]
    used: Set[int] = set(nums)
    ones = 0
    threes = 0
    while current != end:
        if (current + 1) in used:
            out.append(current +1)
            used.remove(current+1)
            ones = ones + 1
            current = current +1
        elif (current + 2) in used:
            out.append(current +2)
            used.remove(current+2)
            current = current +2
        elif (current + 3) in used:
            out.append(current +3)
            used.remove(current+3)
            current = current +3
            threes = threes + 1
    return (ones, threes + 1)


def read_file(name:str) -> List[int]:
    with open(name, "r") as file:
        l: List[str] = [line.rstrip('\n') for line in file.readlines()]
        return [int(x) for x in l]

if __name__ == "__main__":
    main()
