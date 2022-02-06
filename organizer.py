import pathlib as p
import os

path = ""
files = []
ext = set()


def get_ext():
    for i in files:
        if i.is_file():
            ext.add(i.suffix.replace(".", ""))


def make_folder():
    for i in ext:
        try:
            # print()
            os.mkdir(path / i)
        except:
            pass


def move_files():
    for i in files:
        try:
            os.rename(i, path / i.suffix.replace(".", "") / i.name)  # moving files using rename function
        except:
            pass


def main():
    global path

    path = p.Path(input("Enter Path :"))
    for i in path.glob("*"):
        # print(i)
        files.append(i)
    get_ext()
    # print(ext)
    make_folder()
    move_files()


if __name__ == "__main__":
    main()
