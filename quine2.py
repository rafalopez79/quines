import inspect
import sys

def main():
    print(inspect.getsource(sys.modules[__name__]))

if __name__ == "__main__":
    main()