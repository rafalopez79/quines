from typing import List, NoReturn, Tuple, Dict

def main() -> NoReturn:
    exercise1()


def exercise1() -> NoReturn:
    nums: List[int] = read_file("aoc/advent9.txt")
    preamble: int = 25
    selected: int = 0
    for i in range(len(nums)):
        if i < preamble:
            continue
        else:
            item: int = nums[i]
            preamblelist = nums[i-25:i]
            if not check(item, preamblelist):
                selected = item
                break
    print(selected)
    cont: int = contiguous(nums, selected)
    print(cont)

def contiguous(nums: List[int], num: int) -> int:
    for i in range(len(nums)):
        s: int = nums[i]
        for j in range(i + 1, len(nums)):
            s = s + nums[j]
            if s == num:
                l: List[int] = nums[i:j]
                high = max(l)
                low = min(l)
                return high + low
    return 0

def check(num: int, preamble: List[int]) -> bool:
    for i in range(len(preamble)):
        for j in range(len(preamble)):
            if i != j and preamble[i] + preamble[j] == num:
                return True
    return False


def read_file(name:str) -> List[int]:
    with open(name, "r") as file:
        l: List[str] = [line.rstrip('\n') for line in file.readlines()]
        return [int(x) for x in l]

if __name__ == "__main__":
    main()
