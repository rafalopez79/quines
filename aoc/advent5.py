from typing import List, NoReturn, Tuple


def main() -> NoReturn:
    data: List[str] = read_file("aoc/advent5.txt")
    rows: int = 128
    cols: int = 8
    maxseatid: int = 0
    seatids : List[int] = []
    for item in data:
        (row, col) = to_rowinfo(item, rows, cols)
        seatid: int = seat_id(row, col)
        seatids.append(seatid)
        if seatid > maxseatid:
            maxseatid = seatid
    print(maxseatid)
    seatids.sort()
    minseat: int = min(seatids)
    maxseat: int = max(seatids)
    for s in range(minseat, maxseat):
        if s != minseat and s != maxseat and s not in seatids and (s+1) in seatids and (s-1) in seatids:
            print(s)
            break



def to_rowinfo(data:str, rows: int, cols: int) -> Tuple[int,int]:
    rinfo: str = data[:7]
    cinfo: str = data[7:]
    r: int = to_row(rinfo, rows, 'F', 'B')
    c: int = to_row(cinfo, cols, 'L', 'R')
    return (r, c)

def to_row(rinfo: str, rows: int, front: str, back: str) -> int:
    rowl: int = 0
    rowh: int = rows
    half: int = rows
    for c in rinfo:
        half = half//2
        if c == front:
            rowh =  rowh - half
        elif c == back:
            rowl = rowl + half
    rowh = rowh-1
    assert(rowl==rowh)
    return rowl


def seat_id(row: int, col: int) -> int:
    return row * 8 + col



def read_file(name:str) -> List[str]:
    with open(name, "r") as file:
        return [line.rstrip('\n') for line in file.readlines()]

if __name__ == "__main__":
    main()
