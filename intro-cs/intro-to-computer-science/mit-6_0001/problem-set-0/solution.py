import numpy


def main():
    x = int(input("Enter number X: ").strip())
    y = int(input("Enter number Y: ").strip())
    print("X**Y = ", x**y)
    print("log(X) = ", numpy.log2(x))


if __name__ == "__main__":
    main()
