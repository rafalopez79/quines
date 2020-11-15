#Data
data = """
def main():
    print("#Data")
    print("data = \\"\\"\\"%s\\"\\"\\"\\"%(data))
    print(data)

if __name__ == "__main__":
    main()
"""
#Code
def main():
    print("#Data")
    print("data = \"\"\"%s\"\"\""%(data))
    print(data)

if __name__ == "__main__":
    main()