#Data
data = "I0NvZGUKZnJvbSBiYXNlNjQgaW1wb3J0IGI2NGRlY29kZQplbmNvZGluZz0idXRmLTgiCgpkZWYgZGVjKHM6IHN0cikgLT4gc3RyOgogICAgcmV0dXJuIGI2NGRlY29kZShzLmVuY29kZShlbmNvZGluZykpLmRlY29kZShlbmNvZGluZykKCmRlZiBtYWluKCk6CiAgICBwcmludCgiI0RhdGEiKQogICAgcHJpbnQoImRhdGEgPSBcIiVzXCIiJShkYXRhKSkKICAgIHByaW50KGRlYyhkYXRhKSkKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBtYWluKCk="
#Code
from base64 import b64decode
encoding="utf-8"

def dec(s: str) -> str:
    return b64decode(s.encode(encoding)).decode(encoding)

def main():
    print("#Data")
    print("data = \"%s\""%(data))
    print(dec(data))

if __name__ == "__main__":
    main()