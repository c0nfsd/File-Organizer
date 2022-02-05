import pathlib as p
import os

path = ""
files = []


def main():
    global path

    path = p.Path(input("Enter Path :"))
    for i in path.glob("*"):
        print(i)
        # files.append(i)
    # print(files)


if __name__ == "__main__":
    main()
