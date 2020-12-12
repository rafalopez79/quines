from typing import List, NoReturn


def main() -> NoReturn:
    data: List[int] = read_file("advent1.txt")
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if i != j and j !=k and (data[i] + data[j] + data[k] == 2020):
                    print(data[i] * data[j] * data[k])
                    return
    print("Not Found")

def read_file(name:str) -> List[int]:
    with open(name, "r") as file:
        return list(map(int, file.readlines()))

if __name__ == "__main__":
    main()